# TASK.2025-10-19-0001

## 目的
- Roadmap 優先度 #2（CI・自動化基盤）に基づき、lint/type/test/publish の品質ゲートを整備する。
- Guardrails のテスト先行・最小差分原則を守り、CI とリリース判定の一貫性を確保する。

## 要件
- GitHub Actions で `ruff`・`mypy --strict`・`pytest`・`node:test` をジョブ分割し、Secrets 不在時は統合テストを Graceful Skip させる。
- タグ push トリガーの release ワークフローで Docker Buildx + GHCR publish を実行する。
- CI 結果と `docs/Release_Checklist.md` / `docs/Security_Review_Checklist.md` を紐付けて、DoD 判断に使用できる状態にする。
- Birdseye 図と Task Seed を更新し、変更理由とフォローアップを追跡できるようにする。

## 想定コマンド
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-eval.txt  # CI ワークフローのローカル検証
npm install  # node:test が必要な場合
pytest
npm test -- --watch=false  # node:test の雛形
ruff check .
mypy --strict
act -W .github/workflows/ci.yml  # 任意: GitHub Actions のローカルドライラン
```

## 受入基準
- CI 実行ログで lint/type/test が成功し、Secrets なし環境で統合テストがスキップされる。
- Docker イメージが GHCR に push され、`vX.Y.Z-katamari` 形式のタグで管理される。
- `CHECKLISTS.md` と `RUNBOOK.md` に CI/リリース手順が反映され、`EVALUATION.md` で DoD 判定が可能。

## フォローアップ
- Guardrails の「テスト先行・最小差分」原則に従い、未解決項目は後続 Task Seed または Issue に分割する。
- Birdseye index/caps を更新し、CI・リリース関連ノードの可視化を維持する。

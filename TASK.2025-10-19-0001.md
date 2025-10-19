# TASK.2025-10-19-0001

## 目的
- Roadmap 優先度 #2 に基づき、CI（lint/type/test/publish）を整備して開発フローの品質基盤を確立する。[docs/ROADMAP_AND_SPECS.md](docs/ROADMAP_AND_SPECS.md)。

## 要件
- GitHub Actions で `ruff`・`mypy --strict`・`pytest`・`node:test` をジョブ分割し、Secrets 不在時は統合テストをスキップ。
- タグ push トリガーの release ワークフローで Docker Buildx + GHCR publish を行う。
- Release/Security チェックリストと CI 結果をリンクし、リリース判定に利用できる状態にする。
- Guardrails の最小差分・タスク分割方針を遵守し、未対応項目は追跡可能にする。[third_party/Day8/workflow-cookbook/GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)。

## 想定コマンド
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-eval.txt  # CI ワークフローのローカル検証用
npm install  # node:test 対応が必要な場合
pytest
npm test -- --watch=false  # node:test の雛形
ruff check .
mypy --strict
act -W .github/workflows/ci.yml  # 任意。ローカルで GH Actions をドライラン
```

## 受入基準
- CI 実行ログで lint/type/test が成功し、Secrets なし環境で統合テストが Graceful Skip になる。
- Docker イメージが GHCR に push され、`vX.Y.Z-katamari` 形式のタグで管理される。
- Release/Security チェックリストと CI のリンク方法が `CHECKLISTS.md` に追記されている。

## 成果物 / エビデンス
- `.github/workflows/ci.yml`, `.github/workflows/release.yml`
- CI 実行ログ、GHCR の最新タグ一覧
- 更新された `CHECKLISTS.md`, `RUNBOOK.md`, `EVALUATION.md`

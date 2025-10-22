# TASK.2025-10-23-0001

## 目的
- Guardrails ドキュメントの保守に向けて、2025-10-23 実施分の差分検証と記録を行う。
- `TASK.2025-10-19-0001.md` で確立した手順を踏襲し、テスト・Lint・型チェック運用を統一する。

## 要件
- BLUEPRINT/RUNBOOK/EVALUATION/CHECKLISTS の差分確認ログを収集し、再試行可否や担当を明示する。
- README と `docs/ROADMAP_AND_SPECS.md` の導線を再確認し、変更があれば Task Seed に記録する。
- Guardrails 文書更新の理由と採否を Task Seed に追記し、Birdseye 更新と同日にコミットする。
- Lint/Type/Test（`ruff`/`mypy --strict`/`pytest`/`pnpm run test`）の実行計画を RUNBOOK と同期し、結果ログの保存先を Task Seed で管理する。
- チェックリスト差分が発生した場合はフォローアップを作成し、後続タスクを準備する。

## 想定コマンド
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-eval.txt  # CI ワークフローのローカル検証
cd upstream/chainlit && pnpm install  # `pnpm run test` を実行する場合に必要
pytest
pnpm run test -- --watch=false  # 正式なテスト実行手順（`pnpm run test -- --watch=false`）
ruff check .
mypy --strict
rg -n "BLUEPRINT" third_party/Day8/workflow-cookbook/GUARDRAILS.md
rg -n "RUNBOOK" third_party/Day8/workflow-cookbook/GUARDRAILS.md
rg -n "EVALUATION" third_party/Day8/workflow-cookbook/GUARDRAILS.md
rg -n "CHECKLIST" third_party/Day8/workflow-cookbook/GUARDRAILS.md
```

## 受入基準
- CI 実行ログで lint/type/test が成功し、Secrets なし環境で統合テストがスキップされる。
- Docker イメージが GHCR に push され、`vX.Y.Z-katamari` 形式のタグで管理される。
- `CHECKLISTS.md` と `RUNBOOK.md` に CI/リリース手順が反映され、`EVALUATION.md` で DoD 判定が可能。
- Guardrails 文書（HUB/BLUEPRINT/RUNBOOK/EVALUATION/CHECKLISTS）の相互参照が更新されている。

## フォローアップ
- Guardrails の「テスト先行・最小差分」原則に従い、未解決項目は後続 Task Seed または Issue に分割する。
- Birdseye index/caps を更新し、CI・リリース関連ノードの可視化を維持する。
- Guardrails 文書更新の差分と今後のタスクを Task Seed 内で管理する。
- 認証方式導入のフォローアップは [`TASK.2025-10-19-0002.md`](TASK.2025-10-19-0002.md) に集約する。

# RUNBOOK

## 目的
- Katamari 基盤の起動・検証・障害対応を標準化し、ガードレールとロードマップの要件を逸脱せずに運用する。関連仕様: [docs/ROADMAP_AND_SPECS.md](docs/ROADMAP_AND_SPECS.md)。

## スコープ
### In Scope
- ローカル/CI 環境でのアプリ起動、Persona/Trim/Reflect チェーンの動作確認。
- SSE/ログ監視、Provider 設定、基本的な障害復旧フロー。
- Guardrails で定義された最小読込プロセスの遵守確認。[GUARDRAILS](third_party/Day8/workflow-cookbook/GUARDRAILS.md)。

### Out of Scope
- SLA ベースの 24/7 運用（別途 SRE Runbook を策定）。
- プロバイダ課金/秘密情報の管理（`docs/addenda/G_Security_Privacy.md` 参照）。

## 手順
### 1. 準備
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt` と `npm install`（必要時）。
3. `.env.example` を参照し Provider キー・Chainlit 設定を環境変数に投入。
4. Birdseye index/caps の鮮度を確認し、必要なら `scripts/birdseye_refresh.py` を実行。

### 2. 実行
1. `chainlit run src/app.py --watch`
2. Persona YAML を `personas/` からロードし UI で切替を確認。
3. Trim/Reflect チェーンのログを `logs/` で監視し、トークン削減率を記録。
4. Provider を切り替え `docs/addenda/F_Provider_Matrix.md` の互換チェックを行う。

### 3. 検証・障害対応
1. pytest / mypy / ruff / node:test を実行し、失敗した場合は Guardrails の「最小差分」ポリシーに従って修正。
2. SSE 遅延が閾値を超えた場合、`docs/addenda/J_Runbook.md` のトラブルシュート手順に従う。
3. 重大障害は `CHANGELOG.md` に記録し、関連 Task Seed を更新。

## Acceptance Criteria
- 起動直後に Persona 選択・Trim/Reflect チェーンが正常に表示される。
- `ruff`・`mypy --strict`・`pytest`・`node:test` が全て成功するか、既知の skip 理由が記録されている。
- SSE 遅延・トークン削減率が `docs/Katamari_Requirements_v3_ja.md` の目標値を満たす。

## チェック項目
- [ ] `.env` に Secrets を埋めず、環境変数読み込みのみで起動できる。
- [ ] Guardrails の最小読込手順（README → index.json → caps）を実施済み。
- [ ] Birdseye 更新日時が直近コミット以降になっている。
- [ ] 失敗テストがある場合、理由と再実行計画が Task Seed に記録されている。

## 参照リンク
- [docs/ROADMAP_AND_SPECS.md](docs/ROADMAP_AND_SPECS.md)
- [docs/addenda/J_Runbook.md](docs/addenda/J_Runbook.md)
- [docs/addenda/H_Deploy_Guide.md](docs/addenda/H_Deploy_Guide.md)
- [third_party/Day8/workflow-cookbook/GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)

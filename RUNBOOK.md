# RUNBOOK

## 目的
- Katamari の起動・検証・障害対応を標準化し、Guardrails とロードマップで定義された要件を逸脱せずに運用する。
- 変更の影響範囲を即座に共有できるよう、起動から復旧までの手順と証跡取得方法を記録する。

## 担当ロール
- SRE / オンコール担当: 障害対応と復旧の一次手順を把握し、証跡を残す。
- DevOps / CI 担当: 起動・検証の標準シーケンスを維持し、CI との整合をチェックする。
- プロダクトメンテナー: 運用変更がガードレール手順と矛盾しないかをレビューする。

## スコープ
### In Scope
- ローカル / CI 環境でのアプリ起動と Persona/Trim/Reflect チェーン動作確認。
- SSE 遅延やログ監視、Provider 設定の切替、基本的な障害復旧フロー。
- Guardrails が要求する最小読込・自己検証プロセスの実施。

### Out of Scope
- 24/7 SRE 運用や SLA 監視（別途 Runbook を策定）。
- プロバイダ課金や秘密情報の管理（`docs/addenda/G_Security_Privacy.md` を参照）。

## 手順
Guardrails の「準備→実行→検証」順で進める。

### 1. 準備
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt` と必要に応じて `npm install`。
3. `.env.example` を参照して Provider キーなどの環境変数を設定する。
4. Birdseye index/caps を確認し、必要であれば `scripts/birdseye_refresh.py` を実行する。

### 2. 実行
1. `chainlit run src/app.py --watch`
2. Persona YAML を `personas/` からロードし、UI で切替を検証する。
3. Trim/Reflect チェーンのログを `logs/` で監視し、トークン削減率を記録する。
4. Provider を切り替え、`docs/addenda/F_Provider_Matrix.md` の互換チェックを行う。

### 3. 検証・障害対応
1. `pytest` / `node:test` / `ruff` / `mypy --strict` を実行し、失敗時は Guardrails の最小差分方針で修正する。
2. SSE 遅延が閾値を超えた場合、`docs/addenda/J_Runbook.md` のトラブルシュート手順を参照する。
3. 重大障害は `CHANGELOG.md` と Task Seed に記録し、必要なら `RUNBOOK.md` を更新する。

## 最小フロー
1. `docs/ROADMAP_AND_SPECS.md` で対象フェーズと関連タスクを特定する。
2. 「準備→実行→検証」の順に手順を辿り、証跡を `CHECKLISTS.md` の該当フェーズへ転記する。
3. 異常があれば `TASK.*.md` にフォローアップを登録し、再発防止策を検討する。
4. 受入判断を `EVALUATION.md` の AC と照合し、満たない場合は再実行計画を記す。
5. `third_party/Day8/workflow-cookbook/GUARDRAILS.md` の「RUNBOOK」節を参照し、標準手順から逸脱していないかレビューする。

## 受入基準
- 起動直後に Persona 選択と Trim/Reflect チェーンが UI に表示される。
- `ruff`・`mypy --strict`・`pytest`・`node:test` が成功、またはスキップ理由が記録されている。
- SSE 遅延とトークン削減率が `docs/Katamari_Requirements_v3_ja.md` の目標を満たす。
- Guardrails RUNBOOK の `Procedure / Acceptance` 記述と矛盾がない。

## チェック項目
- [ ] Secrets を含む `.env` をリポジトリに残していない。
- [ ] Guardrails の最小読込手順（README → index.json → caps）を実施した。
- [ ] Birdseye 更新日時が直近コミット以降になっている。
- [ ] 失敗テストの理由と再実行計画が Task Seed に記録されている。
- [ ] Guardrails RUNBOOK 節（`third_party/Day8/workflow-cookbook/GUARDRAILS.md`）の手順を参照した。

## 参照
- [docs/ROADMAP_AND_SPECS.md](docs/ROADMAP_AND_SPECS.md)
- [docs/addenda/J_Runbook.md](docs/addenda/J_Runbook.md)
- [docs/addenda/H_Deploy_Guide.md](docs/addenda/H_Deploy_Guide.md)
- [third_party/Day8/workflow-cookbook/GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)

# EVALUATION

## 目的
- Katamari の成果物が仕様・非機能要件・Guardrails を満たしているか判断する枠組みを提供する。
- 受入可否を明確にし、差分が残る場合は Task Seed へフォローアップを連携する。

## スコープ
### In Scope
- `docs/Katamari_Requirements_v3_ja.md` / `docs/Katamari_Functional_Spec_v1_ja.md` に基づく機能評価。
- 非機能（性能・セキュリティ・可観測性）指標の測定と合否判断。
- Task Seed とチェックリストで定義された DoD の追跡。

### Out of Scope
- PMF の評価やビジネス指標の測定。
- SLA/アラートの常時監視（SRE 評価に委譲）。

## 評価ステップ
1. `RUNBOOK.md` に従って環境を起動し、`pytest` / `node:test` / `ruff` / `mypy --strict` を実行する。
2. `scripts/perf/collect_metrics.py`（想定）や Chainlit ログから性能指標を取得し、要件値と比較する。
3. `docs/Release_Checklist.md` と `docs/Security_Review_Checklist.md` の結果を確認し、未完了項目があれば Task Seed に登録する。
4. 判定結果を Issue / PR / `CHANGELOG.md` に記録し、必要なら `RUNBOOK.md`・`CHECKLISTS.md` を更新する。
5. `third_party/Day8/workflow-cookbook/GUARDRAILS.md` の「EVALUATION」節で定義された指標と比較し、差異があれば補足を記録する。

## 指標
- 機能: Persona 切替、Trim/Reflect、多段推論の成功率。
- 性能: SSE p95、UI 反映遅延、トークン削減率（`docs/Katamari_Requirements_v3_ja.md` の数値）。
- セキュリティ: リリース / セキュリティチェックリストの完了状況。
- 再現性: Birdseye 図と Task Seed の証跡が最新コミット以降であること。

## 受入基準
- 主要ユーザーフローが設計通り完遂し、指標が要件内である。
- チェックリストの必須項目が `PASS` か `N/A`（理由付き）で記録されている。
- 未達成項目は Task Seed にフォローアップが登録され、対応計画が明記されている。
- Guardrails EVALUATION の Acceptance 条件を満たさない場合は差分理由が明記されている。

## チェック項目
- [ ] Lint / type / test / node:test の結果ログを保管した。
- [ ] 性能指標（SSE p95、UI 遅延、トークン削減率）を測定し、要件と比較した。
- [ ] セキュリティ / リリースチェックリストをレビューし、未完了項目を Task Seed に転記した。
- [ ] 判定結果を `docs/ROADMAP_AND_SPECS.md` の対象フェーズへ反映した。
- [ ] Guardrails EVALUATION 節（`third_party/Day8/workflow-cookbook/GUARDRAILS.md`）と照合した。

## 参照
- [docs/ROADMAP_AND_SPECS.md](docs/ROADMAP_AND_SPECS.md)
- [docs/Release_Checklist.md](docs/Release_Checklist.md)
- [docs/Security_Review_Checklist.md](docs/Security_Review_Checklist.md)
- [third_party/Day8/workflow-cookbook/GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)

# EVALUATION

## 目的
- Katamari プロジェクトの成果物が要求仕様・非機能要件・Guardrails に適合しているかを検証するための受入判断枠組みを提供する。

## スコープ
### In Scope
- `docs/Katamari_Requirements_v3_ja.md`・`docs/Katamari_Functional_Spec_v1_ja.md` に基づく機能評価。
- 非機能（性能・セキュリティ・可観測性）指標の測定と合否判断。
- Task Seed / Checklist で定義された DoD（Definition of Done）の追跡。

### Out of Scope
- プロダクト市場適合（PMF）の評価。
- SLA 監視・アラート設定（別途 SRE 評価で実施）。

## Acceptance Criteria
- 主要ユーザーフロー（Persona 切替、Trim/Reflect、多段推論）が設計通りに完遂する。
- SSE p95・UI 反映遅延・トークン削減率が要件値以内。
- セキュリティ・リリースチェックリストが全て `PASS` で記録され、例外は Task Seed にフォローアップ済み。

## 手順
Guardrails の「AC → 評価 → Task Seed 更新」順を踏まえ、各工程で `docs/ROADMAP_AND_SPECS.md` 1.〜3.章の対象リンクを参照する。
1. `RUNBOOK.md` に従い環境を起動し、テストスイート（pytest / node:test）を実行する。
2. `scripts/perf/collect_metrics.py`（仮）や Chainlit ログから性能指標を採取し、要件値と比較する。
3. `docs/Release_Checklist.md`, `docs/Security_Review_Checklist.md` の結果を確認し、未完了項目があれば Task Seed を更新。
4. 判定結果を `CHANGELOG.md` と対応する Issue / PR に記録する。

## 最小フロー
1. `docs/ROADMAP_AND_SPECS.md` から評価対象フェーズと関連仕様を抽出。
2. `RUNBOOK.md` に沿って環境を起動し、lint/type/test の証跡を取得。
3. 計測結果とチェックリストの状態を照合し、満たない項目は `TASK.*.md` にフォローアップを記載。
4. 受入可否を判断し、`BLUEPRINT.md` や Birdseye の更新が必要な場合は次回サイクルでの反映を手配。

## チェック項目
- [ ] すべての Acceptance Criteria が満たされ、証跡（ログ/スクリーンショット/計測値）が保存されている。
- [ ] 未達成項目は Task Seed でフォローアップが登録されている。
- [ ] Guardrails の要求するメンタル lint/type/test チェックを完了済み。
- [ ] 評価結果が `docs/ROADMAP_AND_SPECS.md` の対象フェーズに反映された。

## Guardrails 連携
- Guardrails の「AC → 評価 → Task Seed 更新」のフローに沿い、検証結果を `CHECKLISTS.md` と Issue へ連動させる。
- 計測値の算定根拠は `docs/Katamari_Technical_Spec_v1_ja.md` と `docs/addenda/F_Provider_Matrix.md` を参照して整合性を確認する。
- 評価で生じた例外は `RUNBOOK.md` にフィードバックし、同じ手順が再現できるよう補足する。

## 参照リンク
- [docs/ROADMAP_AND_SPECS.md](docs/ROADMAP_AND_SPECS.md)
- [docs/Release_Checklist.md](docs/Release_Checklist.md)
- [docs/Security_Review_Checklist.md](docs/Security_Review_Checklist.md)
- [third_party/Day8/workflow-cookbook/GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)

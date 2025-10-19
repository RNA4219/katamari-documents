# BLUEPRINT

## 目的
- Chainlit ベースの Katamari アシスタント基盤について、前処理・多段推論・評価・UI の統合像を最短で共有する設計基準を示し、全員が同じ設計判断を下せるようにする。[docs/ROADMAP_AND_SPECS.md](docs/ROADMAP_AND_SPECS.md)、[Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)。

## スコープ
### In Scope
- `src/app.py`・`src/core_ext/`・`src/providers/` の役割分離と依存関係。
- SSE/Persona/Trim/Reflect チェーンの UI 表示とトークン制御。
- Day8 Guardrails で定められた最小読込・タスク化プロセスの設計反映。[Guardrails](third_party/Day8/workflow-cookbook/GUARDRAILS.md)。

### Out of Scope
- 特定 Provider 実装詳細（各 Provider SPI ドキュメントを参照）。
- 個別テストケース・CI 設定（`docs/I_Test_Cases.md`, `TASK.*.md` に委譲）。

## 入出力 (I/O 契約)
- **入力**: Persona 設定、ユーザー入力、プロバイダ選択。スキーマは `docs/addenda/C_Persona_Schema.md` と `docs/Katamari_Functional_Spec_v1_ja.md` の UI フローを参照。
- **出力**: Trim/Reflect を経たレスポンスと SSE ストリーム。データフローは `docs/Katamari_Technical_Spec_v1_ja.md` と `third_party/Day8/workflow-cookbook/BLUEPRINT.md` の構成図に整合させる。
- **連携**: I/O 検証手順は `RUNBOOK.md` と `EVALUATION.md` に委譲し、ロードマップとの対応は `docs/ROADMAP_AND_SPECS.md` 1.〜2.章で確認する。

## Acceptance Criteria
- Persona/Trim/Reflect チェーンを含むアーキテクチャ図とデータフローが `docs/Katamari_Technical_Spec_v1_ja.md` と整合している。
- SSE 初期 p95 ≤ 1.0s、UI 反映遅延 ≤ 300ms の非機能要件が設計根拠で裏付けられている。
- Provider 切替が `docs/addenda/F_Provider_Matrix.md` の互換ポリシーで保証される構成になっている。

## 手順
1. `docs/ROADMAP_AND_SPECS.md` で対象フェーズと必須仕様を特定し、Guardrails の節構成に沿って整理する。
2. Guardrails の「目的→スコープ→I/O→AC→最小フロー」の順に、設計要素を `blueprint` セクションへ落とし込む。[third_party/Day8/workflow-cookbook/GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)。
3. `docs/birdseye/index.json` / `caps/*.json` を更新し、依存ノードの最新化を確認する。
4. 設計変更が CI・運用に影響する場合は `RUNBOOK.md`・`CHECKLISTS.md` を同時に更新し、`EVALUATION.md` の受入判断と整合させる。

## 最小フロー
1. `docs/ROADMAP_AND_SPECS.md` で対象フェーズの要件と設計変更点を洗い出す。
2. `BLUEPRINT.md` の I/O 契約と Guardrails の整合を確認し、必要な追加設計をドラフト化。
3. 影響のある手順・チェックリストを `RUNBOOK.md` / `CHECKLISTS.md` に反映し、受入条件を `EVALUATION.md` へ連携。
4. 更新内容を Task Seed (`TASK.*.md`) に記録し、Birdseye の可視化をリフレッシュする。

## チェック項目
- [ ] 主要ユースケースごとに I/O 契約（入力/出力の型・例）が定義されている。
- [ ] 例外パスと再試行可否が `Katamari_Technical_Spec_v1_ja.md` と矛盾しない。
- [ ] Birdseye index/capsule が最新コミット時刻より新しい。
- [ ] Guardrails で要求されるタスク分割と Task Seed 連携が成立している。

## Guardrails 連携
- Guardrails の「目的→スコープ→I/O→AC→最小フロー」を本書の章立てに反映した。詳細は [third_party/Day8/workflow-cookbook/GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)。
- `docs/ROADMAP_AND_SPECS.md` 2.章を参照し、該当モジュールの仕様リンクを維持する。
- Task Seed へのマッピングは `TASK.2025-10-19-0001.md` を初期例として利用する。

## 参照リンク
- [docs/ROADMAP_AND_SPECS.md](docs/ROADMAP_AND_SPECS.md)
- [docs/Katamari_Functional_Spec_v1_ja.md](docs/Katamari_Functional_Spec_v1_ja.md)
- [docs/Katamari_Technical_Spec_v1_ja.md](docs/Katamari_Technical_Spec_v1_ja.md)
- [third_party/Day8/workflow-cookbook/GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)

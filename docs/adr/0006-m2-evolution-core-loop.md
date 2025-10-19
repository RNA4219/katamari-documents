# ADR-0006: M2 プロンプト進化コアループを実装する

## Context
- 背景: M2 では Persona → Draft → Critique → Rewrite の進化ループを確立し、推論品質を継続的に改善する必要がある。
- 課題: 現状は単一プロンプトでの応答に留まり、批評・再生成ステップのオーケストレーションが欠落している。
- 参考資料: [`docs/Katamari_Functional_Spec_v1_ja.md`](../Katamari_Functional_Spec_v1_ja.md) の Prompt Evolution 章、`docs/katamari_wbs.csv` の M2 系タスク。

## Decision
- 方針: Chainlit セッション内で進化ループを構成するマネージャを `src/core_ext/evolution/` に実装し、各ステップを非同期タスクとして編成する。
- 決定理由: ステップ分割により評価・デバッグを段階的に行え、Persona/Prompt 設計の改善サイクルを短縮できる。
- 運用: Critique や Rewrite の評価指標を `/metrics` に送出し、DoD 達成状況を可視化する。失敗時は再試行可能エラーを判定してリトライ制御する。

## Consequences
- 影響範囲: Core loop 実装が `src/core_ext/` の構造に追加され、UI 側にもステップ進捗表示を実装する必要がある。
- 利点: 生成品質向上、改善ログの蓄積、M3 以降の自律学習機能の基盤形成。
- リスク/フォローアップ: 複数ステップの待ち合わせでレイテンシが増加するため、±5% 以内の SLA を維持するよう並列度とキャッシュを調整する。

## Status
- ステータス: 承認済み
- 最終更新日: 2025-02-14

## DoD
- [ ] Persona → Draft → Critique → Rewrite の各ステップがユニットテストで検証され、失敗時のリトライ条件が定義されている。
- [ ] 進化ループのオーケストレータが integration テストで 1 セッション完走することを確認している。
- [ ] `/metrics` に進化ループの成功率・平均リトライ回数が露出され、ダッシュボードで可視化されている。
- [ ] レイテンシ測定が ±5% の SLA を満たすことを測定した結果が残っている。
- [ ] Critique/Rewrite のプロンプトテンプレート変更手順がドキュメント化されている。

# ADR 0001: M1 メトリクスと保持率

- ステータス: Accepted
- 対象マイルストーン: M1

## 目的
- prethought 分析と保持率推定を導入し、圧縮後の意味損失を可視化する。
- `/metrics` と `/healthz` による可観測性を整備し、ヘッダー認証で API 保護を行う。

## スコープ
- 既存対話ログへ prethought スコア付与と保持率（semantic_retention, compress_ratio）の算出。
- `/metrics` エンドポイントで推定値および主要カウンタを公開。
- `/healthz` の Liveness/Readiness 判定実装。
- Header Bearer 認証の実装と設定項目（CHAINLIT_AUTH_SECRET）の追加。
- 既存 UI への保持率メトリクス表示。

## 受け入れ条件
1. 要件書 FR-07 に準拠し、`/metrics` と `/healthz` が稼働すること。
2. AC-04 を満たし、Header Auth が既定トークンで有効化されること。
3. WBS M1-1〜M1-4 の完了条件（prethought、保持率、メトリクス、Header Auth）が満たされること。

## DoD チェックリスト
- [ ] `/metrics` が 200 OK を返し、保持率・prethought 指標が Prometheus 形式で出力される。
- [ ] `/healthz` が readiness/liveness 判定に応じて 200/503 を返すユニットテストが存在する。
- [ ] Header Auth の有効トークン/無効トークンで 200/401 を確認するテストが CI に追加されている。
- [ ] prethought・保持率の算出ロジックに対する単体テストが AC-04 の閾値要件を検証する。
- [ ] Chainlit 設定ドキュメントに `CHAINLIT_AUTH_SECRET` 追加が反映されている。

## 関連ドキュメント
- docs/Katamari_Requirements_v3_ja.md（FR-07, AC-04）
- docs/katamari_wbs.csv（M1-1, M1-2, M1-3, M1-4）

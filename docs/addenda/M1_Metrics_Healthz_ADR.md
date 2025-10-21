# ADR M1: Health & Metrics Endpoints

- **ステータス**: 承認 (2025-10-19)
- **背景**: M1 マイルストーンで Chainlit ベースのアプリに可観測性を導入する必要がある。
- **決定**:
  - FastAPI ルーターに `GET /healthz` を追加し、200/`{"status":"ok"}` を返却する。
  - `MetricsRegistry` で `compress_ratio` / `semantic_retention` を Gauge として保持し、`GET /metrics` から Prometheus Text Format で露出する（`semantic_retention` は未実装・計画中。現状は `/metrics` に露出しない）。
- **影響**:
  - Chainlit ルートに副作用なくサブマウントでき、CI テスト (`pytest`) で監視エンドポイントが検証される。
  - 今後 `semantic_retention` の精度向上（埋め込み導入）時も、Registry 経由で値を差し替え可能（UI / `/metrics` 露出は TODO: `semantic_retention` 実装後に追記）。

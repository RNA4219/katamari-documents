# EVALUATION

## 受け入れ基準
- Persona/Trim/Reflect の設定変更が即時に反映され、System メッセージ差し替えとログ出力が同期する。
- Trim 実行時に `compress_ratio` が 0.3〜0.8 で表示され、Reflect は `draft → critique → final` の順でストリーミングされる。
- `/healthz`・`/metrics` が稼働し、M1.5 時点で OAuth 認証が有効、M1 では Header Auth での運用が可能である。
- 初回トークン p95 ≤ 1.0s、UI 反映遅延 ≤ 300ms、SSE 連続 1 分で切断率 < 1% を満たす。
- Secrets を環境変数で管理し、CORS・Rate Limit・ログマスクのセキュリティ要件を満たす。
- Apache-2.0 ライセンス順守、`vX.Y.Z-katamari` バージョニング、ruff/mypy(strict)/pytest/node:test の CI 合格を確認する。

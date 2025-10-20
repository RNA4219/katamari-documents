# 付録G: セキュリティ & プライバシー指針
**Status: 2025-10-19 JST**

- **キー管理**: `OPENAI_API_KEY` / `GOOGLE_GEMINI_API_KEY`（旧称 `GEMINI_API_KEY` 互換） はサーバENVのみ。フロント送出禁止。
- **ログ衛生**: 個人情報（PII）はマスク。必要最小限のフィールドのみ収集。
- **データ保持**: デフォルトはメモリ保持。M2.5以降でDB導入時は保持期間・削除APIを設計。
- **認証**: M1=Header（開発用）、M1.5=OAuth（本番）。
- **通信**: HTTPS / HTTP/2 / Keep-Alive。CORS制限。

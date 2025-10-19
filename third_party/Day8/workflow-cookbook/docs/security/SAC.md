---
intent_id: INT-001
owner: your-handle
status: active   # draft|active|deprecated
last_reviewed_at: 2025-10-14
next_review_due: 2025-11-14
---

# Security Architecture Contract (SAC) v0.1

対象: 全リポジトリ / エージェント実装 / Chainlit派生UI

## 原則

1. Secretsはサーバ側のみで保持し、ログ出力を禁止する。
2. LLM出力は不信任とし、HTMLはサニタイズ、リンクは `rel="noopener"` を付与する。
3. 許可Egressは LLM API と静的配信のみ。ループバックおよびメタデータIPは禁止。
4. ツール実行はスキーマ検証と許可ドメイン制御を必須とする。
5. CSRF/CORS/CSP を強制する（推奨CSPは付録A参照）。
6. Rate/Quota を設定し、RPS・同時実行・日次トークン上限を設ける。
7. 依存はバージョン固定し、既知脆弱性は CI で検出した時点で失敗させる。
8. 監査ログは PII マスクと改ざん検知を実装する。
9. モデル切替はサーバ設定のみ許可する。
10. リリース前に SAST / Secrets / Dependency / Container の4ゲートを通過する。

### 付録A: 推奨CSP

```
default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; script-src 'self'; connect-src 'self' https://api.openai.com https://generativelanguage.googleapis.com; frame-ancestors 'none'; base-uri 'none'
```

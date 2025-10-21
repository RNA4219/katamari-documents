# 付録I: テストケース集（抜粋）
**Status: 2025-10-19 JST**

## I-1. 機能
- Settings即時反映（model/chain/trim/persona）
- Reflect: 3段の順序・SSE表示・Stop後の再送
- Trim: `target_tokens`に応じてratioが変動
- Persona: 禁則語を含む入力に対する抑制確認

## I-2. 性能
- p95初回トークン ≤ 1.0s（10回×3条件）
- SSE連続1分で切断率 < 1%

## I-3. セキュリティ
- Header Auth 認証通過/失敗（手動確認対象）
- OAuthフロー（M1.5）は未実装（計画中）。[`TASK.2025-10-19-0002.md`](../../TASK.2025-10-19-0002.md) 完了までは手動確認対象外とし、実装後に試験項目を有効化する。
- ENV露出なし・CORSブロック

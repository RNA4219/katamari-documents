# 付録J: 障害時復旧（Runbook）
**Status: 2025-10-19 JST**

1. **SSEが途切れる**: リバースプロキシのバッファ設定確認（HTTP/2、flush、timeout）。
2. **初回トークン遅延**: 近接リージョン・*-miniへ切替、温度低下、Keep-Alive確認。
3. **OAuth失敗**: リダイレクトURL・クレデンシャル再確認、Header Authにフォールバック。
4. **保持率低下**: `target_tokens`増、Trim戦略をSemanticへ、要約プロンプト改善。

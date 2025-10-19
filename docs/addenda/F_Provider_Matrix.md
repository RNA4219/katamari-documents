# 付録F: Provider互換表（初期）
**Status: 2025-10-19 JST**

| 項目 | GPT-5系（OpenAI） | Gemini 2.5系（Google） |
|---|---|---|
| ストリーミング | SSE / SDKストリーム | SSE / SDKストリーム |
| Reasoning拡張 | `reasoning.effort`, `parallel` | `reasoning: true/level` 相当（要マッピング） |
| 推奨Fast | `gpt-5-main(-mini)` | `gemini-2.5-flash` |
| 推奨Thinking | `gpt-5-thinking(-mini/-nano/-pro)` | `gemini-2.5-pro`（思考は限定的） |
| トークン上限 | family依存 | family依存 |
| 料金表記 | `priceIn/priceOut`（任意） | 同左 |

※ 実際のパラメタ名の差は `providers/*_client.py` で吸収する。

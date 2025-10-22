# 付録F: Provider互換表（初期）
**Status: 2025-10-19 JST**

| レジストリキー | GPT-5系（OpenAI） | Gemini 2.5系（Google） |
|---|---|---|
| `id` | `gpt-5-main`, `gpt-5-main-mini`, `gpt-5-thinking`, `gpt-5-thinking-mini`, `gpt-5-thinking-nano`, `gpt-5-thinking-pro` | `gemini-2.5-pro`, `gemini-2.5-flash` |
| `provider` | `openai` | `google` |
| `family` | `gpt-5` | `gemini-2.5` |
| `type` | `fast`, `fast-mini`, `thinking`, `thinking-mini`, `thinking-nano`, `thinking-pro` | `general`, `fast` |
| `reasoning` | `false`（fast系）, `true`（thinking系） | `false` |
| `parallel` | `true`（`gpt-5-thinking`, `gpt-5-thinking-pro`）, `false`（上記以外） | `false` |

※ 実際のパラメタ名の差は `providers/*_client.py` で吸収する。
※ 料金関連フィールドは将来追加予定のため、現在のレジストリには含まれていません。

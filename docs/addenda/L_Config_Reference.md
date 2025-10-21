# 付録L: 設定リファレンス
**Status: 2025-10-19 JST**

- `OPENAI_API_KEY`, `GOOGLE_GEMINI_API_KEY`（旧称 `GEMINI_API_KEY` 互換）, `DEFAULT_PROVIDER`（将来のマルチプロバイダー切り替え用プレースホルダー／現状未使用）, `DEFAULT_MODEL`（起動時の既定モデル ID）
- `CHAINLIT_AUTH_SECRET`
- `PORT`
- Chainlit の詳細ログが必要な場合は `.env` に一時的に `DEBUG=1` を追加するか、CLI 実行時に `chainlit run src/app.py --debug` を付与する
- `model_registry.json`：`id` / `provider` / `family` / `type` / `reasoning` / `parallel`
  - ※ `reasoning`/`parallel` は将来対応予定の予約フィールド（現状は読み飛ばし）
  - ※ 今後追加予定のフィールドは未実装のため本リファレンスでは列挙していません（予約フィールド扱い）

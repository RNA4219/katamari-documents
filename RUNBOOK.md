# RUNBOOK

## 準備
1. `requirements.txt` をインストールし、`OPENAI_API_KEY`・`GEMINI_API_KEY` を環境変数に設定する。初回起動は `chainlit run src/app.py --host 0.0.0.0 --port 8787` を利用する。
2. リバースプロキシで HTTP/2・Keep-Alive・SSE バッファを調整し、フェイルオーバーを用意する。
3. 認証段階に応じて Header Auth / OAuth を切り替え、必要な Redirect URI と Secrets をレビューする。

## 実行
1. SSE が切断した場合はプロキシのバッファとタイムアウトを確認し、HTTP/2 設定を再読み込みする。
2. 初回トークン遅延が閾値超過なら近接リージョンの mini モデルへ切り替え、温度・Keep-Alive を再調整する。
3. OAuth エラーは Redirect URL・クレデンシャルを再確認し、Header Auth へフォールバックしてユーザ影響を最小化する。
4. Trim 成果が低下したら `target_tokens` と Trim プロンプトを調整し、Semantic 戦略を再適用する。

## 確認
1. Persona 変更、Reflect 3段表示、Trim 比率を UI で再確認し、設定が即時反映されることを確かめる。
2. 初回トークン p95、UI 反映遅延、SSE 連続稼働の性能指標がしきい値内であることを計測する。
3. Release/Security Checklist を再実施し、Secrets、CORS、Rate Limit が最新構成と一致していることを確認する。

# RUNBOOK

## 準備
1. 開発環境で `requirements.txt` をインストールし、`OPENAI_API_KEY` と `GEMINI_API_KEY` をサーバ環境変数に設定する。初期起動は `chainlit run src/app.py -h --host 0.0.0.0 --port 8787` を想定する。[付録H: デプロイガイド](docs/addenda/H_Deploy_Guide.md)。
2. リバースプロキシでは HTTP/2・Keep-Alive と SSE バッファ設定を確認し、障害時切替が可能な構成にする。[付録J: 障害時復旧（Runbook）](docs/addenda/J_Runbook.md)。
3. 認証設定を段階に合わせて選択する（M1: Header Auth、M1.5: OAuth）。必要な Redirect URI を Secrets と併せてレビューする。[Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)。

## 実行
1. SSE が途切れた場合はリバースプロキシのバッファ・Flush・Timeout を即時確認し、必要なら HTTP/2 設定を再読み込みする。[付録J: 障害時復旧（Runbook）](docs/addenda/J_Runbook.md)。
2. 初回トークン遅延が閾値を超えるときは近接リージョンの mini モデルへ切り替え、温度と Keep-Alive を再調整する。[付録J: 障害時復旧（Runbook）](docs/addenda/J_Runbook.md)。
3. OAuth エラーは Redirect URL・クレデンシャルを再確認し、Header Auth へのフォールバックでユーザ影響を軽減する。[付録J: 障害時復旧（Runbook）](docs/addenda/J_Runbook.md)。
4. Trim 保持率が低下したら `target_tokens` と Trim 戦略（Semantic 方式）を見直し、要約プロンプトを調整する。[付録J: 障害時復旧（Runbook）](docs/addenda/J_Runbook.md)。

## 確認
1. SSE と OAuth を含む主要ユースケースについて、設定即時反映・Reflect 3段表示・Trim 比率の変動を UI で再確認する。[付録I: テストケース集](docs/addenda/I_Test_Cases.md)。
2. 性能指標（p95 初回トークン ≤ 1.0s、SSE 連続 1 分で切断率 < 1%）を再計測し、しきい値を維持していることを確認する。[Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)。
3. リリース/セキュリティ チェックリストの該当項目を再実施し、Secrets、CORS、Rate Limit を最新構成と照合する。[Release Checklist](docs/Release_Checklist.md)、[Security Review Checklist](docs/Security_Review_Checklist.md)。

# BLUEPRINT

## 目的
- Chainlit フォーク基盤上で Persona/Trim/Reflect チェーンを一貫運用できるアシスタントを構築し、前処理・多段推論・評価を統合する。
- Katamari 要件定義・技術仕様で示された SSE 可視化と即時設定反映をプロダクション品質で提供する。

## 背景
- プロジェクトは Chainlit 安定版をフォークし、差分は `core_ext/` と Provider 抽象層に隔離する方針で進行している。
- 提供モデルは GPT-5 系と Gemini 2.5 系をプラガブルに扱い、Reasoning 拡張と推奨ファミリ比較を内部で吸収する。
- ロードマップでは M1 で Header Auth、M1.5 で OAuth、M2 以降で評価 API の段階導入を想定している。

## 主要制約
- パフォーマンス: 初回トークン p95 ≤ 1.0s、UI 反映遅延 ≤ 300ms、SSE 連続 1 分で切断率 < 1%。
- セキュリティ: Secrets は環境変数管理、ログの PII マスク、CORS/Rate Limit 強制、HTTPS/HTTP2 運用。
- アーキテクチャ: Apache-2.0 ライセンス順守、`app.py` は薄い配線、主要処理を `core_ext/` と Provider SPI に閉じ込める。

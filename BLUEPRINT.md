# BLUEPRINT

## 目的
- Chainlit フォーク基盤上で、前処理・多段推論・評価機構を備えたリッチUIアシスタントを最短で構築し、Persona/Trim/Reflect チェーンを統合運用できる状態を作る。関連仕様: [Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)、[機能仕様 v1](docs/Katamari_Functional_Spec_v1_ja.md)。

## 背景
- プロジェクトは Chainlit 最新安定版をフォークして拡張差分を `core_ext/` と Provider 抽象層に隔離する方針で進行する。ステップごとの SSE 表示、トークン削減、Persona YAML の即時適用を重視し、M2 以降で評価・進化 API を段階投入する計画である。[Katamari 技術仕様 v1](docs/Katamari_Technical_Spec_v1_ja.md)、[ロードマップ & 仕様ハブ](docs/ROADMAP_AND_SPECS.md)。
- 提供モデルは GPT-5 系と Gemini 2.5 系をプラガブルに扱い、Reasoning 拡張や推奨ファミリを比較しつつ Provider 差異を内部で吸収する。[付録F: Provider互換表](docs/addenda/F_Provider_Matrix.md)。

## 制約
- 非機能要件として SSE 初期トークン p95 ≤ 1.0s、UI 反映遅延 ≤ 300ms、ストリーミング 1 分継続時の切断率 < 1% を維持する。M1 で Header Auth、M1.5 で OAuth を必須化し、`/metrics`・`/healthz` を提供する。[Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)。
- セキュリティは API キーをサーバ環境変数に限定し、ログの PII マスク、CORS 制限、HTTPS/HTTP2、Rate Limit を徹底する。認証段階に応じた運用とし、保持データは最小限に抑制する。[付録G: セキュリティ & プライバシー指針](docs/addenda/G_Security_Privacy.md)。
- アーキテクチャは Fork 先ライセンス（Apache-2.0）遵守と差分最小化を前提に、`app.py` は薄い配線、主要処理は `core_ext/` と Provider SPI に封じ込める。性能指標や評価器導入計画も段階リリースと整合させる。[Katamari 技術仕様 v1](docs/Katamari_Technical_Spec_v1_ja.md)。

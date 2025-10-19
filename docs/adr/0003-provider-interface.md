# ADR-0003: LLM プロバイダ抽象インターフェースを定義する

## Status
- 承認済み（2025-02-14）

## Context
- Katamari は OpenAI と Google Gemini など複数の LLM API を切り替えながら利用する。
- `src/providers/` では現在もクライアント別実装が存在するが、Chainlit 本体の API 差異を吸収する薄い適配層が不足している。
- ストリーミングと一括応答の双方をサポートしつつ、再試行やタイムアウト戦略を共通化したい。

## Decision
- `providers` レイヤに `stream(model, messages, **opts)` と `complete(model, messages, **opts)` を持つ非同期インターフェースを定義し、各プロバイダがこれを実装する。
- エラーハンドリングと再試行可能判定は抽象クラス（例: `BaseLLMProvider`）で共通実装し、外部 SDK の例外を Katamari の `RetryableProviderError` / `FatalProviderError` に正規化する。
- モデル設定は `config/model_registry.json` で一元管理し、プロバイダ実装は registry を参照して API 呼び出しパラメータを決定する。

## Consequences
- UI/Chainlit ハンドラ側はプロバイダ差異を意識せずメソッド呼び出しのみで済む。
- 新規プロバイダ追加時は SDK ラッパーと例外マッピングを実装するだけでよく、回帰リスクが低下する。
- 共通抽象に適合しない特殊機能（例: reasoning 拡張パラメータ）は `**opts` で受けつつ、インターフェース膨張に注意する必要がある。

## Definition of Done (DoD)
- `BaseLLMProvider`（仮称）を定義し、OpenAI/Gemini 実装が継承している。
- プロバイダ共通のエラーハンドリング仕様が tests で担保されている。
- model registry からの動的設定読取が providers 層で実装され、ドキュメントに反映されている。

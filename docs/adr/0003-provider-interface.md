# ADR-0003: LLM プロバイダ抽象インターフェースを定義する

## Context
- 背景: Katamari は OpenAI と Google Gemini など複数の LLM API を切り替えながら利用する。
- 課題: `src/providers/` ではクライアント別実装が存在するが、Chainlit 本体の API 差異を吸収する薄い適配層が不足している。
- 参考: `addenda/F_Provider_Matrix.md` にプロバイダ比較、既存実装の例外ポリシーは `src/providers/*` に記載。

## Decision
- 方針: `providers` レイヤに `stream(model, messages, **opts)` と `complete(model, messages, **opts)` を持つ非同期インターフェースを定義し、各プロバイダがこれを実装する。
- 決定理由: 共通抽象を設けることで、UI/Chainlit ハンドラがプロバイダ差異を意識せずに済み、新規プロバイダ追加時の改修範囲を局所化できる。
- 運用: エラーハンドリングと再試行可能判定は抽象クラス（例: `BaseLLMProvider`）で共通実装し、外部 SDK の例外を Katamari の `RetryableProviderError` / `FatalProviderError` に正規化する。モデル設定は `config/model_registry.json` で一元管理する。

## Consequences
- 影響範囲: UI/Chainlit ハンドラ側はプロバイダ差異を意識せずメソッド呼び出しのみで済む。
- 利点: 新規プロバイダ追加時は SDK ラッパーと例外マッピングを実装するだけでよく、回帰リスクが低下する。
- リスク/フォローアップ: 共通抽象に適合しない特殊機能（例: reasoning 拡張パラメータ）は `**opts` で受けるが、インターフェース膨張に注意する必要がある。互換性を維持できない機能は拡張ポイントを `TypedDict` などで明示してから導入する。

## Status
- ステータス: 承認済み
- 最終更新日: 2025-02-14

## DoD
- `BaseLLMProvider`（仮称）を定義し、OpenAI/Gemini 実装が継承している。
- プロバイダ共通のエラーハンドリング仕様がテストで担保されている。
- model registry からの動的設定読取が providers 層で実装され、ドキュメントに反映されている。
- SDK 例外を Katamari の例外階層へ変換する際のルールが `CONTRIBUTING.md` と本 ADR の双方に記述されている。

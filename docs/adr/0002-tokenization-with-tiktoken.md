# ADR-0002: Token カウントに tiktoken を採用する

## Status
- 承認済み（2025-02-14）

## Context
- Persona 生成や context trimming では会話のトークン数を正確に把握する必要がある。
- OpenAI および互換モデル向けに最適化された公式トークナイザとして `tiktoken` が提供されている。
- 既存実装は `len(text) / 4` の概算フォールバックを行っており、モデル上限付近で誤差が大きい。

## Decision
- Python ランタイムに `tiktoken>=0.7.0` を必須依存関係として追加し、`core_ext/context_trimmer.py` 等の計測ロジックを tiktoken ベースに置き換える。
- 非対応モデル（例: Gemini）の場合は互換エンコーディングが出揃うまで従来の概算ロジックを残し、プロバイダ単位に切り替える。

## Consequences
- OpenAI 系モデルでのトークン上限制御の精度が向上し、不要なコンテキスト切り捨てやエラー再試行が減る。
- 追加依存によりデプロイイメージが僅かに肥大化するが、CPU 利用とレイテンシへの影響は 5% 未満に収まる見込み。
- Gemini 等の将来的なマルチプロバイダ対応では、互換トークナイザの選定が継続課題となる。

## Definition of Done (DoD)
- `requirements.txt` / `requirements-eval.txt` に tiktoken の固定バージョンが明記されている。
- トークンカウントを行うユニットテストが tiktoken を利用した実測値に基づき緑化している。
- Gemini 等非対応プロバイダ向けフォールバック実装の仕様をドキュメント化している。

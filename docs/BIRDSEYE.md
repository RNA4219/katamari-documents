# Birdseye フォールバックガイド

Guardrails から Birdseye 系ドキュメントへ遷移する際のフォールバック先です。Birdseye の全体像を素早く把握し、依存関係と検証手順を確認するための導線をまとめます。

## 確認ポイント: `edges`
- `docs/birdseye/index.json` の `edges` セクションで依存関係の有無と整合性を確認します。
- Guardrails から到達した場合は、対象ノードが Hot リストに含まれているかを併せてチェックしてください。

## JSON 資料の参照手順
1. `docs/birdseye/index.json`
   - `nodes` と `edges` を順に確認し、対象モジュールの `caps` パスを特定します。
2. `docs/birdseye/caps/`
   - `caps/` 配下の該当 Capsule ファイルを開き、`summary`、`deps_out`/`deps_in`、`tests` を確認します。
3. `docs/birdseye/hot.json`
   - 優先監視対象 (`entries`) を確認し、対象モジュールが持つ最新の更新理由 (`reason`) を把握します。

## 関連ドキュメント
- 詳細な更新プロセスは [`docs/birdseye/README.md`](birdseye/README.md) を参照してください。

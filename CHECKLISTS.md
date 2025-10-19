# CHECKLISTS

## レビュー
- 差分がロードマップの優先タスクと整合し、`core_ext/`・Provider SPI の責務境界を維持しているか確認する。
- Persona/Trim/Reflect の主要フローに対応したテスト（`tests/`、付録テストケース）を更新しているか確認する。
- Secrets、CORS、Rate Limit、ログマスクなどのセキュリティ方針が守られているか確認する。

## リリース
- Release Checklist に従い、バージョンタグ、ドキュメント更新、ruff/mypy(strict)/pytest/node:test の CI 完走、Docker ビルドを確認する。
- Security Review Checklist に沿って OAuth Redirect、Secrets、依存ライブラリのスキャン結果をレビューする。
- バージョニング規約（`vX.Y.Z-katamari`）とリリースノートの整合性を確認する。

# CHECKLISTS

## レビュー確認
- PR 作成時は `docs/ROADMAP_AND_SPECS.md` 記載の優先タスクと差分を照合し、仕様逸脱がないか確認する。[ロードマップ & 仕様ハブ](docs/ROADMAP_AND_SPECS.md)。
- コード差分は `core_ext/`・`providers/` の責務境界を守り、Chainlit 本体との差分を最小化しているかをレビューする。[Katamari 技術仕様 v1](docs/Katamari_Technical_Spec_v1_ja.md)。
- Persona/Trim/Reflect の主要フローに対し、`tests/` と付録のテストケースに基づく自動テストを追加・更新しているかを確認する。[付録I: テストケース集](docs/addenda/I_Test_Cases.md)。
- セキュリティ方針（ENV のみの Secrets、CORS、Rate Limit、ログマスク）が守られているかをチェックする。[付録G: セキュリティ & プライバシー指針](docs/addenda/G_Security_Privacy.md)。

## リリース確認
- `Release Checklist` に沿ってバージョンタグ、ドキュメント更新、テスト・Lint 完走、Docker ビルドを完了しているか確認する。[Release Checklist](docs/Release_Checklist.md)。
- セキュリティ審査として OAuth Redirect、Secrets、依存ライブラリのスキャン結果をレビューする。[Security Review Checklist](docs/Security_Review_Checklist.md)。
- バージョニング規約（`MAJOR.MINOR.PATCH` / `vX.Y.Z-katamari`）とリリースノートの内容が最新仕様と整合しているかチェックする。[付録M: バージョニング & リリース](docs/addenda/M_Versioning_Release.md)。
- CI ワークフローで lint（ruff）、型検査（mypy/strict）、pytest、node:test が成功し、必要に応じて Provider Secrets を条件付きで適用しているか確認する。[ロードマップ & 仕様ハブ](docs/ROADMAP_AND_SPECS.md)。

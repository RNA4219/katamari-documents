
# Release Checklist

> NOTICE 追記済み: リポジトリ直下の [`NOTICE`](../NOTICE) を参照し、Chainlit 由来告知と改変概要を維持すること。
- [ ] Bump version & tag
- [ ] 受入基準（`EVALUATION.md` 等）の証跡を取得し、PR/Issue に添付
- [ ] 影響範囲（依存モジュール、運用手順、インフラ）を再確認し、必要な同期ドキュメントを更新
- [ ] PR に `type:*` と `semver:*` ラベルを設定
- [ ] `CHANGELOG.md` を最新化
- [ ] Update docs/UPSTREAM.md
- [ ] Run tests & lint
- [ ] Build Docker image
- [ ] Verify SSE streaming & OAuth (if enabled)
- [ ] 配布パッケージ・Docker イメージ・アーカイブに [`LICENSE`](../LICENSE) と [`NOTICE`](../NOTICE) を同梱したことを確認
- [ ] リリース PR 説明欄に `LICENSE`/`NOTICE` 同梱状況を明記（配布要件を満たした旨の記録）

## 配布物のライセンス同梱チェック

- [ ] 配布パッケージ・Docker イメージ・アーカイブに [`LICENSE`](../LICENSE) と [`NOTICE`](../NOTICE) を同梱したことを確認

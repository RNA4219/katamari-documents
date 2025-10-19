# Release Checklist

> `LICENSE` と [`NOTICE`](../NOTICE) の同梱は Apache-2.0 の配布要件です。Chainlit 由来の告知・改変概要は `NOTICE` を最新化して維持してください。
- [ ] Bump version & tag
- [ ] 受入基準（`EVALUATION.md` 等）の証跡を取得し、PR/Issue に添付
- [ ] 影響範囲（依存モジュール、運用手順、インフラ）を再確認し、必要な同期ドキュメントを更新
- [ ] PR に `type:*` と `semver:*` ラベルを設定
- [ ] `CHANGELOG.md` を最新化
- [ ] `NOTICE` の派生元告知・著作権表記・改変要約が最新であることを確認し、更新した場合は差分を Release PR で説明
- [ ] Update docs/UPSTREAM.md
- [ ] Run tests & lint
- [ ] Build Docker image
- [ ] Verify SSE streaming & OAuth (if enabled)
- [ ] 配布パッケージ・Docker イメージ・アーカイブに [`LICENSE`](../LICENSE) と [`NOTICE`](../NOTICE) を同梱したことを確認
- [ ] リリース PR 説明欄に `LICENSE`/`NOTICE` 同梱状況を明記（配布要件を満たした旨の記録）

## 配布物のライセンス同梱チェック

- [ ] 配布パッケージ・Docker イメージ・アーカイブに [`LICENSE`](../LICENSE) と [`NOTICE`](../NOTICE) を同梱したことを確認
- [ ] リリースノートおよび Release PR で同梱確認の結果と証跡リンクを共有

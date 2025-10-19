# Release Checklist

> `LICENSE` と [`NOTICE`](../NOTICE) の同梱は Apache-2.0 の配布要件です。Chainlit 由来の告知・改変概要は `NOTICE` を最新化して維持してください。

## 手順（準備 → 検証 → リリース）

### 準備

- [ ] 影響範囲（依存モジュール、運用手順、インフラ）を再確認し、`RUNBOOK.md`・`CHECKLISTS.md`・`docs/UPSTREAM.md` など同期ドキュメントを必要に応じて更新
- [ ] `CHANGELOG.md` と [`NOTICE`](../NOTICE) / [`LICENSE`](../LICENSE) の改変概要を最新化し、[README.md#変更履歴の更新ルール](../README.md#%E5%A4%89%E6%9B%B4%E5%B1%A5%E6%AD%B4%E3%81%AE%E6%9B%B4%E6%96%B0%E3%83%AB%E3%83%BC%E3%83%AB) に従って記録
- [ ] PR に `type:*` と `semver:*` ラベルを設定し、リリース対象 Issue / Task Seed (`TASK.*.md`) を紐付け
- [ ] リリースノート下書きに配布物一覧・既知の制約・ロールアウト計画を追記

### 検証

- [ ] 受入基準（`EVALUATION.md` 等）の証跡を取得し、PR / Issue に添付（例: `make test` 実行ログ、評価ノート）
- [ ] `make lint` と `make test` を実行し、ローカル検証ログを保存
- [ ] `docker build -t <image>:<tag> .` で Docker イメージをビルドし、生成物を受入環境で起動確認
- [ ] SSE ストリーミングと OAuth（有効化時）を [`RUNBOOK.md`](../RUNBOOK.md) の手順に沿って手動検証
- [ ] GitHub Actions の CI 結果（`Actions > workflows > CI`）が成功していることを確認し、失敗時は原因と対処を記録

### リリース

- [ ] バージョン番号を更新し、`git commit` → `git tag v<X.Y.Z>` → `git push --follow-tags` を実施
- [ ] 配布パッケージ・Docker イメージ・アーカイブに [`LICENSE`](../LICENSE) と [`NOTICE`](../NOTICE) を同梱
- [ ] リリース PR の説明欄に同梱確認結果・CI 実行リンク・受入証跡を明記
- [ ] GitHub Release / ChangeLog / RUNBOOK の公開内容が同期していることを最終確認

## 配布物のライセンス同梱チェック

- [ ] 配布パッケージ・Docker イメージ・アーカイブに [`LICENSE`](../LICENSE) と [`NOTICE`](../NOTICE) を同梱したことを確認
- [ ] リリースノートで同梱確認の結果と証跡リンクを共有

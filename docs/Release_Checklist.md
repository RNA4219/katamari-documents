# Release Checklist

> NOTICE 追記済み: リポジトリ直下の [`NOTICE`](../NOTICE) を参照し、Chainlit 由来告知と改変概要を維持すること。

## 準備（個人運用での段取り）

- [ ] 作業ブランチを最新化: `git status --short` で未コミット差分を確認し、`git fetch origin && git rebase origin/main` で同期。
- [ ] リリース対象の影響範囲を再確認し、`docs/` や `RUNBOOK.md` / `CHECKLISTS.md` / `EVALUATION.md` 等に必要な更新があれば先に反映する。
- [ ] バージョン方針を決定し、`CHANGELOG.md` と [`NOTICE`](../NOTICE) を更新して配布物の改変点と同梱要件を明記する。
- [ ] リリース PR/Issue に受入基準の証跡（`EVALUATION.md` に対応するログ・スクリーンショット等）を添付する計画を立てる。
- [ ] PR に `type:*` と `semver:*` ラベルを設定し、関連 Issue / タスクをリンクする。

## 検証（エビデンス取得）

- [ ] 受入基準を満たす検証を実行し、ログを保存する。
  - Python: `pip install -r requirements.txt` → `make lint` → `make test`（内部では `pytest -q` を実行）。
  - Node/Front: `npm install` → `npm test` が必要な場合に実施。
- [ ] CI 結果を確認し、すべて成功していることを `https://github.com/<owner>/<repo>/actions` で確認（リンクを PR コメントに添付）。
- [ ] Docker イメージをビルドして最小起動確認: `docker build -t <repo>:<version> .` → `docker run --rm -p 8787:8787 <repo>:<version>`。
- [ ] SSE ストリーミングと OAuth（有効化している場合）の動作を、`RUNBOOK.md` の手順で手元確認し、結果を記録する。
- [ ] 配布パッケージ・Docker イメージ・アーカイブへ [`LICENSE`](../LICENSE) と [`NOTICE`](../NOTICE) を同梱した証跡を取得する（ファイルリストや `docker run` での確認ログ）。

## リリース（公開・配布）

- [ ] 受入基準（`EVALUATION.md` 等）の証跡と影響範囲確認結果を PR 説明欄に貼付し、Guardrails の必須項目を満たしたことを明記する。
- [ ] `git tag -s v<version>` → `git push origin v<version>` で署名タグを作成・送信し、GitHub Release のドラフトを作成する。
- [ ] リリース PR 説明欄に `LICENSE`/`NOTICE` 同梱状況を明記し、必要なら配布成果物（Wheel, Docker, アーカイブ）のダウンロードリンクを追記する。
- [ ] `docs/UPSTREAM.md` を更新し、Fork と Upstream の差分取り込み手順が最新であることを確認する。
- [ ] リリース完了後、`RUNBOOK.md` / `CHECKLISTS.md` / `TASK.*.md` に反映したログ・リンクを追記し、次回に備えて記録を整理する。

## 配布物のライセンス同梱チェック

- [ ] 配布パッケージ・Docker イメージ・アーカイブに [`LICENSE`](../LICENSE) と [`NOTICE`](../NOTICE) を同梱したことを確認
- [ ] リリースノートで同梱確認の結果と証跡リンクを共有

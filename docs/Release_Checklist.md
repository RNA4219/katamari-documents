
# Release Checklist

Day8 Guardrails の Release フロー（準備→検証→リリース）に沿った個人運用用チェックリスト。`RUNBOOK.md` / `EVALUATION.md` / `CHECKLISTS.md` と併用し、証跡・通知・配布物の整合を確保する。

## 準備

- [ ] バージョン計画を決定し、`CHANGELOG.md`・[`NOTICE`](../NOTICE) の更新方針を整理（手順: [`README.md#変更履歴の更新ルール`](../README.md#%E5%A4%89%E6%9B%B4%E5%B1%A5%E6%AD%B4%E3%81%AE%E6%9B%B4%E6%96%B0%E3%83%AB%E3%83%BC%E3%83%AB)）。
- [ ] 影響範囲を洗い出し、依存モジュール・運用手順・インフラの同期対象を特定（参照: [`RUNBOOK.md`](../RUNBOOK.md), [`docs/UPSTREAM.md`](UPSTREAM.md)）。
- [ ] ラベル・リリースノート草案を準備し、PR に `type:*` と `semver:*` ラベルを設定。
- [ ] ローカルブランチを同期: `git fetch origin && git rebase origin/main`。

## 検証

- [ ] 受入基準証跡を取得し、`EVALUATION.md` 記載のメトリクス結果を PR/Issue に添付。必要コマンド: `make test`, `pytest -q`, `ruff check`, `mypy --strict src`。
- [ ] Lint / 型 / テスト / ビルドをローカル実行し、出力ログを保存。Docker ビルド確認: `docker build -t katamari:release .`。
- [ ] SSE ストリーミングと OAuth（有効化時）を `RUNBOOK.md#検証` 手順に沿って確認。
- [ ] GitHub Actions など CI の最新結果を確認し、全ジョブが成功していることを記録。
- [ ] 影響範囲で特定したドキュメント（`docs/`, `RUNBOOK.md`, `CHECKLISTS.md` 等）を更新済みか再確認。

## リリース

- [ ] `CHANGELOG.md` と [`NOTICE`](../NOTICE) を更新し、差分をレビュー。必要に応じて `docs/UPSTREAM.md` を同期。
- [ ] バージョン番号を更新し、タグ作成: `git tag -a vX.Y.Z -m "Release vX.Y.Z"` → `git push origin vX.Y.Z`。
- [ ] 配布パッケージ・Docker イメージ・アーカイブに [`LICENSE`](../LICENSE) と [`NOTICE`](../NOTICE) を同梱したことを確認。
- [ ] リリースノートを公開し、影響範囲の関係者へ告知（Slack/Issue/メール等）。
- [ ] リリース後モニタリング計画を確認し、`RUNBOOK.md#運用` に沿って初回チェックを予約。

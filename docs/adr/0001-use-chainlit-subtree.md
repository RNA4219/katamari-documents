# ADR-0001: Chainlit リポジトリを git subtree として取り込む

## Status
- 承認済み（2025-02-14）

## Context
- Katamari は Chainlit/chainlit をベースに多数の独自拡張を加えている。
- `upstream/chainlit/` 配下に公式ソースを同期し、`core_ext/` や `providers/` で差分実装を維持している。
- フォーク保守時に upstream 追従と独自差分の衝突を最小化したい。

## Decision
- `upstream/chainlit/` を `git subtree add --prefix upstream/chainlit https://github.com/Chainlit/chainlit main` で初期化し、以後も `git subtree pull` で同期する。
- Katamari 側の恒久的変更は `core_ext/`・`providers/`・`themes/` など専用ディレクトリに配置し、`upstream/chainlit/` 直下には直接コミットしない。
- upstream に取り込みたい修正は GitHub PR 経由で本家に貢献し、取り込まれたら次回 subtree pull で反映する。

## Consequences
- 差分管理が `git subtree` ログで可視化され、週次同期フロー（`docs/UPSTREAM.md`）と整合する。
- 独自改修が専用ディレクトリに集約され、upstream 更新時のマージ衝突が減る。
- subtree 更新は履歴が膨らむため、タグ単位での取り込みと squash merge 禁止を徹底する必要がある。

## Definition of Done (DoD)
- `upstream/chainlit/` を subtree として初期化済みであることを確認。
- フォーク運用手順（`docs/UPSTREAM.md`, `docs/FORK_NOTES.md`）が本 ADR と矛盾しないことを確認。
- subtree pull 手順を自動化するスクリプトまたはドキュメントが整備されている。

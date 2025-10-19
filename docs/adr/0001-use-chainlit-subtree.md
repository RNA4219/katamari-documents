# ADR-0001: Chainlit リポジトリを git subtree として取り込む

## Context
- 背景: Katamari は Chainlit/chainlit をベースに多数の独自拡張を加えている。
- 制約: upstream 追従と独自差分の衝突を最小化しつつ、公式リポジトリへの貢献も継続したい。
- 参考: `docs/UPSTREAM.md`, `docs/FORK_NOTES.md` にフォーク運用手順を記載。

## Decision
- 方針: `git subtree add --prefix upstream/chainlit https://github.com/Chainlit/chainlit main` で取り込み、以後も `git subtree pull` で同期する。
- 決定理由: subtree は履歴と差分を保ったまま上流の更新を取り込めるため、独自改修と upstream の両立が容易になる。
- 運用: Katamari 側の恒久的変更は `core_ext/`, `providers/`, `themes/` など専用ディレクトリに配置し、`upstream/chainlit/` 直下には直接コミットしない。upstream に還元したい修正は本家 PR を経由する。

## Consequences
- 影響範囲: 差分管理が `git subtree` ログで可視化され、週次同期フロー（`docs/UPSTREAM.md`）と整合する。
- 利点: 独自改修が専用ディレクトリに集約され、upstream 更新時のマージ衝突が減る。
- リスク/フォローアップ: subtree 更新は履歴が膨らむため、タグ単位での取り込みと squash merge 禁止を徹底する必要がある。

## Status
- 承認済み（2025-02-14）

## Definition of Done (DoD)
- `upstream/chainlit/` を subtree として初期化済みであること。
- フォーク運用手順（`docs/UPSTREAM.md`, `docs/FORK_NOTES.md`）が本 ADR と整合していること。
- subtree pull 手順を自動化するスクリプトまたはドキュメントが整備されていること。

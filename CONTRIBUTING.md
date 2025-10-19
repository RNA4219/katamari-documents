
# Contributing to Katamari
- Fork, create feature branch, open PR with tests.
- Keep diffs in `core_ext/` and `providers/` when possible.
- Follow the issue templates.
- ADR を更新する場合は以下を遵守してください。
  - 新規 ADR は `docs/adr/0000-template.md` をコピーし、連番と日付を付与する。
  - 既存 ADR のステータス変更時は `docs/adr/README.md` の目次も同時に更新する。
  - PR には ADR の背景・結論・影響範囲をサマリとして含め、レビュアが経緯を追跡できるようにする。

## ADR / 要件整合フロー
- マイルストーン着手前に該当 ADR（`docs/adr/`）の目的・スコープ・DoD を確認し、差分がある場合は PR で更新する。
- 仕様変更時は Katamari Requirements（FR/AC）、WBS（`docs/katamari_wbs.csv`）、関連 addenda を同一 PR で整合させる。
- ADR を新規追加・更新した場合は、PR 説明に対象マイルストーンと影響する FR/AC 番号を明記する。

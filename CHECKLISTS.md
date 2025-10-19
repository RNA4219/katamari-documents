# CHECKLISTS

## 目的
- Katamari 開発・リリース・運用で必要な確認項目を集約し、Guardrails とロードマップ要件を満たす状態を可視化する。

## スコープ
### In Scope
- 開発（Dev）、レビュー（PR）、リリース（Release）、運用（Ops）フェーズのチェック項目。
- Task Seed と連動する未完了項目の追跡。
- Guardrails で求められる最小差分・自己検証手順の記録。[GUARDRAILS](third_party/Day8/workflow-cookbook/GUARDRAILS.md)。

### Out of Scope
- 組織全体のコンプライアンスチェック（別管理）。
- プロダクトマーケティング/営業資料のレビュー。

## 手順
1. フェーズ開始時に該当セクションのチェックリストをコピーし、Issue/PR/Task に貼り付ける。
2. 項目を実施するたびに証跡（ログ、CI 結果、スクリーンショット）を残す。
3. 未完了項目がある場合は Task Seed を更新し、リリース可否を `EVALUATION.md` に連携する。

## Acceptance Criteria
- 各フェーズの必須項目が `PASS` になっているか、例外（`N/A`）理由が明記されている。
- 例外がある場合、フォローアップ Task Seed が登録されている。
- チェック結果が `docs/ROADMAP_AND_SPECS.md` に記載されたフェーズ進行条件を満たす。

## チェック項目
### Development
- [ ] テストを先に追加し、`pytest` / `node:test` が成功した。
- [ ] `mypy --strict` と `ruff` を通過（もしくは skip 理由を記録）。
- [ ] 公開 API 変更がない、または段階移行フラグを設定済み。
- [ ] Birdseye index/caps を更新し、該当ノードの要約が最新。

### Pull Request / Review
- [ ] 変更理由と影響範囲を `docs/ROADMAP_AND_SPECS.md` の該当項目にリンク。
- [ ] Task Seed を更新し、レビュー観点を共有。
- [ ] Guardrails の最小読込手順をレビュアーが実行できるよう案内。

### Release
- [ ] `docs/Release_Checklist.md` の全項目が `PASS`。
- [ ] `CHANGELOG.md` にリリース内容を記録し、タグ発行準備ができている。
- [ ] GHCR へのビルド/公開手順が `RUNBOOK.md` と一致。

### Ops / Incident
- [ ] 障害時の対応ログが `RUNBOOK.md` に沿って記録されている。
- [ ] 再発防止策が Task Seed または Issue で管理されている。
- [ ] セキュリティインシデントは `docs/Security_Review_Checklist.md` に追記済み。

## 参照リンク
- [docs/ROADMAP_AND_SPECS.md](docs/ROADMAP_AND_SPECS.md)
- [docs/Release_Checklist.md](docs/Release_Checklist.md)
- [docs/Security_Review_Checklist.md](docs/Security_Review_Checklist.md)
- [third_party/Day8/workflow-cookbook/GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)

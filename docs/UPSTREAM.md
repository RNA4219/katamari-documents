# UPSTREAM 取り込み方針（Katamari）
- Upstream: Chainlit/chainlit（Apache-2.0）
- 追従ポリシー: 最新安定タグを週次でチェックし取り込み
- 直近開始日時: 2025-10-19 JST
- 差分は `core_ext/` に隔離、`app.py` は薄い配線のみ。

## Git subtree 運用手順

### 初回導入（`git subtree add`）
1. upstream remote を登録
   ```bash
   git remote add chainlit https://github.com/Chainlit/chainlit.git
   git fetch chainlit --tags
   ```
2. 取り込み対象タグを確認（例: `v1.2.3`）
   ```bash
   git tag -l 'v*' --sort=-v:refname | head
   ```
3. `core_ext/chainlit` にサブツリーを追加
   ```bash
   git subtree add --prefix=core_ext/chainlit chainlit v1.2.3 --squash
   ```
4. 競合が発生した場合は一旦 `git status` で対象ファイルを洗い出し、`core_ext/` 側を優先しつつ最小修正で整合。

### 更新取り込み（`git subtree pull`）
1. 最新タグを取得
   ```bash
   git fetch chainlit --tags
   ```
2. 取り込み対象タグを選定し pull
   ```bash
   git subtree pull --prefix=core_ext/chainlit chainlit v1.2.4 --squash
   ```
3. 競合発生時は以下の手順で解消
   ```bash
   git mergetool  # or 手動編集
   git add <conflicted-files>
   git commit --amend --no-edit
   ```
   - `core_ext/` 外へ波及しない差分に抑制
   - 必要に応じて upstream 側修正内容をコメントで明示

## 週次チェック運用フロー

- **担当**: Platform チーム当番（輪番制、週替わり）
- **スケジュール**: 毎週火曜 10:00 JST にタグ確認、同日 17:00 JST までに差分検証を完了
- **検証観点**:
  - Chainlit release note に記載された breaking change の有無
  - `requirements.txt` 相当の依存更新内容
  - UI/API への影響（`core_ext/` 変更の有無、`app.py` への伝播）

### 差分検証チェックリスト
- [ ] 取り込み対象タグとコミット SHA を記録（Notion Runbook）
- [ ] `git diff v1.2.3..v1.2.4 -- core_ext/chainlit` で差分を確認
- [ ] `poetry install` / `npm install` 等依存解決の再現性確認
- [ ] `pytest` / `npm test` のスモーク実行結果を添付
- [ ] UI 変更時はスクリーンショットを保存しレビューに添付

## 差分隔離方針とレビュー

| レイヤ | 内容 | Chainlit 更新時の扱い | レビュー観点 |
| --- | --- | --- | --- |
| `core_ext/chainlit` | Upstream ソースのミラー | `git subtree` でタグ単位取り込み。直接編集禁止 | Upstream 差分の妥当性、`--squash` による履歴圧縮確認 |
| `core_ext/patches` | 独自パッチ（必要最小限） | Chainlit 側で未解決の issue を暫定補正 | Patch 適用順序と upstream へのフィードバック計画 |
| `app.py` / `src/` | 自前コード | `core_ext/` の公開 API のみ利用 | 依存逆流が無いこと、例外設計遵守 |

### レビューフロー
1. 当番が PR を作成し、Chainlit upstream 差分サマリとチェックリスト結果を記載
2. Reviewer（別担当者）が `core_ext/` への差分と自前コード影響を確認
3. メンテナンス担当（週次輪番リード）が最終承認しデプロイブランチにマージ
4. マージ後、翌営業日までに本番反映ステータスを ops channel に報告

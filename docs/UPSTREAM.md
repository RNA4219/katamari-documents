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

- **担当**: リポジトリオーナー（主担当） + AI アシスタント（差分要約・再確認）
- **スケジュール**: 毎週火曜 09:30 JST にタグ確認を開始し、同日 12:00 JST までに検証とログ更新を完了。遅延時はログに理由を追記。
- **実施手順**:
  1. `git fetch chainlit --tags` で最新タグを取得し、`git tag -l 'v*' --sort=-v:refname | head` で候補を確認。
  2. Release Note を読み、AI へ差分要約を依頼して breaking change の有無と影響領域を整理。
  3. 対象タグを `git diff` で比較し、`core_ext/` へ及ぶ変更と依存更新を洗い出す。
  4. チェックリストを実行しながら `docs/UPSTREAM_WEEKLY_LOG.md` に結果を追記。

### 差分検証チェックリスト
- [ ] `docs/UPSTREAM_WEEKLY_LOG.md` に実施日・担当・対象タグ・比較元タグ・コミット SHA・AI サポート有無を追記
- [ ] `git diff <prev_tag>..<target_tag> -- core_ext/chainlit` の要約（主要ファイル、行数）をログへ残す
- [ ] 依存解決コマンド（`poetry install` / `npm install` 等）の実行結果要約をログへ記録
- [ ] `pytest` / `npm test` のスモーク実行結果とコマンド出力要約をログへ記録
- [ ] UI 変更や見た目差分がある場合はスクリーンショットを `public/upstream/<date>/` に保存しパスをログへ記録

## 差分隔離方針とレビュー

| レイヤ | 内容 | Chainlit 更新時の扱い | レビュー観点 |
| --- | --- | --- | --- |
| `core_ext/chainlit` | Upstream ソースのミラー | `git subtree` でタグ単位取り込み。直接編集禁止 | Upstream 差分の妥当性、`--squash` による履歴圧縮確認 |
| `core_ext/patches` | 独自パッチ（必要最小限） | Chainlit 側で未解決の issue を暫定補正 | Patch 適用順序と upstream へのフィードバック計画 |
| `app.py` / `src/` | 自前コード | `core_ext/` の公開 API のみ利用 | 依存逆流が無いこと、例外設計遵守 |

### レビューフロー
1. 担当者が自己レビューを実施し、`docs/UPSTREAM_WEEKLY_LOG.md` のチェックリスト欄をすべて埋めた上で PR を作成
2. AI アシスタントに差分ハイライトとテスト結果を再検証させ、ログへ AI レビュー所見を追記
3. 担当者が AI 所見を反映して最終確認し、`main` へのマージを実施
4. マージ後、翌営業日までに `docs/UPSTREAM_WEEKLY_LOG.md` にデプロイ状況を追記し、必要なら ops channel にステータスを共有

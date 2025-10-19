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

- **担当**: リポジトリオーナー（主担当） + AI アシスタント（差分整理・記録補助）
- **スケジュール**: 毎週火曜 09:30 JST に開始し、同日 12:00 JST までに記録を確定。遅延・未完了はログに理由と再開予定を残す。
- **実施手順**:
  1. `docs/UPSTREAM_WEEKLY_LOG.md` の最新エントリを複製し、週次セクションに日付・担当・状況欄を用意する。
  2. `git fetch chainlit --tags` と `git tag -l 'v*' --sort=-v:refname | head` で最新タグを把握し、候補をログ欄に控える。
  3. Release Note の要点と想定影響を AI に要約させ、主要論点をログへ転記する。
  4. `git diff <prev_tag>..<target_tag>` で影響領域を確認し、`core_ext/` へ波及する論点をログの「差分メモ」に整理する。
  5. テスト・動作確認の要否を判断し、実施内容と結果をログの専用欄にまとめる。
  6. チェックリストを参照しながらログを埋め、完了後に AI に整合チェックを依頼する。

### 差分検証チェックリスト（記録ベース）
- [ ] `docs/UPSTREAM_WEEKLY_LOG.md` に該当週のエントリを作成し、日付・担当・対象タグ候補・比較元タグを記入
- [ ] リリースノート要約欄に breaking change の有無と対処方針を記入
- [ ] 差分メモ欄に `core_ext/` 影響点と依存更新の要否を記入
- [ ] テスト・検証欄に実施可否と結果（未実施理由含む）を記入
- [ ] 追跡メモ欄に AI レビュー所見と後続タスク（必要なら GitHub Projects へのカードリンク）を記入

## 差分隔離方針とレビュー

| レイヤ | 内容 | Chainlit 更新時の扱い | レビュー観点 |
| --- | --- | --- | --- |
| `core_ext/chainlit` | Upstream ソースのミラー | `git subtree` でタグ単位取り込み。直接編集禁止 | Upstream 差分の妥当性、`--squash` による履歴圧縮確認 |
| `core_ext/patches` | 独自パッチ（必要最小限） | Chainlit 側で未解決の issue を暫定補正 | Patch 適用順序と upstream へのフィードバック計画 |
| `app.py` / `src/` | 自前コード | `core_ext/` の公開 API のみ利用 | 依存逆流が無いこと、例外設計遵守 |

### レビューフロー
1. 担当者が自己レビューを実施し、`docs/UPSTREAM_WEEKLY_LOG.md` の当該エントリを自己チェック欄まで埋める
2. AI アシスタントにログと差分を共有し、レビュー観点と不足事項の指摘を受けて同エントリに所見として追記
3. 担当者が AI 所見に基づき修正・再確認を行い、自己レビュー完了印を付与してから PR を作成
4. マージ後は翌営業日までにエントリへリリース状況を追記し、必要に応じて GitHub Projects や ops channel へ共有する

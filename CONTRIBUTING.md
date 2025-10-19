# Contributing to Katamari

## ブランチ戦略
- リリース済みの安定コードは `main` ブランチで管理します。作業を始める前に必ず `git fetch` し、`main` を最新化してから派生してください。
- 新規機能は `feature/<issue番号>-<要約>`、バグ修正は `fix/<issue番号>-<要約>`、緊急対応は `hotfix/<要約>` の命名規則を徹底します。
- 1 PR = 1 トピックを守り、関連するコミットのみを含めます。レビュー前に `git rebase main` で履歴を整理し、不要なマージコミットを避けてください。
- 変更は極力 `src/core_ext/` と `providers/` に閉じ、他領域へ波及する場合は影響範囲を PR 説明で明示します。
- タスクが複数日にまたがる場合は、毎日 `git fetch origin && git rebase origin/main` を実施し、衝突リスクを最小化します。バックポートやリリース分岐が必要な場合は `release/<version>` ブランチを起点にした cherry-pick を利用し、マージ対象と履歴を Issue に記録します。
- 複数メンバーが関与する大型開発では、共通の統合ブランチ (`integration/<feature>`) を作成し、最低 1 日 1 回 `main` を取り込んだ上で CI を緑化してください。

### ブランチ運用フロー
#### ブランチクイックリファレンス
| 目的 | ブランチ名の例 | 派生元 | マージ先 | 備考 |
| --- | --- | --- | --- | --- |
| 新機能 | `feature/<issue番号>-<要約>` | `main` | `main` | テスト追加→実装→レビューの順に進める |
| バグ修正 | `fix/<issue番号>-<要約>` | `main` | `main` | 影響範囲を Issue と PR の双方で共有 |
| 緊急対応 | `hotfix/<要約>` | `main` または `release/<version>` | `main` と対象リリース | `--force-with-lease` で履歴整形、逆マージを必須化 |
| リリース | `release/<version>` | `main` | `main` | タグ発行後、残タスクは Follow-up Issue 化 |

1. `git switch main && git pull --ff-only` で最新状態を取得します。
2. 課題単位で `git switch -c feature/<issue番号>-<要約>` などの新規ブランチを作成します。
3. コミットはテスト緑化後に行い、`git push --set-upstream origin <branch>` でリモート追随させます。
4. レビュー中の修正は `git commit --amend` または `git rebase -i` で整え、強制プッシュ時は必ず `--force-with-lease` を使用します。

#### ブランチ運用チェックリスト
- [ ] 作業前に `git status` を確認し、未コミット差分がないことを確認した
- [ ] `git pull --ff-only` で main を最新化した
- [ ] Issue・タスク番号を含む新規ブランチ名を作成した
- [ ] main と衝突しそうなファイルを CODEOWNERS と共有した
- [ ] レビュー後は `git rebase main` で履歴を整理し、必要に応じてドラフト PR を更新した

### ブランチ保護ルール
- `main` への直接 push・ウェブ編集は禁止です。必ず Pull Request 経由でマージしてください。
- リリース作業は `release/<version>` ブランチを作成し、タグ付け (`git tag v<version>`) を行った上でマージします。
- 複数人で並行作業する場合は、ドラフト PR を早期に共有し、衝突しそうなファイルを `CODEOWNERS` と相談して担当を明確化してください。
- ステージング環境へのホットフィックスは `hotfix/<要約>` ブランチから行い、マージ後に必ず `main` へも逆マージして整合性を保ちます。
- リリースブランチに対する修正は `cherry-pick` を基本とし、同一修正を `main` にも必ず反映します。コミット本文には `Backport: <対象PR #>` を追記し、トレース性を確保してください。

### コミットポリシー
- 1 コミットは 1 つの論点に限定し、コミットメッセージは `[scope] 要約` 形式で 50 文字以内のタイトル + 必要に応じて本文を箇条書きで記述します。
- 実装変更に先立ちテストを追加し、赤→緑を確認してから本実装を行うテスト駆動を推奨します。`tests/` または `upstream/chainlit` 配下のケースを更新しない理由がある場合は PR の `## Notes` で説明してください。
- `git commit --amend` や `git rebase -i` を利用する際は、レビュー済みコミットを上書きしないようレビュアへ事前連絡し、履歴の再共有が必要ならドラフト PR 状態に戻します。
- 機密情報（API キー、個人情報）が含まれないことを `git diff --stat` と `git diff --check` で確認し、警告が発生した場合は修正後に再実行します。

## 品質ゲート
### テスト必須
- Python の基盤テストは `pytest -q` を最小単位とし、失敗時は関連テストケースを追加してから修正を行います。
- 型安全は `mypy --strict` を唯一の基準とし、抑制を追加する場合はコメントと Issue で恒久対応を追跡します。
- Lint は `ruff check .` をデフォルトとし、自動修正は該当差分のみに限定します。
- Node/ESM のユニットテストは `node:test` ベースで `pnpm run test` に統合し、必要に応じて `pnpm run test -- --watch` で再現確認します。
- UI 変更はスクリーンショットまたは動画を必ず取得し、PR テンプレートの `## Notes` に添付します。
- 迷った場合は `make test` → `pytest -q` → `ruff check .` → `mypy --strict` の順に再実行し、すべての成功ログを記録してください。

#### テスト / Lint 実行クイックガイド
| 対象 | 必須コマンド | 目的 |
| --- | --- | --- |
| Python | `pytest -q` | 回帰検知とリグレッション防止 |
| Python 型 | `mypy --strict` | 型安全と例外ポリシーの遵守確認 |
| Python Lint | `ruff check .` | コードスタイルおよび設計逸脱の検知 |
| Node/ESM | `cd upstream/chainlit && pnpm run test` | `node:test` ベースの自動テスト実行 |
| Node Lint | `cd upstream/chainlit && pnpm run lint` | ESLint/TS による静的解析 |
| UI ビルド | `cd upstream/chainlit && pnpm run buildUi` | 本番向けビルドの健全性確認 |

- Python コードは `pytest -q` を必ずグリーンにしてください。外部リソースに依存するテストは `pytest -q -m "not slow"` での確認も行います。
- Chainlit フロントエンドや Node 周辺を変更した場合は `cd upstream/chainlit && pnpm install && pnpm run test` を実行し、E2E が必要なら `pnpm run test:ui` を追加で回してください。
- UI を含む変更ではスクリーンショットやキャプチャ動画を `## Notes` セクションに添付し、レビュアが再現可能な情報を提供します。
- 迷った場合は `make test` を起点にし、CI の `pytest -q` と同一コマンドをローカルでも再現してください。
- すべてのテストコマンド実行ログ（抜粋で可）を PR テンプレートの `## Test` セクションへ貼り付け、失敗時のリトライ理由をコメントに追記します。
- 依存サービスをモックする場合は `tests/fixtures/` にスタブを追加し、`pytest --strict-markers` で未登録マーカーが存在しないことを確認してください。
- Node.js で `node:test` ベースの検証を追加した場合は、`package.json` にスクリプトを登録し `pnpm run test` から呼び出せるよう整備します。

#### 標準テストシーケンス
1. 依存関係を最新化：`pip install -r requirements.txt` / `pnpm install`
2. Python ユニット：`pytest -q`
3. Node/ESM 変更時：`cd upstream/chainlit && pnpm run test`
4. 変更範囲に応じてマーカー指定（例：`pytest -q tests/path/test_x.py -k scenario`）で再現
5. 失敗したテストは修正コミット後に同一コマンドで再実行し、ログを PR に貼付

### Lint / Type Check
- Python は `ruff check .` で lint、`mypy --strict` で型チェックを通過させてください。差分に合わせて `ruff --fix` や `mypy --strict src/...` を活用し、型エラーを解消します。
- `src/` 以下で ESM/TypeScript を触る場合は `pnpm run lint`（ESLint + TypeScript）と `pnpm run buildUi` でビルドが通ることを確認します。
- `pre-commit` を使用している場合でも手動での最終確認を省略しないでください。CI 失敗はレビュー停止の対象です。
- 最低限 `ruff check . && mypy --strict && pytest -q` を同一シェルで実行し、成功ログを PR の `## Test` セクションへ貼り付けてください。
- Lint/型チェック専用コミットを作成する場合は、そのコミット内での自動整形差分を必ず確認し、不要な大量変更を含めないようにしてください。
- `ruff` の自動修正で対応できない警告は Issue としてトラッキングし、PR 説明の `## Notes` で対応方針を共有してください。
- `mypy` の新規抑制（`type: ignore`）を追加する際は理由と Issue リンクをコメントで残し、恒久対応の期限を `## Notes` に明記します。
- Lint/型チェックは PR 作成前とレビュー修正後の 2 回以上実行し、`git status --short` が空であることを確認してから push してください。

#### Lint / 型チェックシーケンス
1. ルートで `ruff check .` → 自動修正は `ruff --fix <files>` を限定的に使用
2. Python 型検証：`mypy --strict`
3. フロントエンド改修時：`pnpm run lint` と `pnpm run buildUi`
4. 失敗時は該当コミットで修正し、再実行ログを PR に追記

## PR テンプレの使い方
- PR 作成時は `.github/PULL_REQUEST_TEMPLATE.md` が自動で展開されます。各セクションに必ず記入し、空欄のまま提出しないでください。
- `## What` には変更内容の概要、`## Why` には目的・背景を簡潔に記載します。
- `## Test` のチェックボックスは実行結果を根拠にオンにし、未実施の場合はオフのまま実行予定をコメントで共有してください。
- 参照 Issue や追加情報は `## Notes` に追記し、レビュアが判断できるようリンクを整理します。
- テンプレ内の `## Checklist` が増えた場合は全項目の Yes/No を明確化し、未完了のものは着手予定日時をコメントで補足してください。
- テンプレートの項目を削除・改変する場合は `## Notes` で理由を説明し、レビュアの同意を得てからマージしてください。
- スクリーンショットやログなどの添付は GitHub の Markdown 形式で埋め込み、外部ストレージのリンクのみを共有しないでください。
- ドキュメントのみの変更でも `## Test` セクションでは実行しなかったコマンドと理由を明示し、レビュアが再現不要と判断できる根拠を添えてください。
- レビュアコメントを解消した際は該当スレッドを Resolve し、`## Checklist` の該当項目に ✅/❌ を反映してください。
- テンプレートの最後にある `## Checklist` は `mypy --strict` / `ruff check .` / `pytest -q` / `pnpm run test` の各結果と同期させ、ログが貼付されていないチェックはオンにしないでください。
- 例外的にテンプレの編集が必要な場合はドラフト状態で相談し、最終マージまでにテンプレ構造を復元してください。
- PR 本文に「リリース影響なし」などのサマリタグを付ける場合は `## Notes` へも同じ文言を転記し、検索性を確保します。

#### PR テンプレ記入チェックリスト
- [ ] `## What` と `## Why` を 3 行以内で要約
- [ ] `## Test` に実行コマンドと成功ログを貼付
- [ ] `## Checklist` の各項目に明示的な Yes/No を記入
- [ ] 影響範囲（UI/API/CLI 等）を `## Notes` に記述
- [ ] 必要なスクリーンショット・動画・ログを Markdown で添付
- [ ] レビュー観点・未決事項を `## Notes` に列挙し、追加調査があれば担当者を明示

## レビューとマージ
- 少なくとも 1 名の CODEOWNERS レビュア承認が必要です。必要に応じてドラフト PR で早期フィードバックをもらってください。
- CODEOWNERS が複数いる場合は、最低 2 名の合意（Approve または LGTM コメント）が揃ったタイミングでマージ可能です。相反するレビューがあるときはディスカッションを解消し、関係者の合意をコメントで明記してください。
- CI がすべて通過した後、Squash and Merge を推奨します。複数コミットを残す場合は意味のある粒度でまとめてください。
- Fork, create feature branch, open PR with tests.
- Keep diffs in `core_ext/` and `providers/` when possible.
- Follow the issue templates.
- Adhere to `.gitattributes` line ending policy (LF for shell/Python/Makefile, CRLF for PowerShell).
- GitHub Review のステータスは `Comment` / `Approve` / `Request changes` を正しく使い分け、レビュー観点を箇条書きで残してください。
- 仕様に関わる合意は PR 内のコメントまたはリンクされた Issue で記録し、マージ時に `## Notes` に最終判断を追記してください。

#### レビュー合意フロー
1. PR 作成者は主要な論点を `## Notes` に要約し、必要レビュアをメンション
2. 各レビュアは `Request changes` 時に再現手順と修正期待値を明文化
3. 修正後は作成者が解決コメントを追記し、レビュアの `Resolve conversation` を待つ
4. すべてのブロッカーが解消されたら CODEOWNERS 最少 1 名 + 追加レビュア 1 名の承認を取得
5. マージ前に最終テスト結果を `## Test` に追記し、Squash or Rebase 方針をコメントで共有
### ADR を追加・更新する手順
1. `docs/adr/0000-template.md` をコピーし、次の連番（例: `0005-new-decision.md`）とタイトルを付与する。ファイル冒頭のステータスと更新日を必ず記入する。
2. 「Context / Decision / Consequences / Status / DoD」に背景・決定理由・影響範囲・進捗状況を明示する。Status セクションでは「ステータス」「最終更新日」を個別行で記載し、代替案を検討した場合は Decision セクションで触れる。
3. `docs/adr/README.md` の目次テーブルへ新規 ADR を追加し、ステータス変更があれば同時に更新する。
4. `docs/ROADMAP_AND_SPECS.md` や関連ドキュメントからの参照リンクを最新化する。マイルストーンや仕様の整合が必要な場合は同一 PR で対応する。
5. PR 説明では対象 ADR の背景・結論・影響範囲をサマリとして記載し、レビュアが判断できる補足資料を添付する。
6. DoD に列挙したフォローアップ（例: スクリプト更新や Feature Flag 追加）が実施済みであることを PR チェックリストで明示する。

## ADR / 要件整合フロー
- マイルストーン着手前に該当 ADR（`docs/adr/`）の目的・スコープ・DoD を確認し、差分がある場合は PR で更新する。
- 仕様変更時は Katamari Requirements（FR/AC）、WBS（`docs/katamari_wbs.csv`）、関連 addenda を同一 PR で整合させる。
- ADR を新規追加・更新した場合は、PR 説明に対象マイルストーンと影響する FR/AC 番号を明記する。

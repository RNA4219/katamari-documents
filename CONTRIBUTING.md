# Contributing to Katamari

このリポジトリは個人でメンテナンスしている OSS です。作業の流れはシンプルに保ち、気軽に改善案を試せることを大切にしています。

## 作業の進め方
- `main` に直接コミットして構いません。履歴を整理したい場合だけ `feature/<説明>` のようなブランチを作成してください。
- Issue が無くても OK ですが、挙動の相談やタスクのメモは Issue にまとめておくと後で追跡しやすくなります。
- 変更が小さく済むように意識し、レビューしやすい粒度で Pull Request を作成してください。

## コミットと Pull Request
- コミットメッセージは簡潔な日本語または英語で要点を 1 行に書きます。
- Pull Request はテンプレートをそのまま使い、埋められる項目だけで構いません。未実施のことは空欄のままで問題ありません。
- レビューは基本的にメンテナー自身が行います。気になる点があれば Draft のままメモを残してください。

## チェックしてほしいこと
- Python のコードを触った場合は `ruff check .` と `mypy --strict` と `pytest -q` を一度ずつ実行してください。
- Node/フロントエンドに触れた場合は `pnpm run lint` と `pnpm run test` を目安に実行します。対象外なら「対象外」とだけ PR に書けば大丈夫です。
- テストのログは全文を貼る必要はありません。成功したことが分かる一行があれば十分です。

## Guardrails ドキュメント更新フロー
1. 設計判断や運用手順に影響が出る変更は、まず `BLUEPRINT.md`・`RUNBOOK.md`・`EVALUATION.md`・`CHECKLISTS.md` の担当ロールを確認します。
2. 更新が必要なドキュメントに差分を加えたら、Task Seed (`TASK.<YYYY-MM-DD>-0001.md` など) にフォローアップを記録してください。
3. 変更内容を Pull Request で共有し、`docs/ROADMAP_AND_SPECS.md#guardrails-ドキュメント更新フロー` の手順に沿って整合性をレビューします。
4. Guardrails 原典 ([`third_party/Day8/workflow-cookbook/GUARDRAILS.md`](third_party/Day8/workflow-cookbook/GUARDRAILS.md)) を参照し、Purpose/Scope/AC と矛盾していないか確認してください。
5. ドキュメント更新後は Birdseye 図や関連チェックリストを同期し、役割ごとの証跡が追跡できるようにします。

## メンテナーからのお願い
- 機密情報（API キー等）はコミットに含めないでください。
- 大きめの設計変更を検討する際は、先に Issue や Discussion で方針を共有してもらえると助かります。
- わからない点や迷った点は遠慮なくコメントしてください。ドキュメントの更新だけでも歓迎です。

## ADR を追加・更新する手順
1. `docs/adr/README.md` を参照して未使用の連番（4 桁ゼロ埋め）を決めます。
2. `docs/adr/0000-template.md` をコピーし、新しいファイル名にリネームします。
3. タイトル・Context・Decision・Consequences・Status を埋め、ステータスと最終更新日を最新状態に合わせます。
4. DoD セクションはチェックボックス形式のまま残し、完了条件を具体的に記述します（マイルストーン ADR の場合は `docs/katamari_wbs.csv` の DoD と整合させる）。
5. 新しい ADR を `docs/adr/README.md` の一覧表に追記します。
6. 変更に伴う追加ドキュメントやフォローアップがあれば、DoD の "Follow-up" として明示します。

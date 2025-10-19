# Katamari (Chainlit Fork) – 要件&仕様パック

<!-- LLM-BOOTSTRAP v1 -->
読む順番:
1. [`docs/birdseye/index.json`](docs/birdseye/index.json) …… ノード一覧・隣接関係（軽量）
2. [`docs/birdseye/caps/<path>.json`](docs/birdseye/caps) …… 必要ノードだけ point read（個別カプセル）
3. [`docs/ROADMAP_AND_SPECS.md`](docs/ROADMAP_AND_SPECS.md) …… Birdseye ノードと仕様ハブを突き合わせ、優先タスクを特定
4. [`docs/birdseye/hot.json`](docs/birdseye/hot.json) …… 頻出エントリポイントの鮮度確認（`generated_at` は共通タイムスタンプで更新）
5. [third_party/Day8/README.md](third_party/Day8/README.md) …… Day8 資料の総覧（詳細は `docs/day8/README.md`）
6. Guardrails 基盤ドキュメント: [BLUEPRINT.md](BLUEPRINT.md)（設計指針）→ [RUNBOOK.md](RUNBOOK.md)（運用手順）→ [EVALUATION.md](EVALUATION.md)（受入判定）→ [CHECKLISTS.md](CHECKLISTS.md)（Dev→Ops チェックリスト）→ [TASK.<YYYY-MM-DD>-0001.md](TASK.2025-10-19-0001.md)（タスク追跡）
7. Day8 オペレーション資料（推奨参照順）: [HUB.codex.md](third_party/Day8/workflow-cookbook/HUB.codex.md)（観測ハブ）→ [GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)（統制基準）→ [BLUEPRINT.md](third_party/Day8/workflow-cookbook/BLUEPRINT.md) 群（運用設計）

> [`docs/birdseye/hot.json`](docs/birdseye/hot.json) の `generated_at` は頻出入口リストの生成時刻です。エントリポイントや依存関係を更新した際は `date -u '+%Y-%m-%dT%H:%M:%SZ'` で時刻を取得し、[`docs/birdseye/index.json`](docs/birdseye/index.json)・`docs/birdseye/caps/`・[`docs/birdseye/hot.json`](docs/birdseye/hot.json) を併せて更新してください。
> 1. `date -u '+%Y-%m-%dT%H:%M:%SZ'` を実行して共通タイムスタンプを取得
> 2. [`docs/birdseye/index.json`](docs/birdseye/index.json) の `generated_at` と対象ノードの `mtime` を更新
> 3. 更新対象の `docs/birdseye/caps/*.json` と [`docs/birdseye/hot.json`](docs/birdseye/hot.json) に同じ `generated_at` を反映
> 4. [`docs/birdseye/hot.json`](docs/birdseye/hot.json) には Chainlit 起動やプロバイダー呼び出しなど主要なエントリポイント ID を 3 件程度列挙し、理由を最新化
> 5. `hot.json` の `entries` は Birdseye index の主要ノード（エントリポイント / ワークフロー制御 / コンテキスト制御）と整合させる
> 6. 各カプセル JSON では `summary` / `role` / `deps` / `tests` を現行コードとテストに合わせて更新

フォーカス手順:
- 直近変更ファイル±2hopのノードIDを [`docs/birdseye/index.json`](docs/birdseye/index.json) から取得
- 対応する `docs/birdseye/caps/*.json` のみ読み込み

参照リンク:
- 仕様ハブ: [`docs/ROADMAP_AND_SPECS.md`](docs/ROADMAP_AND_SPECS.md)
- Guardrails 基盤ドキュメント: [`BLUEPRINT.md`](BLUEPRINT.md), [`RUNBOOK.md`](RUNBOOK.md), [`EVALUATION.md`](EVALUATION.md), [`CHECKLISTS.md`](CHECKLISTS.md), [`TASK.<YYYY-MM-DD>-0001.md`](TASK.2025-10-19-0001.md)
- Birdseye 参照先（整備予定）: `docs/birdseye/README.md`
- Birdseye 再生成フロー: `RUNBOOK.md` と [`third_party/Day8/workflow-cookbook/tools/codemap/update.py`](third_party/Day8/workflow-cookbook/tools/codemap/update.py)
- CHANGELOG 更新フロー: [`CHANGELOG.md#更新手順`](CHANGELOG.md#%E6%9B%B4%E6%96%B0%E6%89%8B%E9%A0%86)

アップデート手順メモ:
1. `date -u '+%Y-%m-%dT%H:%M:%SZ'` を実行して共通タイムスタンプを取得
2. [`docs/birdseye/index.json`](docs/birdseye/index.json) の `generated_at` と対象ノードの `mtime` を更新
3. 更新対象の `docs/birdseye/caps/*.json` と [`docs/birdseye/hot.json`](docs/birdseye/hot.json) に同じ `generated_at` を反映
4. [`docs/birdseye/hot.json`](docs/birdseye/hot.json) には Chainlit 起動やプロバイダー呼び出しなど主要なエントリポイント ID を 3 件程度列挙し、理由を最新化
5. `hot.json` の `entries` は Birdseye index の主要ノード（エントリポイント / ワークフロー制御 / コンテキスト制御）と整合させる
<!-- /LLM-BOOTSTRAP -->

## 同梱物
- 要件: [`docs/Katamari_Requirements_v3_ja.md`](docs/Katamari_Requirements_v3_ja.md)
- 機能仕様: [`docs/Katamari_Functional_Spec_v1_ja.md`](docs/Katamari_Functional_Spec_v1_ja.md)
- 技術仕様: [`docs/Katamari_Technical_Spec_v1_ja.md`](docs/Katamari_Technical_Spec_v1_ja.md)
- ロードマップ & 仕様索引: [`docs/ROADMAP_AND_SPECS.md`](docs/ROADMAP_AND_SPECS.md)
- OpenAPI: [`docs/openapi/katamari_openapi.yaml`](docs/openapi/katamari_openapi.yaml)
- 設定: [`config/model_registry.json`](config/model_registry.json), [`config/env.example`](config/env.example)
- フォーク運用: [`docs/UPSTREAM.md`](docs/UPSTREAM.md), [`docs/FORK_NOTES.md`](docs/FORK_NOTES.md)
- ADR: [`docs/adr/README.md`](docs/adr/README.md)
- Day8 HUB / Guardrails / Blueprint 群: `third_party/Day8/workflow-cookbook/HUB.codex.md`, `third_party/Day8/workflow-cookbook/GUARDRAILS.md`, `third_party/Day8/workflow-cookbook/BLUEPRINT.md`

## 主要導線
- 要件・仕様ハブ: [`docs/ROADMAP_AND_SPECS.md`](docs/ROADMAP_AND_SPECS.md)
- 詳細要件: [`docs/Katamari_Requirements_v3_ja.md`](docs/Katamari_Requirements_v3_ja.md)
- 機能仕様: [`docs/Katamari_Functional_Spec_v1_ja.md`](docs/Katamari_Functional_Spec_v1_ja.md)
- 技術仕様: [`docs/Katamari_Technical_Spec_v1_ja.md`](docs/Katamari_Technical_Spec_v1_ja.md)
- OpenAPI: [`docs/openapi/katamari_openapi.yaml`](docs/openapi/katamari_openapi.yaml)
- 変更履歴: [`CHANGELOG.md`](CHANGELOG.md)（更新フロー: [`CHANGELOG.md#更新手順`](CHANGELOG.md#%E6%9B%B4%E6%96%B0%E6%89%8B%E9%A0%86) / [`README.md#変更履歴の更新ルール`](README.md#%E5%A4%89%E6%9B%B4%E5%B1%A5%E6%AD%B4%E3%81%AE%E6%9B%B4%E6%96%B0%E3%83%AB%E3%83%BC%E3%83%AB)）
- フォーク運用: [`docs/UPSTREAM.md`](docs/UPSTREAM.md), [`docs/FORK_NOTES.md`](docs/FORK_NOTES.md)
- Day8 オペレーション資料（推奨参照順: HUB → Guardrails → Blueprint）: [`third_party/Day8/workflow-cookbook/HUB.codex.md`](third_party/Day8/workflow-cookbook/HUB.codex.md)（観測ハブ）→ [`third_party/Day8/workflow-cookbook/GUARDRAILS.md`](third_party/Day8/workflow-cookbook/GUARDRAILS.md)（統制基準）→ [`third_party/Day8/workflow-cookbook/BLUEPRINT.md`](third_party/Day8/workflow-cookbook/BLUEPRINT.md)（運用設計）

## ローカル起動手順

### 依存インストールとセットアップ

1. Python 3.11 系を用意し、任意の場所で仮想環境を作成する。
2. `.env` を [`config/env.example`](config/env.example) からコピーし、後述の表を参照して値を埋める。
3. `make dev` で Python 依存を一括インストールする（`pip install -r requirements.txt` と同等）。

```bash
python -m venv .venv
source .venv/bin/activate
cp config/env.example .env
make dev
```

- GNU Make が利用できない場合は `pip install -r requirements.txt` を直接実行しても良い。
- 依存パッケージの更新が必要になった際も `make dev` を再実行する。

### アプリのローカル実行

- `make run` で Chainlit を `http://localhost:8787`（`PORT` 変更時はその値）に起動する。
- 終了は実行ターミナルで `Ctrl + C`。

```bash
make run
```

## 環境変数一覧

`.env` の初期値は [`config/env.example`](config/env.example) を参照してください。値の詳細や追加オプションは必要に応じて [`README_PERSONAS_THEMES.md`](README_PERSONAS_THEMES.md) も確認してください。

| 種別 | 名称 | 用途 | 設定例 | 備考 |
| ---- | ---- | ---- | ------ | ---- |
| 必須 | `OPENAI_API_KEY` | OpenAI プロバイダー利用時の API キー | `OPENAI_API_KEY=sk-...` | `.env` のみで管理し、Git には含めない |
| 任意 | `GOOGLE_GEMINI_API_KEY` | Google Gemini プロバイダー利用時の API キー | `GOOGLE_GEMINI_API_KEY=...` | Gemini API を利用する場合のみ |
| 任意 | `GEMINI_API_KEY` | 旧名称。既存デプロイ互換用 | `GEMINI_API_KEY=...` | 既存環境からの移行時に保持 |
| 任意 | `DEFAULT_PROVIDER` | 既定で使用する LLM プロバイダー識別子 | `DEFAULT_PROVIDER=openai` | 省略時は OpenAI |
| 任意 | `CHAINLIT_AUTH_SECRET` | Chainlit セッション署名用シークレット | `CHAINLIT_AUTH_SECRET=change-me` | 本番は十分な長さに変更 |
| 任意 | `PORT` | `make run` の待ち受けポート | `PORT=8787` | Docker 起動時は `-p <host>:<PORT>` と併用 |
| 任意 | `LOG_LEVEL` | Chainlit ログ出力レベル | `LOG_LEVEL=info` | `debug`/`warning` などを指定可 |
| 任意 | `SEMANTIC_RETENTION_PROVIDER` | 会話保持率メトリクス算出時の埋め込みプロバイダー | `SEMANTIC_RETENTION_PROVIDER=openai` | 指定時は下記モデル設定も併用 |
| 任意 | `SEMANTIC_RETENTION_OPENAI_MODEL` | OpenAI 埋め込みモデル名 | `SEMANTIC_RETENTION_OPENAI_MODEL=text-embedding-3-large` | OpenAI プロバイダー指定時に利用 |
| 任意 | `SEMANTIC_RETENTION_GEMINI_MODEL` | Google Gemini 埋め込みモデル名 | `SEMANTIC_RETENTION_GEMINI_MODEL=text-embedding-004` | Gemini プロバイダー指定時に利用 |
| 任意 | `GOOGLE_API_KEY` | Gemini 埋め込み生成用 API キー（会話保持率用） | `GOOGLE_API_KEY=...` | `SEMANTIC_RETENTION_PROVIDER=google_gemini` 時に必要 |

> まず `.env` に必須項目を入力し、環境に合わせて任意項目を追記してください。

### `.env` 設定例

```dotenv
OPENAI_API_KEY=sk-...
DEFAULT_PROVIDER=openai
CHAINLIT_AUTH_SECRET=change-me
PORT=8787
LOG_LEVEL=info
```

## テーマ切り替え

1. Chainlit UI 右上の **Settings → Theme** から `themes/` 配下のプリセット（`.theme.json`）を選択する。
2. テーマを追加する場合は `themes/` に `.theme.json` を配置し、同メニューの **Theme → Import JSON** で読み込む。
3. ペルソナ設定と連携するテーマの編集手順は [`README_PERSONAS_THEMES.md`](README_PERSONAS_THEMES.md) で詳細を確認する。

- 本パックは「katamari」の要件定義・機能仕様・技術仕様・OpenAPI・初期設定を含むドキュメント集です。
- まずは `docs/Katamari_Requirements_v3_ja.md` をご確認ください。

## Docker イメージの利用

リポジトリ同梱の `Dockerfile` は `chainlit run src/app.py` を既定コマンドとして公開しています。

```bash
# ビルド
docker build -t katamari:dev .

# 起動 (ポートは PORT 環境変数で変更可能)
docker run --rm -e PORT=8787 -p 8787:8787 katamari:dev
```

GitHub Container Registry への公開フローは [docs/addenda/H_Deploy_Guide.md](docs/addenda/H_Deploy_Guide.md) を参照してください。
## 運用エンドポイント

- `GET /healthz`: Chainlit アプリの Liveness。`{"status":"ok"}` を返却。
- `GET /metrics`: Prometheus Text Format (`compress_ratio`, `semantic_retention`) を露出。

## 変更履歴の更新ルール

1. PR で顕著な差分が出たら、必ず [`CHANGELOG.md`](CHANGELOG.md) の `[Unreleased]` に追記する。
2. 記法は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) を踏襲し、`Added`/`Changed`/`Deprecated`/`Removed`/`Fixed`/`Security` の分類に整理する（不要な分類は削除可）。
3. 各エントリの先頭に 4 桁ゼロ埋めの通番（例: `0001`）を付与し、既存の最大値から 1 ずつ繰り上げる。
4. リリース確定時は `[Unreleased]` のエントリを新しいバージョン見出しへ移し、セマンティックバージョンと日付を付けてタグ作成と同じコミットで確定する。
5. README やロードマップに散在する履歴は、該当リリースの見出しへ移管し、`docs/Release_Checklist.md` と併せて公開する。

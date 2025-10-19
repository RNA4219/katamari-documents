# Katamari (Chainlit Fork) – 要件&仕様パック

<!-- README_TOP_TEMPLATE v1 -->
> **Birdseye参照フロー**
> 1. `docs/birdseye/index.json` で対象ノードID・依存を確認。
> 2. `docs/birdseye/caps/<path>.json` の必要カプセルのみ point read。
> 3. `docs/birdseye/hot.json` の頻出入口と `generated_at` を照合し、古い場合は `date -u '+%Y-%m-%dT%H:%M:%SZ'` で共通タイムスタンプを取得して一括更新。
>
> **仕様ハブ**
> - 横断導線: [`docs/ROADMAP_AND_SPECS.md`](docs/ROADMAP_AND_SPECS.md)
> - Birdseye 再生成: `RUNBOOK.md` の更新手順、[`third_party/Day8/workflow-cookbook/tools/codemap/update.py`](third_party/Day8/workflow-cookbook/tools/codemap/update.py)
<!-- /README_TOP_TEMPLATE -->

<!-- LLM-BOOTSTRAP v1 -->
読む順番:
1. docs/birdseye/index.json  …… ノード一覧・隣接関係（軽量）
2. docs/birdseye/caps/<path>.json …… 必要ノードだけ point read（個別カプセル）
3. docs/ROADMAP_AND_SPECS.md …… Birdseye ノードと仕様ハブを突き合わせ、優先タスクを特定
4. docs/birdseye/hot.json …… 頻出エントリポイントの鮮度確認（`generated_at` をテンプレート上記手順で更新）
5. [third_party/Day8/README.md](third_party/Day8/README.md) …… Day8 資料の総覧（詳細は `docs/day8/README.md`）
6. Day8 オペレーション資料（推奨参照順）: [HUB.codex.md](third_party/Day8/workflow-cookbook/HUB.codex.md)（観測ハブ）→ [GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)（統制基準）→ [BLUEPRINT.md](third_party/Day8/workflow-cookbook/BLUEPRINT.md)（運用設計）

> `docs/birdseye/hot.json` の `generated_at` は頻出入口リストの生成時刻です。エントリポイントや依存関係を更新した際は `date -u '+%Y-%m-%dT%H:%M:%SZ'` で時刻を取得し、`docs/birdseye/index.json`・`docs/birdseye/caps/`・`docs/birdseye/hot.json` を併せて更新してください。
> 1. `date -u '+%Y-%m-%dT%H:%M:%SZ'` を実行して共通タイムスタンプを取得
> 2. `docs/birdseye/index.json` の `generated_at` と対象ノードの `mtime` を更新
> 3. 更新対象の `docs/birdseye/caps/*.json` と `docs/birdseye/hot.json` に同じ `generated_at` を反映
> 4. `docs/birdseye/hot.json` には Chainlit 起動やプロバイダー呼び出しなど主要なエントリポイント ID を 3 件程度列挙し、理由を最新化

フォーカス手順:
- 直近変更ファイル±2hopのノードIDを `index.json` から取得
- 対応する `caps/*.json` のみ読み込み

<!-- /LLM-BOOTSTRAP -->

## 主要導線
- 要件・仕様ハブ: [`docs/ROADMAP_AND_SPECS.md`](docs/ROADMAP_AND_SPECS.md)
- 詳細要件: [`docs/Katamari_Requirements_v3_ja.md`](docs/Katamari_Requirements_v3_ja.md)
- 機能仕様: [`docs/Katamari_Functional_Spec_v1_ja.md`](docs/Katamari_Functional_Spec_v1_ja.md)
- 技術仕様: [`docs/Katamari_Technical_Spec_v1_ja.md`](docs/Katamari_Technical_Spec_v1_ja.md)
- OpenAPI: [`docs/openapi/katamari_openapi.yaml`](docs/openapi/katamari_openapi.yaml)
- フォーク運用: [`docs/UPSTREAM.md`](docs/UPSTREAM.md), [`docs/FORK_NOTES.md`](docs/FORK_NOTES.md)
- Day8 オペレーション資料: [`third_party/Day8/workflow-cookbook/HUB.codex.md`](third_party/Day8/workflow-cookbook/HUB.codex.md)（観測ハブ）→ [`third_party/Day8/workflow-cookbook/GUARDRAILS.md`](third_party/Day8/workflow-cookbook/GUARDRAILS.md)（統制基準）→ [`third_party/Day8/workflow-cookbook/BLUEPRINT.md`](third_party/Day8/workflow-cookbook/BLUEPRINT.md)（運用設計）

## 同梱物
- 要件: [`docs/Katamari_Requirements_v3_ja.md`](docs/Katamari_Requirements_v3_ja.md)
- 機能仕様: [`docs/Katamari_Functional_Spec_v1_ja.md`](docs/Katamari_Functional_Spec_v1_ja.md)
- 技術仕様: [`docs/Katamari_Technical_Spec_v1_ja.md`](docs/Katamari_Technical_Spec_v1_ja.md)
- ロードマップ & 仕様索引: [`docs/ROADMAP_AND_SPECS.md`](docs/ROADMAP_AND_SPECS.md)
- OpenAPI: [`docs/openapi/katamari_openapi.yaml`](docs/openapi/katamari_openapi.yaml)
- 設定: [`config/model_registry.json`](config/model_registry.json), [`config/env.example`](config/env.example)
- フォーク運用: [`docs/UPSTREAM.md`](docs/UPSTREAM.md), [`docs/FORK_NOTES.md`](docs/FORK_NOTES.md)
- ADR: [`docs/adr/README.md`](docs/adr/README.md)
- Day8 HUB / Guardrails / Blueprint: `third_party/Day8/workflow-cookbook/HUB.codex.md`, `third_party/Day8/workflow-cookbook/GUARDRAILS.md`, `third_party/Day8/workflow-cookbook/BLUEPRINT.md`

## ローカル起動手順

### 前提インストール

- Python 3.11 系（`python -m venv .venv && source .venv/bin/activate` で仮想環境を推奨）
- 依存パッケージは `pip install -r requirements.txt` または `make dev`

### セットアップ

```bash
python -m venv .venv
source .venv/bin/activate
cp config/env.example .env  # 必須・任意の値をこのファイルで管理
make dev                    # 依存関係を一括インストール
```

### 起動フロー

```bash
make run  # Chainlit を http://localhost:8787 で起動
```

- アプリ終了は実行ターミナルで `Ctrl + C`
- 依存を更新したい場合は別ターミナルで `make dev`

## 環境変数一覧

| 名称 | 必須 | 用途 | 設定例 | 備考 |
| ---- | ---- | ---- | ------ | ---- |
| `OPENAI_API_KEY` | 必須 | OpenAI プロバイダー利用時の API キー | `OPENAI_API_KEY=sk-...` | サンプルは [`config/env.example`](config/env.example) を参照 |
| `GOOGLE_GEMINI_API_KEY` | 任意 | Google Gemini プロバイダー利用時の API キー | `GOOGLE_GEMINI_API_KEY=...` | Gemini API を利用する場合のみ |
| `GEMINI_API_KEY` | 任意 | 旧名称。既存デプロイ互換用 | `GEMINI_API_KEY=...` | 既存環境からの移行時に保持 |
| `DEFAULT_PROVIDER` | 任意 | 既定で使用する LLM プロバイダー識別子 | `DEFAULT_PROVIDER=openai` | 省略時は OpenAI |
| `CHAINLIT_AUTH_SECRET` | 任意（本番推奨） | Chainlit セッション署名用シークレット | `CHAINLIT_AUTH_SECRET=change-me` | 本番は十分な長さに変更 |
| `PORT` | 任意 | `make run` の待ち受けポート | `PORT=8787` | Docker 起動時は `-p <host>:<PORT>` と併用 |
| `LOG_LEVEL` | 任意 | Chainlit ログ出力レベル | `LOG_LEVEL=info` | `debug`/`warning` などを指定可 |
| `SEMANTIC_RETENTION_PROVIDER` | 任意 | 会話保持率メトリクス算出時の埋め込みプロバイダー | `SEMANTIC_RETENTION_PROVIDER=openai` | 指定時は下記モデル設定も併用 |
| `SEMANTIC_RETENTION_OPENAI_MODEL` | 任意 | OpenAI 埋め込みモデル名 | `SEMANTIC_RETENTION_OPENAI_MODEL=text-embedding-3-large` | OpenAI プロバイダー指定時に利用 |
| `SEMANTIC_RETENTION_GEMINI_MODEL` | 任意 | Google Gemini 埋め込みモデル名 | `SEMANTIC_RETENTION_GEMINI_MODEL=text-embedding-004` | Gemini プロバイダー指定時に利用 |
| `GOOGLE_API_KEY` | 任意 | Gemini 埋め込み生成用 API キー（会話保持率用） | `GOOGLE_API_KEY=...` | `SEMANTIC_RETENTION_PROVIDER=google_gemini` 時に必要 |

### `.env` 設定例

```dotenv
OPENAI_API_KEY=sk-...
DEFAULT_PROVIDER=openai
CHAINLIT_AUTH_SECRET=change-me
PORT=8787
LOG_LEVEL=info
```

> まず `cp config/env.example .env` を行い、上記を参考に必須項目を埋めてください。

## テーマ切り替え

1. Chainlit UI 右上の **Settings → Theme** から `themes/` 配下のプリセット（`.theme.json`）を選択
2. 追加したいテーマ JSON を `themes/` に配置し、同メニューの **Theme → Import JSON** で読み込む
3. ペルソナ連携やテーマ JSON の詳細は [`README_PERSONAS_THEMES.md`](README_PERSONAS_THEMES.md) を参照

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
3. リリース確定時は `[Unreleased]` のエントリを新しいバージョン見出しへ移し、セマンティックバージョンと日付を付けてタグ作成と同じコミットで確定する。
4. README やロードマップに散在する履歴は、該当リリースの見出しへ移管し、`docs/Release_Checklist.md` と併せて公開する。

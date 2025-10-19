# Katamari (Chainlit Fork) – 要件&仕様パック

<!-- LLM-BOOTSTRAP v1 -->
読む順番:
1. docs/birdseye/index.json  …… ノード一覧・隣接関係（軽量）
2. docs/birdseye/caps/<path>.json …… 必要ノードだけ point read（個別カプセル）
3. docs/ROADMAP_AND_SPECS.md …… 要件・仕様の横断導線
4. [third_party/Day8/README.md](third_party/Day8/README.md) …… Day8 資料の総覧（詳細は `docs/day8/README.md`）
5. Day8 オペレーション資料（推奨参照順）: [HUB.codex.md](third_party/Day8/workflow-cookbook/HUB.codex.md)（観測ハブ）→ [GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md)（統制基準）→ [BLUEPRINT.md](third_party/Day8/workflow-cookbook/BLUEPRINT.md)（運用設計）

> `docs/birdseye/hot.json` の `generated_at` は頻出入口リストの生成時刻です。エントリポイントや依存関係を更新した際は `date -u '+%Y-%m-%dT%H:%M:%SZ'` で時刻を取得し、`docs/birdseye/index.json`・`docs/birdseye/caps/`・`docs/birdseye/hot.json` を併せて更新してください。
> 1. `date -u '+%Y-%m-%dT%H:%M:%SZ'` を実行して共通タイムスタンプを取得
> 2. `docs/birdseye/index.json` の `generated_at` と対象ノードの `mtime` を更新
> 3. 更新対象の `docs/birdseye/caps/*.json` と `docs/birdseye/hot.json` に同じ `generated_at` を反映

フォーカス手順:
- 直近変更ファイル±2hopのノードIDを `index.json` から取得
- 対応する `caps/*.json` のみ読み込み

主要導線:
- 要件・仕様ハブ: [`docs/ROADMAP_AND_SPECS.md`](docs/ROADMAP_AND_SPECS.md)
- 詳細要件: [`docs/Katamari_Requirements_v3_ja.md`](docs/Katamari_Requirements_v3_ja.md)
- 機能仕様: [`docs/Katamari_Functional_Spec_v1_ja.md`](docs/Katamari_Functional_Spec_v1_ja.md)
- 技術仕様: [`docs/Katamari_Technical_Spec_v1_ja.md`](docs/Katamari_Technical_Spec_v1_ja.md)
- OpenAPI: [`docs/openapi/katamari_openapi.yaml`](docs/openapi/katamari_openapi.yaml)
- フォーク運用: [`docs/UPSTREAM.md`](docs/UPSTREAM.md), [`docs/FORK_NOTES.md`](docs/FORK_NOTES.md)
- Day8 オペレーション資料: [`third_party/Day8/workflow-cookbook/HUB.codex.md`](third_party/Day8/workflow-cookbook/HUB.codex.md)（観測ハブ）→ [`third_party/Day8/workflow-cookbook/GUARDRAILS.md`](third_party/Day8/workflow-cookbook/GUARDRAILS.md)（統制基準）→ [`third_party/Day8/workflow-cookbook/BLUEPRINT.md`](third_party/Day8/workflow-cookbook/BLUEPRINT.md)（運用設計）
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
- Day8 HUB / Guardrails / Blueprint: `third_party/Day8/workflow-cookbook/HUB.codex.md`, `third_party/Day8/workflow-cookbook/GUARDRAILS.md`, `third_party/Day8/workflow-cookbook/BLUEPRINT.md`

## ローカル起動手順

### 前提インストール

- Python 3.11 系（`python -m venv .venv && source .venv/bin/activate` で仮想環境を推奨）
- 依存パッケージ: `pip install -r requirements.txt`（または `make dev`）

### 起動フロー

1. `.env` を `cp config/env.example .env` で作成し、必要な値を埋める
2. Chainlit を `make run` で起動（デフォルトは `http://localhost:8787`）
   - 依存の再インストールは `make dev` を利用し、アプリ自体は別ターミナルで `make run`
3. 終了は実行ターミナルで `Ctrl + C`

## 環境変数一覧

| 名称 | 必須 | 用途 | 設定例 | 備考 |
| ---- | ---- | ---- | ------ | ---- |
| `OPENAI_API_KEY` | はい | OpenAI プロバイダー利用時の API キー | `OPENAI_API_KEY=sk-...` | `.env` または `config/env.example` を参照 |
| `GOOGLE_GEMINI_API_KEY` | いいえ | Google Gemini プロバイダー利用時の API キー | `GOOGLE_GEMINI_API_KEY=...` | Gemini API を利用する場合のみ |
| `GEMINI_API_KEY` | いいえ | 旧名称。既存デプロイ互換用 | `GEMINI_API_KEY=...` | `config/env.example` に記載 |
| `DEFAULT_PROVIDER` | いいえ | 既定で使用する LLM プロバイダー識別子 | `DEFAULT_PROVIDER=openai` | 省略時は OpenAI |
| `CHAINLIT_AUTH_SECRET` | いいえ（本番推奨） | Chainlit セッション署名用シークレット | `CHAINLIT_AUTH_SECRET=change-me` | 本番は十分な長さに変更 |
| `PORT` | いいえ | `make run` の待ち受けポート | `PORT=8787` | Docker 起動時は `-p <host>:<PORT>` と併用 |
| `LOG_LEVEL` | いいえ | Chainlit ログ出力レベル | `LOG_LEVEL=info` | `debug`/`warning` などを指定可 |
| `SEMANTIC_RETENTION_PROVIDER` | いいえ | 会話保持率メトリクス算出時の埋め込みプロバイダー | `SEMANTIC_RETENTION_PROVIDER=openai` | 集計を無効にする場合は未設定で可 |
| `SEMANTIC_RETENTION_OPENAI_MODEL` | いいえ | OpenAI 埋め込みモデル名 | `SEMANTIC_RETENTION_OPENAI_MODEL=text-embedding-3-large` | OpenAI プロバイダー指定時に利用 |
| `SEMANTIC_RETENTION_GEMINI_MODEL` | いいえ | Google Gemini 埋め込みモデル名 | `SEMANTIC_RETENTION_GEMINI_MODEL=text-embedding-004` | Gemini プロバイダー指定時に利用 |
| `GOOGLE_API_KEY` | いいえ | Gemini 埋め込み生成用 API キー（会話保持率用） | `GOOGLE_API_KEY=...` | `SEMANTIC_RETENTION_PROVIDER=google_gemini` 時に必要 |

> すべての項目は [`config/env.example`](config/env.example) などのサンプルを `.env` にコピーし、必要な値だけ上書きしてください。

## テーマ切り替え

1. Chainlit UI 右上の **Settings → Theme** で `themes/` 配下のプリセット（`.theme.json`）を選択
2. 追加したいテーマ JSON を `themes/` に配置し、UI の **Theme → Import JSON** から読み込む
3. 詳細なカスタマイズやペルソナ連携は [`README_PERSONAS_THEMES.md`](README_PERSONAS_THEMES.md) を参照（JSON の雛形・設定例を掲載）

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

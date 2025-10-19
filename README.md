# Katamari (Chainlit Fork) – 要件&仕様パック

<!-- LLM-BOOTSTRAP v1 -->
読む順番:

1. docs/birdseye/index.json  …… ノード一覧・隣接関係（軽量）
2. docs/birdseye/caps/<path>.json …… 必要ノードだけ point read（個別カプセル）
3. docs/ROADMAP_AND_SPECS.md …… 要件・仕様の横断導線
4. [third_party/Day8/README.md](third_party/Day8/README.md) …… Day8 資料の総覧（詳細は `docs/day8/README.md`）
5. Day8 系資料の推奨読書順: [HUB.codex.md](third_party/Day8/workflow-cookbook/HUB.codex.md) → [GUARDRAILS.md](third_party/Day8/workflow-cookbook/GUARDRAILS.md) → [BLUEPRINT.md](third_party/Day8/workflow-cookbook/BLUEPRINT.md)

> `docs/birdseye/hot.json` の `generated_at` は頻出入口リストの生成時刻です。エントリポイントや依存関係を更新した際は `date -u '+%Y-%m-%dT%H:%M:%SZ'` で時刻を取得し、`docs/birdseye/index.json`・`docs/birdseye/caps/`・`docs/birdseye/hot.json` を併せて更新してください。

フォーカス手順:

- 直近変更ファイル±2hopのノードIDを index.json から取得
- 対応する caps/*.json のみ読み込み

主要導線:

- 要件: [`docs/Katamari_Requirements_v3_ja.md`](docs/Katamari_Requirements_v3_ja.md)
- 機能仕様: [`docs/Katamari_Functional_Spec_v1_ja.md`](docs/Katamari_Functional_Spec_v1_ja.md)
- 技術仕様: [`docs/Katamari_Technical_Spec_v1_ja.md`](docs/Katamari_Technical_Spec_v1_ja.md)
- OpenAPI: [`docs/openapi/katamari_openapi.yaml`](docs/openapi/katamari_openapi.yaml)
- フォーク運用: [`docs/UPSTREAM.md`](docs/UPSTREAM.md), [`docs/FORK_NOTES.md`](docs/FORK_NOTES.md)
- Day8 系資料: [`third_party/Day8/workflow-cookbook/HUB.codex.md`](third_party/Day8/workflow-cookbook/HUB.codex.md) → [`third_party/Day8/workflow-cookbook/GUARDRAILS.md`](third_party/Day8/workflow-cookbook/GUARDRAILS.md) → [`third_party/Day8/workflow-cookbook/BLUEPRINT.md`](third_party/Day8/workflow-cookbook/BLUEPRINT.md)
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

1. Python 3.11 系を用意し、必要なら仮想環境を作成: `python -m venv .venv && source .venv/bin/activate`
2. 依存パッケージを初期化: `pip install -r requirements.txt` または `make dev`
3. アプリ起動: `make run`（`http://localhost:8787` で UI が開きます）
   - ホットリロード付きで開発する場合は、`make dev` 実行後に別ターミナルで `make run`
4. 停止: 実行中のターミナルで `Ctrl + C`

## 環境変数一覧

| 名称 | 必須 | 用途 | 設定例 |
| ---- | ---- | ---- | ------ |
| `OPENAI_API_KEY` | はい | OpenAI プロバイダー利用時の API キー | `OPENAI_API_KEY=sk-...` |
| `GOOGLE_GEMINI_API_KEY` | いいえ | Google Gemini プロバイダー利用時の API キー | `GOOGLE_GEMINI_API_KEY=...` |
| `DEFAULT_PROVIDER` | いいえ | 既定で使用する LLM プロバイダー識別子 | `DEFAULT_PROVIDER=openai` |
| `CHAINLIT_AUTH_SECRET` | いいえ（本番推奨） | Chainlit セッション署名用シークレット | `CHAINLIT_AUTH_SECRET=change-me` |
| `PORT` | いいえ | `make run` の待ち受けポート | `PORT=8787` |
| `LOG_LEVEL` | いいえ | Chainlit ログ出力レベル | `LOG_LEVEL=info` |
| `SEMANTIC_RETENTION_PROVIDER` | いいえ | 会話保持率メトリクス算出時の埋め込みプロバイダー | `SEMANTIC_RETENTION_PROVIDER=openai` |
| `SEMANTIC_RETENTION_OPENAI_MODEL` | いいえ | OpenAI 埋め込みモデル名 | `SEMANTIC_RETENTION_OPENAI_MODEL=text-embedding-3-large` |
| `SEMANTIC_RETENTION_GEMINI_MODEL` | いいえ | Google Gemini 埋め込みモデル名 | `SEMANTIC_RETENTION_GEMINI_MODEL=text-embedding-004` |
| `GOOGLE_API_KEY` | いいえ | Gemini 埋め込み生成用 API キー（会話保持率用） | `GOOGLE_API_KEY=...` |

> すべての項目は `config/env.example` を参照して `.env` にコピーできます。`.env` は Chainlit 実行時に自動読み込みされます。

## テーマ切り替え

1. Chainlit UI 右上の **Settings → Theme** からプリセット名を選択（`themes/` 配下の `.theme.json` と一致）。
2. 新規テーマを追加する場合は、`themes/` に JSON を配置し、UI のテーマ一覧を再読み込み。
   - UI からテーマをインポートする場合は、設定画面の **Theme → Import JSON** からファイルをアップロード。
   - 既存プリセットとカスタマイズ手順は [`themes/CATALOG.md`](themes/CATALOG.md) および [`README_PERSONAS_THEMES.md`](README_PERSONAS_THEMES.md) を参照。

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
2. 記法は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) を踏襲し、セマンティックバージョンと日付を付ける。
3. README やロードマップに散在する履歴は、該当リリースの見出しへ移管し、`docs/Release_Checklist.md` と併せて公開する。

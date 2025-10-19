# Katamari (Chainlit Fork) – 要件&仕様パック

## ローカル起動手順

1. 依存パッケージを初期化: `pip install -r requirements.txt`
2. アプリ起動: `make run`（`http://localhost:8787` で UI が開きます）
   - ホットリロード付きで開発する場合は `make dev` を先に実行して依存を揃えた後、別ターミナルで `make run`
3. 停止: 実行中のターミナルで `Ctrl + C`

## 環境変数一覧

| 名称 | 必須 | 用途 | 設定例 |
| ---- | ---- | ---- | ------ |
| `OPENAI_API_KEY` | はい | OpenAI プロバイダー利用時の API キー | `OPENAI_API_KEY=sk-...` |
| `GEMINI_API_KEY` | いいえ | Google Gemini プロバイダー利用時の API キー | `GEMINI_API_KEY=...` |
| `DEFAULT_PROVIDER` | いいえ | 既定で使用する LLM プロバイダー識別子 | `DEFAULT_PROVIDER=openai` |
| `CHAINLIT_AUTH_SECRET` | いいえ（本番推奨） | Chainlit セッション署名用シークレット | `CHAINLIT_AUTH_SECRET=change-me` |
| `PORT` | いいえ | `make run` の待ち受けポート | `PORT=8787` |
| `LOG_LEVEL` | いいえ | Chainlit ログ出力レベル | `LOG_LEVEL=info` |

> すべての項目は `config/env.example` を参照して `.env` にコピーできます。

## テーマ切り替え

1. Chainlit UI 右上の **Settings → Theme** からプリセット名を選択（`themes/` 配下の `.theme.json` と一致）。
2. 新規テーマを追加する場合は、`themes/` に JSON を配置し、UI のテーマ一覧を再読み込み。
   - 既存プリセットの一覧は [`themes/CATALOG.md`](themes/CATALOG.md) を参照。

- 本パックは「katamari」の要件定義・機能仕様・技術仕様・OpenAPI・初期設定を含むドキュメント集です。
- まずは `docs/Katamari_Requirements_v3_ja.md` をご確認ください。

## 同梱物
- 要件: `docs/Katamari_Requirements_v3_ja.md`
- 機能仕様: `docs/Katamari_Functional_Spec_v1_ja.md`
- 技術仕様: `docs/Katamari_Technical_Spec_v1_ja.md`
- ロードマップ & 仕様索引: `docs/ROADMAP_AND_SPECS.md`
- OpenAPI: `docs/openapi/katamari_openapi.yaml`
- 設定: `config/model_registry.json`, `config/env.example`
- フォーク運用: `docs/UPSTREAM.md`, `docs/FORK_NOTES.md`
- ADR: `docs/adr/README.md`

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

- 変更をマージする前に、該当差分を [`CHANGELOG.md`](CHANGELOG.md) の `[Unreleased]` セクションへ追記してください。
- 記法は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) に従い、日付とセマンティックバージョンを付与します。
- リリース確定時は `[Unreleased]` から新しいバージョン見出しへ移し、`docs/Release_Checklist.md` の手順と合わせて履歴を公開します。

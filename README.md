# Katamari (Chainlit Fork) – 要件&仕様パック
- 本パックは「katamari」の要件定義・機能仕様・技術仕様・OpenAPI・初期設定を含むドキュメント集です。
- まずは `docs/Katamari_Requirements_v3_ja.md` をご確認ください。

## 同梱物
- 要件: `docs/Katamari_Requirements_v3_ja.md`
- 機能仕様: `docs/Katamari_Functional_Spec_v1_ja.md`
- 技術仕様: `docs/Katamari_Technical_Spec_v1_ja.md`
- OpenAPI: `docs/openapi/katamari_openapi.yaml`
- 設定: `config/model_registry.json`, `config/env.example`
- フォーク運用: `docs/UPSTREAM.md`, `docs/FORK_NOTES.md`

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

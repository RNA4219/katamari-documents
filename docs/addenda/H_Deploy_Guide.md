# 付録H: デプロイガイド（簡易）
**Status: 2025-10-19 JST**

## H-1. 開発
```bash
pip install chainlit openai pyyaml tiktoken
export OPENAI_API_KEY=sk-...
export GEMINI_API_KEY=...
chainlit run src/app.py --host 0.0.0.0 --port 8787
```

## H-2. Docker（M3）
```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT=8787
EXPOSE 8787
ENTRYPOINT ["chainlit","run"]
CMD ["src/app.py","--host","0.0.0.0","--port","8787"]
```

## H-3. GitHub Actions リリースワークフロー（M3）
- ファイル: `.github/workflows/release.yml`
- トリガー: `v*.*.*` 形式のタグに対する `push`
- 処理内容:
  1. `docker/setup-buildx-action@v3` で Buildx をセットアップ
  2. `docker/login-action@v3` で `ghcr.io` に `GITHUB_TOKEN` を用いてログイン
  3. `docker/build-push-action@v6` で `ghcr.io/<owner>/<repo>:latest` とタグ名の 2 つを push

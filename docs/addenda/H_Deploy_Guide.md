# 付録H: デプロイガイド（簡易）
**Status: 2025-10-19 JST**

## H-1. 開発
```bash
pip install chainlit openai pyyaml tiktoken
export OPENAI_API_KEY=sk-...
export GEMINI_API_KEY=...
chainlit run app.py -h --host 0.0.0.0 --port 8787
```

## H-2. Docker（M3）
```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT=8787
EXPOSE 8787
CMD ["chainlit","run","app.py","-h","--host","0.0.0.0","--port","8787"]
```

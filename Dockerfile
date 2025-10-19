
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=8787
EXPOSE 8787
CMD ["chainlit","run","src/app.py","-h","--host","0.0.0.0","--port","8787"]

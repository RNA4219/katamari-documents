# TASK.2025-10-19-0001

## 概要
- **CI 整備（lint/type/test/publish）** — Roadmap 優先度 #2 に従い、ruff・mypy --strict・pytest・node:test を自動実行し、Docker イメージ公開を可能にする。

## 目的
- Pull Request ごとにスタイル/型/テストが自動検証されるパイプラインを提供する。
- リリースタグで GHCR へ署名付きイメージを発行し、Release/Security Checklist と連動できる状態にする。

## 要件
- `.github/workflows/ci.yml` を新規作成し、ruff、mypy --strict、pytest、node:test を個別ジョブで実行する。
- Provider 統合テストは Secrets 存在時のみ有効化し、未設定時はスキップとして扱う。
- リリース用ワークフローで Buildx による Docker ビルドと GHCR への push、`vX.Y.Z-katamari` タグ付けを行う。

## 確認コマンド
- `ruff check .`
- `mypy --strict src tests`
- `pytest`
- `node --test`

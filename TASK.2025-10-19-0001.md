# TASK.2025-10-19-0001

## 概要
- **CI 整備（lint/type/test/publish）** — Roadmap 優先度 #2 に基づき、lint・テスト・イメージ公開を自動化する初期整備を行う。[ロードマップ & 仕様ハブ](docs/ROADMAP_AND_SPECS.md)。

## 背景
- 現状 `.github/workflows/` に統合 CI は存在しないため、`ruff`・`mypy --strict`・`pytest`・`node:test` を定常実行する仕組みを構築し、Secrets 依存の統合テストは条件付きにする必要がある。[ロードマップ & 仕様ハブ](docs/ROADMAP_AND_SPECS.md)。
- リリース時に Docker イメージを GHCR へ公開するワークフローも Roadmap に記載されており、同一タスクでの雛形化が望ましい。[付録H: デプロイガイド](docs/addenda/H_Deploy_Guide.md)、[付録M: バージョニング & リリース](docs/addenda/M_Versioning_Release.md)。

## 実行ステップ
1. `.github/workflows/ci.yml` を新規作成し、lint（ruff）、型チェック（mypy --strict）、pytest、node:test をジョブ分割で実行する。Secrets が存在するときのみ Provider 統合テストを追加する条件分岐を入れる。[ロードマップ & 仕様ハブ](docs/ROADMAP_AND_SPECS.md)。
2. Docker ビルドと GHCR への push を行う `release` ワークフローの雛形を作成し、タグ push トリガーと Buildx/ログイン/ビルド手順を定義する。[付録H: デプロイガイド](docs/addenda/H_Deploy_Guide.md)。
3. `Release Checklist`・`Security Review Checklist` の項目を CI の結果に紐付け、リリース前に結果を確認できるようドキュメントへリンクする。[Release Checklist](docs/Release_Checklist.md)、[Security Review Checklist](docs/Security_Review_Checklist.md)。

## 成果物 / 検証
- CI 実行ログで lint・型・テストが成功していること、条件付き統合テストが Secrets 不在でもスキップ扱いになることを確認する。
- Docker イメージが GHCR に push され、バージョンタグが `vX.Y.Z-katamari` 形式で管理されていることを release ワークフローで検証する。[付録M: バージョニング & リリース](docs/addenda/M_Versioning_Release.md)。

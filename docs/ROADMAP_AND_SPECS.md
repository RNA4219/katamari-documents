# Katamari ロードマップ & 仕様書インデックス

本ドキュメントは、リポジトリ内に散在する Markdown/ソース構成を横断的に参照できるようにする統合ハブです。優先タスク、仕様書、実装領域の対応関係をここから辿れます。

## 1. 上位ドキュメントの索引

| 区分 | ファイル | 目的 / 主な内容 |
| --- | --- | --- |
| ビジョン・要件 | `docs/Katamari_Requirements_v3_ja.md` | 対象ユーザー、価値、非機能要件、M1〜M3の到達目標。 |
| 機能仕様 | `docs/Katamari_Functional_Spec_v1_ja.md` | ユースケース別フロー、画面要素、チェーン挙動。 |
| 技術仕様 | `docs/Katamari_Technical_Spec_v1_ja.md` | システム構成、API、データフロー、例外ハンドリング方針。 |
| OpenAPI | `docs/openapi/katamari_openapi.yaml` | HTTP インターフェース定義 (`/metrics`, `/healthz` 予定含む)。 |
| 追加リファレンス | `docs/addenda/*.md` | UI モック、プロバイダ比較、テストケース、構成ファイル解説など。 |
| フォーク運用 | `docs/UPSTREAM.md`, `docs/FORK_NOTES.md`<br>[ADR #0001](adr/0001-use-chainlit-subtree.md) | Chainlit subtree の取得・差分吸収手順。 |
| リリース & セキュリティ | `docs/Release_Checklist.md`, `docs/Security_Review_Checklist.md` | 品質ゲートとリリース判定項目。 |
| Guardrails 連動ドキュメント | `BLUEPRINT.md`, `RUNBOOK.md`, `EVALUATION.md`, `CHECKLISTS.md`, `TASK.*.md` | Guardrails フローに沿った設計・運用・評価・追跡の基盤文書。 |
| Day8 HUB / Guardrails | `third_party/Day8/workflow-cookbook/HUB.codex.md` / `third_party/Day8/workflow-cookbook/GUARDRAILS.md` | Day8 オペレーションの入口（HUB）と統制基準（Guardrails）を横断確認できるセット。 |
| Day8 Blueprint | `third_party/Day8/workflow-cookbook/BLUEPRINT.md` | Guardrails を適用した運用ブループリント（実装設計）。 |

## 2. 実装モジュールと対応仕様

| 実装ディレクトリ | 主担当機能 | 関連仕様 / 参考資料 |
| --- | --- | --- |
| `src/app.py` | Chainlit アプリ本体、ステップ実行、UI 設定。 | 技術仕様 3章、`addenda/B_UI_Mock.md`、`addenda/J_Runbook.md` |
| `src/core_ext/` | トリミング、ペルソナ解析、マルチステップ制御などの拡張。 | `addenda/D_Trim_Design.md`<br>`addenda/C_Persona_Schema.md`<br>[ADR #0002](adr/0002-tokenization-with-tiktoken.md) |
| `src/providers/` | OpenAI/Gemini など LLM プロバイダ抽象化。 | `addenda/F_Provider_Matrix.md`<br>[ADR #0003](adr/0003-provider-interface.md) |
| `themes/` | Chainlit テーマ JSON。 | `README_PERSONAS_THEMES.md`<br>`addenda/B_UI_Mock.md` |
| `tests/` | Pytest ベースの検証群。 | `docs/I_Test_Cases.md` |
| `config/` | モデル登録、環境変数サンプル。 | `docs/L_Config_Reference.md` |

## 3. ロードマップ（推奨進行順）

1. **ドキュメント整備**  
   - [`LICENSE`](../LICENSE) を Apache-2.0 に更新し [`NOTICE`](../NOTICE) を追加。
   - `docs/UPSTREAM.md` に subtree 運用手順を追記。  
   - `README.md` を起動手順・ENV・テーマ説明付きに拡充。  
   - `CONTRIBUTING.md` / `CODE_OF_CONDUCT.md` / `CODEOWNERS` を最終化。  
   - `.gitattributes` で改行統一。  
   - `docs/adr/` にテンプレート ([ADR #0000](adr/0000-template.md)) と初期3件（[ADR #0001](adr/0001-use-chainlit-subtree.md) / [ADR #0002](adr/0002-tokenization-with-tiktoken.md) / [ADR #0003](adr/0003-provider-interface.md)）を整備し、最新状態を維持（追加・更新フローは [CONTRIBUTING.md#ADR を追加・更新する手順](../CONTRIBUTING.md#adr-を追加・更新する手順) を参照）。
   - M1〜M2.5 向け ADR + DoD を整理。

2. **CI・自動化基盤**  
   - `.github/workflows/ci.yml` で lint (ruff), test (pytest), audit (pip-audit) を条件付き実行化。  
   - Secrets がある場合のみプロバイダ統合テストを実行。  
   - `.github/workflows/release.yml` でタグ push 時に GHCR へ Docker イメージを公開。

3. **実装フェーズ**  
   - `context_trimmer` を `tiktoken` ベースへ置換（±5% 精度）。  
   - `semantic_retention` 指標を実装し UI / メトリクスへ露出。  
   - `/metrics` / `/healthz` エンドポイントを追加。  
   - Gemini Provider（stream 対応）を実装。  
   - 以降、OAuth・評価 UI・Prompt evolution など M2 系機能へ拡張。

## 4. 参照クイックリンク

- 実装開始時は `CONTRIBUTING.md` と `CODE_OF_CONDUCT.md` を必読。
- テスト駆動で進める場合は `tests/` を先に追加し、`I_Test_Cases.md` を参照。
- Subtree 同期は `docs/UPSTREAM.md` → `scripts/` の補助スクリプトを活用。
- アーキテクチャ判断は `docs/adr/README.md` と各 ADR（例: [ADR #0001](adr/0001-use-chainlit-subtree.md) / [ADR #0002](adr/0002-tokenization-with-tiktoken.md) / [ADR #0003](adr/0003-provider-interface.md)）を参照。
- 運用時のチェックは `Release_Checklist.md` と `Security_Review_Checklist.md` を使用。
- Day8 系資料の推奨参照順: `third_party/Day8/workflow-cookbook/HUB.codex.md`（観測ハブ）→ `third_party/Day8/workflow-cookbook/GUARDRAILS.md`（統制基準）→ `third_party/Day8/workflow-cookbook/BLUEPRINT.md`（運用設計）。
- Birdseye 図 (`docs/birdseye/index.json`, `docs/birdseye/caps/`, `docs/birdseye/hot.json`) はエントリポイントや依存関係を更新した際に同時更新する。更新手順: (1) 主要ノードとエッジを `index.json` に追記、(2) 代表ノードごとの Capsule を `caps/` 配下で整備（`summary`/`role`/`deps`/`tests` を最新化）、(3) 頻出入口を `hot.json` に列挙し理由を明記、(4) 本手順を守った最終更新日時を `generated_at` に記録する。
- CHANGELOG 更新手順: [`README.md#変更履歴の更新ルール`](../README.md#%E5%A4%89%E6%9B%B4%E5%B1%A5%E6%AD%B4%E3%81%AE%E6%9B%B4%E6%96%B0%E3%83%AB%E3%83%BC%E3%83%AB)。

本ハブは開発フェーズ毎に更新し、未作成 ADR や追加仕様が発生した際は本書内のロードマップを最新化してください。

## 5. Guardrails ドキュメント更新フロー

1. 変更検討時は `BLUEPRINT.md` を起点に目的・スコープ・I/O・AC を見直し、必要な設計更新をドラフト化する。
2. 実装・運用手順の変更は `RUNBOOK.md` と `CHECKLISTS.md` に反映し、ガードレール順序（準備→実行→検証 / Dev→PR→Release→Ops）を維持する。
3. 受入条件や計測指標の更新は `EVALUATION.md` へ同期し、未完了項目は `TASK.<YYYY-MM-DD>-0001.md` など Task Seed へ記録する。
4. 更新を確定したら本ドキュメントの対象セクションを修正し、Birdseye 図および関連 ADR との整合を確認する。

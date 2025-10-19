# EVALUATION

## 機能
- Settings を更新すると System メッセージ差し替えとログ出力が即座に行われる。Persona YAML、チェーン種別、Trim 設定の UI 操作を含む。[Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)、[付録I: テストケース集](docs/addenda/I_Test_Cases.md)。
- Trim 実行時に `compress_ratio` が 0.3–0.8 の範囲で表示され、Reflect では `draft→critique→final` の順序でストリーミングされる。[Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)。
- `/healthz`・`/metrics` エンドポイントが稼働し、M1.5 以降で OAuth 認証が有効化される（M1 は Header Auth）。[Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)、[Katamari 技術仕様 v1](docs/Katamari_Technical_Spec_v1_ja.md)。

## 性能
- 初回トークン p95 ≤ 1.0s、UI 反映遅延 ≤ 300ms を維持し、SSE 連続 1 分で切断率 < 1% を確認する。[Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)。
- 主要ユースケース（設定即時反映、Reflect、Trim）で性能劣化がないことを再測定する。[付録I: テストケース集](docs/addenda/I_Test_Cases.md)。

## セキュリティ
- Secrets は ENV のみに配置し、ログに個人情報を残さない。CORS 制限と Rate Limit を適用する。[付録G: セキュリティ & プライバシー指針](docs/addenda/G_Security_Privacy.md)。
- Header Auth / OAuth のフローを通し、OAuth リダイレクト URL を検証する。[付録I: テストケース集](docs/addenda/I_Test_Cases.md)、[Security Review Checklist](docs/Security_Review_Checklist.md)。

## コンプライアンス
- Apache-2.0 ライセンス順守（`LICENSE`・`NOTICE`・変更点）とバージョニングルール（`vX.Y.Z-katamari`）を満たす。[Katamari 要件定義 v3](docs/Katamari_Requirements_v3_ja.md)、[付録M: バージョニング & リリース](docs/addenda/M_Versioning_Release.md)。
- Lint（ruff）、型チェック（mypy/strict）、テスト（pytest / node:test）を CI 上で完了し、Docker イメージをビルドできる状態とする。[ロードマップ & 仕様ハブ](docs/ROADMAP_AND_SPECS.md)、[Release Checklist](docs/Release_Checklist.md)。

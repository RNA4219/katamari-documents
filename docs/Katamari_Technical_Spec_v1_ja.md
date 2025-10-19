# Katamari 技術仕様書 v1
**Status: 2025-10-19 JST / Initial**

## 1. アーキテクチャ
- **Fork**：Chainlit本体（Apache-2.0）最新安定を追従
- **差分**：`app.py`（薄い配線）＋ `core_ext/`（機能群）＋ `providers/`（OpenAI/Gemini）
```
repo
├─ app.py
├─ core_ext/
│  ├─ persona_compiler.py
│  ├─ context_trimmer.py
│  ├─ prethought.py
│  ├─ multistep.py
│  └─ evolve.py
├─ providers/
│  ├─ openai_client.py
│  └─ google_gemini_client.py
└─ docs / config
```

## 2. Provider 抽象
```python
class ProviderClient(Protocol):
    async def stream(self, model: str, messages: list[dict], **opts) -> AsyncIterator[str]: ...
    async def complete(self, model: str, messages: list[dict], **opts) -> str: ...
```
- Thinking系は `reasoning` パラメタ（例：`{"reasoning":{"effort":"medium","parallel":true}}`）

## 3. 前処理
- **Persona**：YAML→System変換。禁則語検査（正規表現リスト）
- **Trim**：最後Nターン保持（M1で保持率推定：埋め込み類似度）
- **Prethought**：`目的/制約/視点/期待` への分解（テンプレプロンプト）

## 4. チェーン制御
- `reflect = ["draft","critique","final"]`
- Step境界で`system`メッセージに段階ヒントを追加（短く・安全に）

## 5. 評価器（M2）
- **BERTScore**：`xlm-roberta-large` 既定（軽量化にfallback用モデルを併設）
- **ROUGE**：`rouge-l`, `rouge-1/2`、日本語は正規化ベースから開始
- **ルール**：語彙一致・構造検査（JSON/Markdown/字数）

## 6. 性能目標
- p95 初回トークン ≤ 1.0s（近接リージョン・*-mini推奨）
- UI反映延滞 ≤ 300ms
- ストリーミング連続 1 分以上（切断率 < 1%）

## 7. セキュリティ
- ENV キーのみ使用、フロント露出なし
- `CHAINLIT_AUTH_SECRET`、CORS制限、Rate Limit、HTTPS

## 8. デプロイ
- dev: `chainlit run app.py -h --host 0.0.0.0 --port 8787`
- prod: Docker/Helm（M3）、リバースプロキシでHTTP/2・Keep-Alive

## 9. 受け入れ試験（抜粋）
- Settings反映・Trim圧縮率・Reflect順序・Header/OAuth・メトリクス出力

# 付録D: Trim（圧縮）設計詳細
**Status: 2025-10-19 JST**

## D-1. 戦略オプション
1) **Sliding Window（M0）**: 最後のNターン保持（計算量O(n)）。実装容易、語彙流失に弱い。  
2) **Semantic Clustering（M1）**: 意味クラスタごと要約→要点を残す（埋め込み＋k-means）。  
3) **Memory/RAG Hybrid（M2.5）**: 永続メモリ（Postgres/ベクトルDB）から関連要点のみ再構成。

## D-2. 保持率推定（M1）
- `semantic_retention = cosine(emb(before), emb(after))`
- 目標: **≥0.85**（ユースケース依存で調整）

## D-3. 制御パラメタ
- `target_tokens`（UIのスライダ 1k–8k）
- `min_turns`（最低保持ターン数）
- `priority_roles`（system/user優先）

## D-4. フィードバック
- UIに `compress_ratio` と `semantic_retention`（M1）を表示。

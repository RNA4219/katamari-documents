
from typing import Dict, List, Tuple

def _count_tokens(text: str) -> int:
    # Rough count: chars/4 fallback; replace with tiktoken if available
    return max(1, len(text)//4)

def trim_messages(messages: List[Dict], target_tokens: int, model: str) -> Tuple[List[Dict], Dict]:
    sys = [m for m in messages if m.get("role") == "system"]
    convo = [m for m in messages if m.get("role") != "system"]
    budget = max(256, target_tokens)
    kept: List[Dict] = []
    total = 0
    for m in reversed(convo):
        t = _count_tokens(m.get("content",""))
        if total + t > budget:
            break
        kept.append(m)
        total += t
    kept.reverse()
    out = (sys[:1] if sys else []) + kept

    original_tokens = sum(_count_tokens(m.get("content","")) for m in messages)
    trimmed_tokens = sum(_count_tokens(m.get("content","")) for m in out)
    ratio = trimmed_tokens / max(1, original_tokens)
    metrics = {"input_tokens": original_tokens, "output_tokens": trimmed_tokens, "compress_ratio": round(ratio,3)}
    return out, metrics

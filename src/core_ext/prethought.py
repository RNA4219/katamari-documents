
def analyze_intent(text: str) -> str:
    # Very naive decomposition; replace with LLM-assisted analyzer if needed.
    lines = []
    lines.append(f"目的: ユーザーの入力を達成する")
    lines.append(f"制約: 安全/簡潔/正確")
    lines.append(f"視点: ユースケースに即した実装志向")
    lines.append(f"期待: 具体・短文・即使える成果物")
    return "\n".join(lines)


from typing import List

CHAINS = {
    "single": ["final"],
    "reflect": ["draft","critique","final"],
}

def get_chain_steps(chain_id: str) -> List[str]:
    return CHAINS.get(chain_id, CHAINS["single"])

def system_hint_for_step(step: str) -> str:
    if step == "draft":
        return "You are in DRAFT phase. Produce a brief candidate answer."
    if step == "critique":
        return "You are in CRITIQUE phase. List issues and propose fixes concisely."
    return "You are in FINAL phase. Provide the best final answer."

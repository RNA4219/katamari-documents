import sys
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import pytest

from core_ext import retention
from core_ext.context_trimmer import trim_messages


def _build_messages(contents: List[str]) -> List[Dict[str, str]]:
    msgs: List[Dict[str, str]] = [{"role": "system", "content": "sys"}]
    roles = ["user", "assistant"]
    for idx, text in enumerate(contents):
        msgs.append({"role": roles[idx % 2], "content": text})
    return msgs


def test_compute_semantic_retention_cosine_similarity():
    before = _build_messages(["alpha", "omega"])
    after = _build_messages(["alpha"])

    def fake_embed(text: str) -> List[float]:
        table = {
            "sys\nalpha\nomega": [1.0, 0.0],
            "sys\nalpha": [0.5, 0.8660254],
        }
        return table[text]

    score = retention.compute_semantic_retention(before, after, embedder=fake_embed)
    assert score == pytest.approx(0.5, rel=1e-3)


def test_trim_messages_retention_toggle(monkeypatch):
    monkeypatch.setenv("SEMANTIC_RETENTION_PROVIDER", "openai")
    calls: List[int] = []
    original_compute = retention.compute_semantic_retention

    def fake_compute(before, after, embedder=None):
        calls.append(1)
        return 0.42

    monkeypatch.setattr(retention, "compute_semantic_retention", fake_compute)

    msgs = _build_messages(["short", "reply", "next"])
    trimmed, metrics = trim_messages(msgs, target_tokens=4096, model="gpt-5")

    assert calls == [1]
    assert metrics["semantic_retention"] == 0.42

    monkeypatch.setattr(retention, "compute_semantic_retention", original_compute)
    monkeypatch.setenv("SEMANTIC_RETENTION_PROVIDER", "none")

    trimmed2, metrics2 = trim_messages(msgs, target_tokens=4096, model="gpt-5")

    assert "semantic_retention" not in metrics2

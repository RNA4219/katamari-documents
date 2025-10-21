"""Structured logging utilities for Katamari inference events."""

from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass, field
from typing import Any, List, Literal, Optional, TypedDict
from uuid import uuid4


class StepLatency(TypedDict):
    """Latency measurement for a single chain step."""

    step: str
    latency_ms: float


@dataclass(slots=True)
class InferenceLogRecord:
    """Dataclass representing a structured inference log entry."""

    status: Literal["success", "failure"]
    model: str
    chain: str
    token_in: int
    token_out: int
    compress_ratio: float
    step_latency_ms: List[StepLatency]
    latency_ms: float
    semantic_retention: Optional[float] = None
    retryable: Optional[bool] = None
    error: Optional[str] = None
    req_id: str = field(default_factory=lambda: str(uuid4()))

    def to_payload(self) -> dict[str, Any]:
        """Convert the dataclass to a JSON-serialisable mapping."""

        payload = asdict(self)
        # Ensure dictionaries contain plain Python types.
        payload["step_latency_ms"] = [dict(item) for item in self.step_latency_ms]
        return payload


class StructuredLogger:
    """Emit structured log records to the Katamari request logger."""

    def __init__(self, *, logger_name: str = "katamari.request") -> None:
        self._logger_name = logger_name

    def emit(self, record: InferenceLogRecord) -> None:
        """Serialise and emit the provided log record."""

        payload = record.to_payload()
        logging.getLogger(self._logger_name).info(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        )

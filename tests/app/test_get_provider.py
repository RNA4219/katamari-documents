"""Tests for the provider factory exposed by :mod:`src.app`."""

from __future__ import annotations

import os
import sys
from importlib import import_module
from pathlib import Path
from types import SimpleNamespace
from typing import Iterator

import pytest


@pytest.fixture()
def app_module(tmp_path) -> Iterator[object]:
    """Import :mod:`src.app` with an isolated Chainlit configuration."""

    app_root = tmp_path / "app"
    app_root.mkdir()
    previous_root = os.environ.get("CHAINLIT_APP_ROOT")
    os.environ["CHAINLIT_APP_ROOT"] = str(app_root)
    project_root = Path(__file__).resolve().parents[2]
    added_paths: list[str] = []
    for path in [project_root, project_root / "src"]:
        if str(path) not in sys.path:
            sys.path.insert(0, str(path))
            added_paths.append(str(path))
    for module_name in [name for name in sys.modules if name.startswith("chainlit")]:
        sys.modules.pop(module_name, None)
    sys.modules.pop("src.app", None)
    module = import_module("src.app")
    yield module
    for module_name in [name for name in sys.modules if name.startswith("chainlit")]:
        sys.modules.pop(module_name, None)
    sys.modules.pop("src.app", None)
    for path in added_paths:
        if path in sys.path:
            sys.path.remove(path)
    if previous_root is None:
        os.environ.pop("CHAINLIT_APP_ROOT", None)
    else:
        os.environ["CHAINLIT_APP_ROOT"] = previous_root


@pytest.fixture()
def stub_openai(monkeypatch):
    """Avoid constructing the real OpenAI client during tests."""

    from providers import openai_client

    class _StubOpenAI:
        def __init__(self, **_):
            self.chat = SimpleNamespace(
                completions=SimpleNamespace(
                    create=lambda **__: SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(content=""),
                                message=SimpleNamespace(content=""),
                            )
                        ]
                    )
                )
            )

    monkeypatch.setattr(openai_client, "AsyncOpenAI", _StubOpenAI)


@pytest.fixture(name="stub_genai")
def fixture_stub_genai(monkeypatch):
    """Provide a stubbed google generative AI module."""

    from providers import google_gemini_client

    stub = SimpleNamespace(
        configure=lambda **_: None,
        GenerativeModel=lambda name: SimpleNamespace(name=name),
    )
    monkeypatch.setattr(google_gemini_client, "_genai", stub, raising=False)
    return google_gemini_client


def test_get_provider_returns_openai_for_gpt_models(app_module, stub_openai):
    provider = app_module.get_provider("gpt-4o-mini")

    from providers.openai_client import OpenAIProvider

    assert isinstance(provider, OpenAIProvider)


def test_get_provider_returns_gemini_for_prefixed_models(app_module, stub_genai):
    provider = app_module.get_provider("gemini-2.5-flash")

    assert isinstance(provider, stub_genai.GoogleGeminiProvider)

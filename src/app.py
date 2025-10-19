
# Katamari (Chainlit Fork) - app.py (skeleton)
# Run (dev):
#   pip install -r requirements.txt
#   export OPENAI_API_KEY=sk-...
#   chainlit run src/app.py -h --host 0.0.0.0 --port 8787

import os
from typing import Dict, List

import chainlit as cl
from chainlit.input_widget import Select, Slider, TextInput, Switch

from core_ext.persona_compiler import compile_persona_yaml
from core_ext.context_trimmer import trim_messages
from core_ext.prethought import analyze_intent
from core_ext.multistep import get_chain_steps, system_hint_for_step
from providers.openai_client import OpenAIProvider

DEFAULT_MODEL = "gpt-5-main"
DEFAULT_CHAIN = "single"

def get_provider(model_id: str):
    # Simple mapping by provider prefix; extend with Gemini etc.
    if model_id.startswith("gpt-"):
        return OpenAIProvider()
    # elif model_id.startswith("gemini-"):
    #     return GoogleGeminiProvider()
    return OpenAIProvider()

@cl.on_chat_start
async def on_start():
    cl.user_session.set("model", os.getenv("DEFAULT_MODEL", DEFAULT_MODEL))
    cl.user_session.set("chain", os.getenv("DEFAULT_CHAIN", DEFAULT_CHAIN))
    cl.user_session.set("trim_tokens", 4096)
    cl.user_session.set("system", "You are a helpful assistant named Katamari.")

    settings = await cl.ChatSettings(
        inputs=[
            Select(id="model", label="Model",
                   values=["gpt-5-main","gpt-5-main-mini","gpt-5-thinking",
                           "gpt-5-thinking-mini","gpt-5-thinking-nano","gpt-5-thinking-pro",
                           "gemini-2.5-pro","gemini-2.5-flash"],
                   initial_index=0),
            Select(id="chain", label="Multi-step Chain", values=["single","reflect"], initial_index=0),
            Slider(id="trim_tokens", label="Trim target tokens", initial=4096, min=1024, max=8192, step=256),
            TextInput(id="persona_yaml", label="Persona YAML", initial="", description="name/style/forbid/notes"),
            Switch(id="show_debug", label="Show debug metrics", initial=False)
        ]
    ).send()

    await apply_settings(settings)

@cl.on_settings_update
async def on_settings_update(settings: Dict):
    await apply_settings(settings)

async def apply_settings(settings: Dict):
    for k in ("model","chain","trim_tokens","show_debug"):
        if k in settings:
            cl.user_session.set(k, settings[k])

    yaml_str = settings.get("persona_yaml","")
    if yaml_str:
        system, issues = compile_persona_yaml(yaml_str)
        cl.user_session.set("system", system)
        if issues:
            await cl.Message(content="\n".join(["[persona issues]"]+issues)).send()

@cl.on_message
async def on_message(message: cl.Message):
    model: str = cl.user_session.get("model") or DEFAULT_MODEL
    chain_id: str = cl.user_session.get("chain") or DEFAULT_CHAIN
    target_tokens: int = int(cl.user_session.get("trim_tokens") or 4096)
    show_debug: bool = bool(cl.user_session.get("show_debug"))

    # 1) Prethought (optional display as a step)
    intent = analyze_intent(message.content)
    if show_debug and intent:
        await cl.Message(content=f"[prethought]\n{intent}").send()

    # 2) Build/trim history
    hist: List[Dict] = cl.user_session.get("history") or []
    system = cl.user_session.get("system") or "You are a helpful assistant named Katamari."
    if not hist or hist[0].get("role") != "system":
        hist = [{"role":"system","content":system}] + hist
    hist.append({"role":"user","content":message.content})

    trimmed, metrics = trim_messages(hist, target_tokens, model)
    cl.user_session.set("history", trimmed)
    if show_debug:
        await cl.Message(content=f"[trim] tokens: {metrics['output_tokens']}/{metrics['input_tokens']} (ratio {metrics['compress_ratio']})").send()

    # 3) Run chain
    provider = get_provider(model)
    steps = get_chain_steps(chain_id)
    for idx, step_name in enumerate(steps, start=1):
        async with cl.Step(name=f"Step {idx}: {step_name}", type="llm", show_input=True) as step:
            step.input = message.content
            msgs = list(trimmed)
            if step_name != "final":
                msgs.append({"role":"system","content": system_hint_for_step(step_name)})
            # Stream
            accum = []
            async for delta in provider.stream(model=model, messages=msgs, temperature=0.7):
                if delta:
                    accum.append(delta)
                    await step.stream_token(delta)
            output = "".join(accum)
            step.output = output
            trimmed.append({"role":"assistant","content":output})
            cl.user_session.set("history", trimmed)

    # Mirror last output as normal message
    if trimmed and trimmed[-1]["role"] == "assistant":
        await cl.Message(content=trimmed[-1]["content"]).send()

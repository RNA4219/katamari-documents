
from src.core_ext.persona_compiler import compile_persona_yaml

def test_persona_default():
    sys, issues = compile_persona_yaml("")
    assert "Katamari" in sys
    assert issues == []

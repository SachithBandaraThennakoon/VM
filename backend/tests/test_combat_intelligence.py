from app.intelligence.core import CombatIntelligenceCore

def test_combat_intelligence():
    core = CombatIntelligenceCore()

    inputs = {
        "balance": "poor",
        "timing": "rushed",
        "tension": "high",
        "intent": "training"
    }

    results = core.evaluate(inputs)

    assert len(results) > 0
    assert any("balance" in r.get("issue", "") for r in results)

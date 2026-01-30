from app.agents.base_agent import BaseAgent
from app.intelligence.core import CombatIntelligenceCore

class IntelligenceAgent(BaseAgent):

    def __init__(self):
        self.core = CombatIntelligenceCore()

    def act(self, context: dict) -> dict:
        signals = context.get("signals", {})
        feedback = self.core.evaluate(signals)

        return {
            "intelligence_feedback": feedback
        }

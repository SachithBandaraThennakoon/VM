from app.intelligence.base import IntelligenceModule

class SpatialIntelligence(IntelligenceModule):

    def evaluate(self, inputs: dict) -> dict:
        balance = inputs.get("balance", "unknown")

        if balance == "poor":
            return {
                "issue": "balance",
                "guidance": "Stability is weak. Focus on grounding and posture."
            }

        return {
            "issue": "balance",
            "guidance": "Balance is stable."
        }

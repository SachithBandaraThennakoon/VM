from app.intelligence.base import IntelligenceModule

class EthicalRestraintIntelligence(IntelligenceModule):

    def evaluate(self, inputs: dict) -> dict:
        intent = inputs.get("intent", "training")

        if intent != "training":
            return {
                "block": True,
                "message": "Training focuses on control and safety, not harm."
            }

        return {
            "block": False
        }

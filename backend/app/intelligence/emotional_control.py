from app.intelligence.base import IntelligenceModule

class EmotionalControlIntelligence(IntelligenceModule):

    def evaluate(self, inputs: dict) -> dict:
        tension = inputs.get("tension", "low")

        if tension == "high":
            return {
                "issue": "tension",
                "guidance": "Release unnecessary tension. Breathe and soften."
            }

        return {
            "issue": "tension",
            "guidance": "Emotional state is calm."
        }

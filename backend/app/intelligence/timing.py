from app.intelligence.base import IntelligenceModule

class TimingIntelligence(IntelligenceModule):

    def evaluate(self, inputs: dict) -> dict:
        timing = inputs.get("timing", "normal")

        if timing == "rushed":
            return {
                "issue": "timing",
                "guidance": "You are moving ahead of your awareness. Slow down."
            }

        return {
            "issue": "timing",
            "guidance": "Timing is controlled."
        }

from app.intelligence.spatial import SpatialIntelligence
from app.intelligence.timing import TimingIntelligence
from app.intelligence.emotional_control import EmotionalControlIntelligence
from app.intelligence.ethics import EthicalRestraintIntelligence

class CombatIntelligenceCore:

    def __init__(self):
        self.modules = [
            EthicalRestraintIntelligence(),
            SpatialIntelligence(),
            TimingIntelligence(),
            EmotionalControlIntelligence()
        ]

    def evaluate(self, inputs: dict) -> list:
        results = []

        for module in self.modules:
            result = module.evaluate(inputs)
            results.append(result)

            if result.get("block"):
                break

        return results

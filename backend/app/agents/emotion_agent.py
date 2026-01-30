from app.agents.base_agent import BaseAgent
from app.emotion.emotion_state import EmotionState

class EmotionAgent(BaseAgent):

    def __init__(self):
        self.state = EmotionState()

    def act(self, context: dict) -> dict:
        self.state.update(context.get("signals", {}))
        return {"emotion": self.state.state}

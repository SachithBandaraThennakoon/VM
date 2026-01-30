from app.agents.base_agent import BaseAgent

class EthicsAgent(BaseAgent):

    def act(self, context: dict) -> dict:
        user_input = context.get("user_input", "")

        unsafe_keywords = ["attack", "hurt", "kill", "fight"]

        if any(word in user_input.lower() for word in unsafe_keywords):
            return {
                "block": True,
                "message": "Training focuses on safety, discipline, and restraint."
            }

        return {"block": False}

from app.agents.base_agent import BaseAgent

class EvaluationAgent(BaseAgent):

    def act(self, context: dict) -> dict:
        response = context.get("response", "")
        return {
            "response_length": len(response),
            "calmness_score": response.count(".")
        }

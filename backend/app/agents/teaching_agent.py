from app.agents.base_agent import BaseAgent
from app.mind.llm_engine import call_master_llm
from app.mind.context_builder import build_context

class TeachingAgent(BaseAgent):

    def act(self, context: dict) -> dict:
        response = call_master_llm(
            user_input=context["user_input"],
            context_prompt=context["prompt_context"]
        )

        return {"response": response}

from app.agents.ethics_agent import EthicsAgent
from app.agents.intelligence_agent import IntelligenceAgent
from app.agents.emotion_agent import EmotionAgent
from app.agents.teaching_agent import TeachingAgent
from app.agents.evaluation_agent import EvaluationAgent
from app.intelligence.formatter import format_intelligence_feedback
from app.emotion.personality import PERSONALITY_RULES


class AgentController:

    def __init__(self):
        self.ethics = EthicsAgent()
        self.intelligence = IntelligenceAgent()
        self.emotion = EmotionAgent()
        self.teacher = TeachingAgent()
        self.evaluator = EvaluationAgent()

    def run(self, context: dict) -> dict:
        ethics_result = self.ethics.act(context)
        if ethics_result.get("block"):
            return {"response": ethics_result["message"]}

        intel_result = self.intelligence.act(context)
        emotion_result = self.emotion.act(context)
        tone_instruction = PERSONALITY_RULES.get(
            emotion_result["emotion"],
            "Remain calm and respectful."
        )

        context["prompt_context"] += f"\n\nTeaching tone:\n{tone_instruction}"



        formatted_intel = format_intelligence_feedback(
            intel_result["intelligence_feedback"]
        )

        context["prompt_context"] += f"\n\nGuidance:\n{formatted_intel}"
        context["prompt_context"] += f"\nTone: {emotion_result['emotion']}"

        teaching_result = self.teacher.act(context)
        evaluation = self.evaluator.act(teaching_result)

        return {
            "response": teaching_result["response"],
            "evaluation": evaluation
        }

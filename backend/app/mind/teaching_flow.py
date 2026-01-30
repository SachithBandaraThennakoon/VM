from app.emotion.emotion_state import EmotionState
from app.mind.context_builder import build_context
from app.mind.llm_engine import call_master_llm

emotion_state = EmotionState()

def generate_teaching_response(
    user_input,
    student,
    session_state,
    retrieved_knowledge,
    intelligence_signals
):
    # Update emotion model
    emotion_state.update(intelligence_signals)

    context = build_context(
        student,
        session_state,
        retrieved_knowledge,
        emotion_state
    )

    response = call_master_llm(
        user_input=user_input,
        context_prompt=context
    )

    session_state.last_feedback = response
    return response

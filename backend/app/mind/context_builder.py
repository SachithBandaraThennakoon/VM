from app.emotion.personality import PERSONALITY_RULES

def build_context(student, session_state, knowledge):
    return f"""
Student level: {student.level}
Current focus: {session_state.current_focus}

Relevant principles:
{knowledge}

Respond as a disciplined martial arts master.
"""

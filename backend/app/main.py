from fastapi import FastAPI
from app.memory.knowledge_store import search
from app.state.state_manager import state


from dotenv import load_dotenv

from app.mind.context_builder import build_context
load_dotenv()


app = FastAPI(title="Virtual Martial Arts Master")

#---------------------------------------
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "VMAI backend running"}

from app.memory.knowledge_loader import load_knowledge

@app.on_event("startup")
def startup_event():
    load_knowledge()


@app.post("/session/start")
def start_session(student_id: int, focus: str):
    state.current_focus = focus
    return {"status": "session started", "focus": focus}

@app.get("/knowledge/search")
def search_knowledge(query: str):
    results = search(query)
    return {"results": results}

#////////////////////////////////////////////////////////////////////////////////////////////////teach/////////////////

from app.mind.teaching_flow import generate_teaching_response
from app.memory.repository import get_student


from app.agents.controller import AgentController

agent_controller = AgentController()

@app.post("/teach")
def teach(user_input: str, student_id: int):
    student = get_student(student_id)

    retrieved = search_knowledge(user_input)
    knowledge_text = "\n".join(retrieved)

    context = {
        "user_input": user_input,
        "signals": {
            "balance": "poor",
            "timing": "rushed",
            "tension": "high",
            "intent": "training"
        },
        "prompt_context": build_context(
            student,
            state,
            knowledge_text
        )

    }

    result = agent_controller.run(context)
    return result


@app.get("/state")
def get_state():
    return {
        "focus": state.current_focus,
        "level": state.student_level,
        "last_feedback": state.last_feedback
    }


from app.memory.database import SessionLocal
from app.memory.models import Student

@app.post("/student/create")
def create_student(
    name: str,
    level: str = "beginner",
    focus_area: str = "balance"
):
    db = SessionLocal()

    student = Student(
        name=name,
        level=level,
        focus_area=focus_area
    )

    db.add(student)
    db.commit()
    db.refresh(student)
    db.close()

    return {
        "id": student.id,
        "name": student.name,
        "level": student.level,
        "focus_area": student.focus_area
    }


# --------------------------------------------------------

from app.api.models import PerceptionPayload

@app.post("/perception/teach")
def teach_with_perception(payload: PerceptionPayload):
    student = get_student(payload.student_id)

    if not student:
        return {"error": "Student not found"}

    knowledge = "\n".join(search_knowledge(payload.user_input))

    context = {
        "user_input": payload.user_input,
        "signals": payload.signals,
        "prompt_context": build_context(
            student=student,
            session_state=state,
            knowledge=knowledge
        )
    }

    result = agent_controller.run(context)
    return result

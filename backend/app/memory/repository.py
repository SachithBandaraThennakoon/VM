from sqlalchemy.orm import Session
from app.memory.database import SessionLocal
from app.memory.models import Student

def get_student(student_id: int) -> Student:
    db: Session = SessionLocal()
    try:
        student = db.query(Student).filter(Student.id == student_id).first()
        return student
    finally:
        db.close()

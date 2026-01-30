from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(String)
    focus_area = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class TrainingSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    topic = Column(String)
    state = Column(String)
    started_at = Column(DateTime, default=datetime.utcnow)

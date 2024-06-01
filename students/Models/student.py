from students.database import Base
from sqlalchemy import Column, Integer, String

class StudentSQL(Base):
    __tablename__ = "students"

    id= Column(Integer, primary_key = True, index=True) 
    name = Column(String)
    age = Column(Integer)
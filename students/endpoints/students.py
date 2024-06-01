from fastapi import Depends
from typing import List
from database import get_session
from students.Models.student import StudentSQL
from students.serializers.student import Student

from sqlalchemy.orm import Session

class StudentsAPI:

    def list_students(self, name: str, age: int, session: Session = Depends(get_session)) -> List[Student]:
        students: List[StudentSQL] = session.query(StudentSQL).filter_by(name=name, age=age)
        return [Student.from_orm(student) for student in students]
    
    def create(self, student: Student, session: Session = Depends(get_session)) -> List[Student]:
        student_sql = StudentSQL(name=student.name, age=student.age)
        session.add(student_sql)
        return Student.from_orm(student_sql)
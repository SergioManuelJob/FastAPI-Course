from fastapi import APIRouter, Depends
from students.endpoints.students import StudentsAPI
from students.serializers.student import Student
from students.dependencies import validate_token
from typing import List

router = APIRouter(prefix="/students", dependencies=[Depends(validate_token)])

student_api = StudentsAPI()

router.add_api_route(path="", endpoint=student_api.list_students, methods=["GET"], response_model=List[Student])
router.add_api_route(path="", endpoint=student_api.create, methods=["POST"], response_model=Student)
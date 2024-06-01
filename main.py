import uvicorn
from fastapi import FastAPI
from students.database import Base, engine
from students.Models.student import StudentSQL
from students.endpoints.routes import router as student_router

from sqlalchemy.orm import Session

app = FastAPI()

app.include_router(router=student_router)

@app.on_event("startup")
def create_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)

# Primera parte del curso
# class PeopleName(str, Enum):
#     JUAN = "JUAN"
#     NADIA = "NADIA"

# PEOPLE = {
#     PeopleName.JUAN: {
#         'age': 23,
#         'name': PeopleName.JUAN.value
#     },
#     PeopleName.NADIA: {
#         'age': 23,
#         'name': PeopleName.NADIA.value
#     }
# }

# @app.get("/", status_code=status.HTTP_200_OK)
# def hello_world():
#     return "Hello World"

# @app.get("/{name}", status_code=status.HTTP_200_OK)
# def hello_world(name: str, param: int = 1) -> Dict[Any, Any]:
#     return {"Parameter": param, "Name": name}

# @app.get("/People/{name}", status_code=status.HTTP_200_OK)
# def validate_person(name: PeopleName = Path(..., title="Name of the person", description= "Name of the person we want to validate"), 
#                     age: int = Query(10, gte=10, le=30, title="Person's Age", description="Person's age we want to find in a query")) -> Dict[str, Any]:
#     return {**PEOPLE[name], "age_valid": PEOPLE[name]['age'] == age}

# @app.get("/student", response_model=List[Student], dependencies=[Depends(validate_token)])
# def list_students(student_filter: StudentFilter = Depends()) -> List[Student]:
#     return [student for student in school.students if StudentFilter(age = student.age, name= student.name) == student_filter]
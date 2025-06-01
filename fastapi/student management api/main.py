from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Student(BaseModel):
    name:str
    age:int
    grade:str


students=[]
student_id_counter = 1

@app.post("/students")
def add_student(student: Student):
    global student_id_counter
    new_student = {"id": student_id_counter, **student.dict()}
    students.append(new_student)
    student_id_counter += 1
    return new_student

@app.get("/students")
def get_students():
    return students

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for s in students:
        if s["id"] == student_id:
            s["name"] = student.name
            s["age"] = student.age
            s["grade"] = student.grade
            return s
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, s in enumerate(students):
        if s["id"] == student_id:
            return students.pop(i)
    raise HTTPException(status_code=404, detail="Student not found")
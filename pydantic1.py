from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI() 

class Student(BaseModel):
    id: int
    name: str
    score: int

students: List[Student] = [
    Student(id=1, name="John", score=30),
    Student(id=2, name="Jack", score=20),
    Student(id=3, name="Jim", score=40),
]

@app.get("/students", response_model=List[Student])
async def get_students(): 
    return students

@app.get("/students/{student_id}", response_model=Student)
async def get_student_by_id(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students", 
          response_model=Student, 
          status_code=status.HTTP_200_OK)
async def create_student(student: Student):
    students.append(student)
    return student

@app.delete("/students/{student_id}", status_code=status.HTTP_200_OK)
async def delete_student_by_id(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)
            return {"message": "Delete student sucessfully", 
                    "data": deleted_student}
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {student_id} not found"
    )

@app.put("/students/{student_id}", status_code=status.HTTP_200_OK)
async def update_student_by_id(student_id: int, updated_student: Student):
    for index, student in enumerate(students) :
        if student.id == student_id :
            students[index] = updated_student
            return { "message" : "Update successfully", "data": updated_student}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Item with ID {student_id} not found"
    )
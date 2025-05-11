from fastapi import FastAPI, HTTPException
from models import Student
from utils import generate_student_id, log_json, validate_input
from eligibility import check_eligibility
from database import init_db, get_connection
import json

app = FastAPI()
init_db()

@app.get("/")
def read_root():
    return {"message": "College Admission Eligibility API is running!"}

@app.post("/check-eligibility/")
def check_eligibility_api(student: Student):
    student_data = student.dict()
    is_valid, message = validate_input(student_data)
    if not is_valid:
        raise HTTPException(status_code=400, detail=message)

    student_id = generate_student_id(student_data['name'])

    conn = get_connection()
    cursor = conn.cursor()

    # Delete existing
    cursor.execute("DELETE FROM students WHERE name=?", (student_data['name'],))

    eligible, result = check_eligibility(student_data)
    student_data['student_id'] = student_id
    student_data['eligibility'] = result
    student_data['timestamp'] = json.dumps(student_data, indent=2)

    # Store in DB
    cursor.execute("""
        INSERT INTO students (student_id, name, age, gender, marks, qualification, course, eligibility, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))
    """, (
        student_id, student_data['name'], student_data['age'], student_data['gender'],
        json.dumps(student_data['marks']), student_data['qualification'], student_data['course'],
        result
    ))
    conn.commit()

    # Log
    log_json(student_data, "input")
    log_json({"student_id": student_id, "eligibility": result}, "output")

    return {
        "student_id": student_id,
        "eligibility": result
    }

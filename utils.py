import re
import uuid
import json
from datetime import datetime

def generate_student_id(name):
    return f"{name[:3].upper()}{uuid.uuid4().hex[:6]}"

def log_json(data, log_type):
    timestamp = datetime.now().isoformat()
    log_file = f"{log_type}_log.json"
    log_entry = {"timestamp": timestamp, "data": data}
    with open(log_file, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def validate_input(data):
    name_pattern = r"^[A-Za-z ]+$"
    course_list = [
        "Computer Science Engineering", "Mechanical Engineering", "Electrical Engineering",
        "Civil Engineering", "Electronics and Communication Engineering",
        "MBBS", "BDS", "BAMS", "BHMS", "BPT",
        "B.Com", "BBA", "BBM", "CA",
        "BA in History", "BA in Psychology", "BA in Sociology", "BA in Political Science", "BA in English"
    ]

    if not re.match(name_pattern, data['name']):
        return False, "Invalid name"
    if not (17 <= data['age'] <= 25):
        return False, "Age must be between 17 and 25"
    if data['gender'] not in ['Male', 'Female', 'Other']:
        return False, "Invalid gender"
    if any(not (0 <= m <= 100) for m in data['marks'].values()):
        return False, "Invalid marks"
    if data['course'] not in course_list:
        return False, "Invalid course"
    return True, ""

# 🎓 College Admission Eligibility Checker

An API + GUI-based Python application to determine eligibility for college admissions based on student demographics, marks, and qualifying exams.

---

## 🔧 Technologies Used

- **Backend**: Python, FastAPI, SQLite
- **Frontend**: Tkinter (GUI)
- **Logic/Validation**: Pandas, NumPy, Regex, Pydantic
- **Packaging**: PyInstaller

---

## 📂 Project Structure

college_admission/
├── app.py # FastAPI server
├── gui_app.py # Tkinter GUI application
├── eligibility.py # Core eligibility logic
├── database.py # SQLite interactions
├── models.py # Pydantic request models
├── utils.py # Helpers: logging, validation, etc.
├── test_cases/ # Sample input JSONs
├── log/ # Input/Output logs
├── requirements.txt # Python dependencies
├── README.md # Project overview
└── student_records.db # Generated SQLite DB
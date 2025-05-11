import numpy as np

def check_eligibility(data):
    course = data['course']
    marks = data['marks']
    subjects = list(marks.keys())
    avg_marks = np.mean(list(marks.values()))
    qualified = data['qualification'].upper()

    def has_subjects(required):
        return all(sub in subjects for sub in required)

    if "Engineering" in course:
        required = ['Physics', 'Chemistry', 'Mathematics']
        if qualified == "JEE" and has_subjects(required):
            cutoffs = {
                "Computer Science Engineering": 75,
                "Mechanical Engineering": 70,
                "Electrical Engineering": 70,
                "Civil Engineering": 65,
                "Electronics and Communication Engineering": 70
            }
            if avg_marks >= cutoffs[course]:
                return True, "Eligible"
    elif course in ["MBBS", "BDS", "BAMS", "BHMS", "BPT"]:
        required = ['Physics', 'Chemistry', 'Biology']
        if qualified == "NEET" and has_subjects(required):
            cutoffs = {
                "MBBS": 85,
                "BDS": 80,
                "BAMS": 75,
                "BHMS": 75,
                "BPT": 70
            }
            if avg_marks >= cutoffs[course]:
                return True, "Eligible"
    elif course in ["B.Com", "BBA", "BBM", "CA"]:
        required = ['Accountancy', 'Business Studies', 'Economics']
        if has_subjects(required):
            return True, "Eligible"
    elif course.startswith("BA"):
        humanities_map = {
            "BA in History": ['History', 'Political Science', 'Geography'],
            "BA in Psychology": ['Psychology', 'Sociology', 'English'],
            "BA in Sociology": ['Sociology', 'Political Science', 'History'],
            "BA in Political Science": ['Political Science', 'History', 'Geography'],
            "BA in English": ['English', 'History', 'Political Science']
        }
        if has_subjects(humanities_map[course]):
            return True, "Eligible"

    return False, suggest_alternatives(subjects, qualified, avg_marks)

def suggest_alternatives(subjects, qualified, avg_marks):
    # A basic suggestion logic
    if set(subjects) >= {'Physics', 'Chemistry', 'Mathematics'}:
        return "Try Civil or Mechanical Engineering"
    elif set(subjects) >= {'Physics', 'Chemistry', 'Biology'}:
        return "Try BPT or BHMS"
    elif set(subjects) >= {'Accountancy', 'Business Studies', 'Economics'}:
        return "Try BBA or B.Com"
    else:
        return "Consider BA in Humanities courses"

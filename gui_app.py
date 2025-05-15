import tkinter as tk
from tkinter import messagebox, ttk
import requests
import json

API_URL = "http://127.0.0.1:8000/check-eligibility/"

class EligibilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 College Admission Eligibility Checker")
        self.root.geometry("600x720")
        self.root.configure(bg="#f0f4f7")

        self.fields = {}
        self.subject_entries = {}

        # Heading
        heading = tk.Label(root, text="College Admission Eligibility Checker",
                           font=("Helvetica", 16, "bold"), bg="#f0f4f7", fg="#2c3e50")
        heading.pack(pady=15)

        # Frame for inputs
        form_frame = tk.Frame(root, bg="#f0f4f7")
        form_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.create_label_entry(form_frame, "Name")
        self.create_label_entry(form_frame, "Age")
        self.create_label_dropdown(form_frame, "Gender", ["Male", "Female", "Other"])
        self.create_label_dropdown(form_frame, "Qualification", ["JEE", "NEET", "12th"])
        self.create_label_dropdown(form_frame, "Desired Course", [
            "Computer Science Engineering", "Mechanical Engineering", "Electrical Engineering",
            "Civil Engineering", "Electronics and Communication Engineering",
            "MBBS", "BDS", "BAMS", "BHMS", "BPT",
            "B.Com", "BBA", "BBM", "CA",
            "BA in History", "BA in Psychology", "BA in Sociology", "BA in Political Science", "BA in English"
        ])

        # Subjects
        subject_label = tk.Label(form_frame, text="Subjects and Marks (0–100):", font=("Helvetica", 12, "bold"), bg="#f0f4f7")
        subject_label.pack(pady=(15, 5))

        subject_frame = tk.Frame(form_frame, bg="#f0f4f7")
        subject_frame.pack(pady=5)

        default_subjects = ["Physics", "Chemistry", "Mathematics", "Biology", "English", "Economics"]
        for subject in default_subjects:
            self.create_subject_mark_entry(subject_frame, subject)

        # Submit button
        submit_btn = tk.Button(root, text="Submit", font=("Helvetica", 12, "bold"),
                               bg="#2980b9", fg="white", padx=20, pady=10,
                               command=self.submit)
        submit_btn.pack(pady=20)

    def create_label_entry(self, parent, label):
        tk.Label(parent, text=label, bg="#f0f4f7", anchor='w', font=("Helvetica", 10)).pack(fill='x')
        entry = tk.Entry(parent, font=("Helvetica", 10))
        entry.pack(fill='x', pady=3)
        self.fields[label] = entry

    def create_label_dropdown(self, parent, label, options):
        tk.Label(parent, text=label, bg="#f0f4f7", anchor='w', font=("Helvetica", 10)).pack(fill='x')
        var = tk.StringVar(value=options[0])
        dropdown = ttk.Combobox(parent, textvariable=var, values=options, state="readonly", font=("Helvetica", 10))
        dropdown.pack(fill='x', pady=3)
        self.fields[label] = var

    def create_subject_mark_entry(self, parent, subject):
        row = tk.Frame(parent, bg="#f0f4f7")
        row.pack(fill='x', pady=2)

        tk.Label(row, text=subject + ":", width=15, anchor='w', bg="#f0f4f7").pack(side='left')
        entry = tk.Entry(row, width=10)
        entry.insert(0, "80")
        entry.pack(side='left')
        self.subject_entries[subject] = entry

    def submit(self):
        try:
            name = self.fields["Name"].get().strip()
            age = int(self.fields["Age"].get())
            gender = self.fields["Gender"].get()
            qualification = self.fields["Qualification"].get()
            course = self.fields["Desired Course"].get()

            marks = {}
            for subject, entry in self.subject_entries.items():
                val = entry.get().strip()
                if val == "":
                    continue
                marks[subject] = int(val)

            payload = {
                "name": name,
                "age": age,
                "gender": gender,
                "qualification": qualification,
                "marks": marks,
                "course": course
            }

            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                result = response.json()
                messagebox.showinfo("✅ Eligibility Result", json.dumps(result, indent=4))
            else:
                error = response.json()
                messagebox.showerror("❌ Invalid Input", json.dumps(error, indent=4))

        except Exception as e:
            messagebox.showerror("🚨 Error", f"Something went wrong:\n{str(e)}")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = EligibilityApp(root)
    root.mainloop()

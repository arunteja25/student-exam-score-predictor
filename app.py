import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import tkinter as tk

data = pd.read_csv("student_habits_performance.csv")

X = data[['study_hours_per_day', 'attendance_percentage', 'sleep_hours', 'mental_health_rating']]
y = data['exam_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

def predict_score():
    study = float(study_entry.get())
    attendance = float(attendance_entry.get())
    sleep = float(sleep_entry.get())
    mental = float(mental_entry.get())

    prediction = model.predict([[study, attendance, sleep, mental]])
    result_label.config(text=f"Predicted Exam Score: {round(prediction[0], 2)}")

root = tk.Tk()
root.title("Student Exam Score Predictor")
root.geometry("450x420")
root.configure(bg="#1e1e1e")

tk.Label(root, text="Student Exam Score Predictor",
         font=("Arial", 18, "bold"),
         bg="#1e1e1e", fg="white").pack(pady=15)

def make_label(text):
    tk.Label(root, text=text,
             font=("Arial", 11),
             bg="#1e1e1e", fg="white").pack()

def make_entry():
    entry = tk.Entry(root, font=("Arial", 12), width=25)
    entry.pack(pady=5)
    return entry

make_label("Study Hours Per Day")
study_entry = make_entry()

make_label("Attendance Percentage")
attendance_entry = make_entry()

make_label("Sleep Hours")
sleep_entry = make_entry()

make_label("Mental Health Rating (1-10)")
mental_entry = make_entry()

tk.Button(root, text="Predict Score",
          command=predict_score,
          font=("Arial", 12, "bold"),
          bg="#00c853", fg="white",
          width=15).pack(pady=20)

result_label = tk.Label(root, text="",
                        font=("Arial", 14, "bold"),
                        bg="#1e1e1e", fg="#00e676")
result_label.pack()

root.mainloop()
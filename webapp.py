from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset
data = pd.read_csv("student_habits_performance.csv")

X = data[['study_hours_per_day',
          'attendance_percentage',
          'sleep_hours',
          'mental_health_rating']]

y = data['exam_score']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        study = float(request.form["study"])
        attendance = float(request.form["attendance"])
        sleep = float(request.form["sleep"])
        mental = float(request.form["mental"])

        result = model.predict([[study, attendance, sleep, mental]])

        prediction = round(result[0], 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
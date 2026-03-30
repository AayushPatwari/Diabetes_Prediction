from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import sqlite3

app = Flask(__name__)

print("Loading model...")
model = joblib.load("model/diabetes_model.pkl")
print("Model loaded")

def get_db():
    return sqlite3.connect("diabetes.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    print("Predict API called")

    try:
        data = request.get_json()
        print("Received data:", data)

        features = np.array([[
            float(data["pregnancies"]),
            float(data["glucose"]),
            float(data["bloodpressure"]),
            float(data["skin"]),
            float(data["insulin"]),
            float(data["bmi"]),
            float(data["dpf"]),
            float(data["age"])
        ]])

        print("Features:", features)

        prediction = model.predict(features)[0]
        result = "Diabetic" if prediction == 1 else "Non-Diabetic"

        conn = get_db()
        conn.execute(
            "INSERT INTO records VALUES (NULL,?,?,?,?,?,?,?,?,?)",
            (*features[0], result)
        )
        conn.commit()
        conn.close()

        print("Prediction:", result)

        return jsonify({"prediction": result})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

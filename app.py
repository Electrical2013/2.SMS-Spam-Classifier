from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load your model/vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    vect = vectorizer.transform([message])
    prediction = model.predict(vect)[0]

    label_map = {0: "HAM", 1: "SPAM"}  # Adjust if your encoder is reversed
    return render_template("index.html",
                           prediction_text=f"Message is: {label_map[prediction]}")

if __name__ == "__main__":
    app.run(debug=True)

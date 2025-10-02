# 📩 SMS Spam Classifier 🚀

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-green?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/ScikitLearn-ML-orange?logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

A simple **SMS Spam Classifier** built with **Machine Learning (Scikit-Learn)** and deployed using **Flask** 🌐.  
The app predicts whether a given SMS message is **SPAM 🚨** or **HAM ✅** (not spam).

---

## 📂 Project Structure

📦 SMS-Spam-Classifier
├── app.py # Flask web app
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF/Count vectorizer
├── spam.xlsx # Dataset (Excel format)
├── SMS Spam Classifier.ipynb # Jupyter Notebook (model training)
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── templates/
│ └── index.html # Frontend HTML page



---

## ⚙️ Installation & Setup  

🔹 **Step 1: Clone Repository**  
```bash
git clone https://github.com/your-username/sms-spam-classifier.git
cd sms-spam-classifier

🔹 Step 2: Create Virtual Environment (Recommended)

python -m venv venv
# Activate it
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


🔹 Step 3: Install Requirements

pip install -r requirements.txt


🔹 Step 4: Run App

python app.py


🔹 Step 5: Open Browser
👉 http://127.0.0.1:5000/

🖼️ Example

Input:

Congratulations! You have won a free ticket to Bahamas. Reply WIN to claim.


Output:

Message is: 🚨 SPAM

🛠️ Tech Stack

🐍 Python 3.8+

🤖 Scikit-Learn – Machine Learning

📊 Pandas & NumPy – Data Handling

🌐 Flask – Web Framework

🎨 HTML/CSS – Frontend UI

📌 Future Improvements

✨ Add a beautiful frontend (Bootstrap / Tailwind)
☁️ Deploy on Heroku / Render / AWS
📊 Build an EDA dashboard with word clouds & charts

👨‍💻 Author

Made with ❤️ by Eshita Adhikary

📜 License

📝 This project is licensed under the MIT License – free for personal & commercial use.


---









# SmartFAQ – Intelligent FAQ Chatbot 🤖

SmartFAQ is a simple FAQ chatbot developed using Python and Flask. It helps users find answers to frequently asked questions by comparing their input with predefined questions using TF-IDF vectorization and cosine similarity.

## ✨ Features

- User-friendly chatbot interface
- Matches user questions with predefined FAQs
- Uses TF-IDF for text vectorization
- Uses cosine similarity to identify relevant answers
- Provides a fallback response when no suitable match is found

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- HTML
- CSS
- JavaScript
- JSON

## 📂 Project Structure

```text
SmartFAQ/
│
├── app.py
├── faqs.json
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── script.js
    └── style.css
```

## 🚀 Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/upparasrija1-glitch/CodeAlpha_SmartFAQ.git
```

2. Navigate to the project folder:

```bash
cd CodeAlpha_SmartFAQ
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

5. Install the required libraries:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
python app.py
```

7. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## 🧠 How It Works

1. The user enters a question.
2. The chatbot converts the question into numerical text features using TF-IDF.
3. Cosine similarity compares the question with predefined FAQs.
4. The chatbot returns the answer associated with the most relevant FAQ.
5. If the similarity score is below the configured threshold, it displays a fallback response.

## 🎯 Learning Outcomes

- Working with Flask applications
- Understanding text vectorization
- Implementing cosine similarity
- Connecting frontend and backend
- Handling JSON data

## 👩‍💻 Developed As Part Of

**CodeAlpha AI Internship**

Developed with Python and a passion for learning AI! 
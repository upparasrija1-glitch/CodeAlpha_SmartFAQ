import json
from pathlib import Path

from flask import Flask, jsonify, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

FAQ_FILE = Path(__file__).with_name("faqs.json")

with FAQ_FILE.open("r", encoding="utf-8") as file:
    faqs = json.load(file)

vectorizer = TfidfVectorizer(
    lowercase=True,
    strip_accents="unicode",
    ngram_range=(1, 2)
)

faq_questions = [faq["question"] for faq in faqs]
faq_vectors = vectorizer.fit_transform(faq_questions)


def get_answer(user_question):
    user_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_vector, faq_vectors)[0]

    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]

    if best_score < 0.15:
        return (
            "Sorry, I couldn't find an answer. "
            "Please contact the college administration."
        )

    return faqs[best_match_index]["answer"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Please send a valid JSON request."}), 400

    message = data.get("message")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Please enter a question."}), 400

    if len(message) > 500:
        return jsonify(
            {"error": "Your question must be 500 characters or fewer."}
        ), 400

    answer = get_answer(message.strip())
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)

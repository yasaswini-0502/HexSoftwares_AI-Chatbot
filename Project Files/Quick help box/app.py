# app.py (local only)
import os
import time
import random
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("quick-help-chatbox")

app = Flask(__name__, template_folder="templates")
CORS(app)

# Local fallback responses only
LOCAL_KNOWLEDGE = {
    "greetings": [
        "Hello! I'm Quick Help Chatbox 👋 How can I help you today?",
        "Hi there! 😊 What would you like to ask?"
    ],
    "goodbye": [
        "Goodbye — come back soon! 👋",
        "See you later! If you need help again, I'm here."
    ],
    "thanks": [
        "You're welcome! 🙌",
        "Happy to help! 😊"
    ],
    "capabilities": [
        "I can answer questions about general topics, help with simple programming problems, or chat about everyday things.",
        "Ask me anything — if I don't know, I'll try my best or tell you I don't know."
    ],
    "good_morning": [
        "Good morning! ☀ Hope you have a wonderful day ahead."
    ],
    "good_night": [
        "Good night! 🌙 Sweet dreams!"
    ],
    "joke": [
        "Why did the computer go to the doctor? 💻 Because it caught a virus! 😂"
    ],
    "how_are_you": [
        "I'm doing great, thanks for asking! How about you?"
    ],
    "default": [
        "Interesting — tell me more!",
        "I don't have a full answer for that, but I can try. Could you rephrase?"
    ],
    "error": [
        "Sorry, something went wrong. Please try again in a few seconds."
    ]
}

def get_local_response(text):
    t = text.lower()
    if any(x in t for x in ["hi", "hello", "hey"]):
        return random.choice(LOCAL_KNOWLEDGE["greetings"])
    if any(x in t for x in ["bye", "goodbye", "see you"]):
        return random.choice(LOCAL_KNOWLEDGE["goodbye"])
    if any(x in t for x in ["thank", "thanks"]):
        return random.choice(LOCAL_KNOWLEDGE["thanks"])
    if "what can you" in t or "capabilities" in t:
        return random.choice(LOCAL_KNOWLEDGE["capabilities"])
    if "good morning" in t:
        return random.choice(LOCAL_KNOWLEDGE["good_morning"])
    if "good night" in t:
        return random.choice(LOCAL_KNOWLEDGE["good_night"])
    if "tell me a joke" in t:
        return random.choice(LOCAL_KNOWLEDGE["joke"])
    if "how are you" in t:
        return random.choice(LOCAL_KNOWLEDGE["how_are_you"])
    if "?" in t:
        return random.choice(LOCAL_KNOWLEDGE["default"])
    return random.choice(LOCAL_KNOWLEDGE["default"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    start_time = time.time()
    data = request.get_json(force=True, silent=True) or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Empty message", "reply": "Please send a message."}), 400

    logger.info("User: %s", message)

    # Always use local responses
    reply = get_local_response(message)
    elapsed = round(time.time() - start_time, 2)
    logger.info("Reply (local) in %ss", elapsed)
    return jsonify({
        "reply": reply,
        "source": "local",
        "processing_time": elapsed,
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
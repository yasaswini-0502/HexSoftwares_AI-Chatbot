# HexSoftwares_AI-Chatbot

Project Video Link:https://drive.google.com/file/d/1WcpkgI63SIukaIf9H4tgOUGPg2Bdb7R7/view?usp=drivesdk

Quick Help Chatbox 🤖

An interactive AI-powered chatbot web application designed to handle user queries, provide quick support, and engage in conversations in a human-like manner.

📌 Features

Customer Support & Engagement – Simulates a virtual assistant that can answer queries and maintain conversational flow.

Rule-Based NLP – Uses keyword matching to generate intelligent responses without heavy ML models.

Voice Interaction – Supports voice input via Web Speech API and optional text-to-speech for bot responses.

Emoji Support – Quick emoji picker for expressive communication.

Responsive UI – Works seamlessly on desktop and mobile devices.

Accessible Design – ARIA roles, live region updates, and keyboard-friendly navigation.


🛠 Technologies & Techniques Used

🖥️ Frontend

HTML5, CSS3, JavaScript (Vanilla)

Responsive UI with Flexbox and Media Queries

CSS Variables for theming (--primary, --secondary)

Animations for typing indicators (@keyframes typing)

DOM Manipulation for dynamic message rendering

Web Speech API for voice recognition (Speech-to-Text)

SpeechSynthesis API for text-to-speech (toggleable)

Emoji Picker for quick reactions

XSS Prevention via HTML escaping (escapeHtml() function)

🛠 Backend

Python Flask for serving pages and handling chat requests

Flask-CORS for cross-origin API access

Rule-based NLP using keyword matching


Randomized Responses with random.choice() for natural feel

Environment Variables via python-dotenv

Structured Logging using Python’s logging module

🚀 How It Works

1. User sends a message via text, emoji, or voice input.
2. Message is sent to Flask backend via Fetch API.
3. Backend processes the message using rule-based NLP and returns a JSON response.
4. Frontend displays the bot’s response, plays voice output (if enabled), and scrolls to the latest message.

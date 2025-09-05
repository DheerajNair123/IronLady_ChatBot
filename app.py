
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Initialize Flask app
app = Flask(__name__)


# Set Gemini API Key (replace with your actual Gemini API key)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyAfvdrhX6IVC0sWlE2w8z9BD08DOMefJhQ")
genai.configure(api_key=GEMINI_API_KEY)

# Function to interact with Gemini API and provide FAQ answers
def get_bot_response(user_input):
    user_input_lower = user_input.lower()

    # Predefined FAQ answers
    faq_answers = {
        "What programs does Iron Lady offer?": "Iron Lady offers leadership programs focused on personal growth, entrepreneurship, and empowering women.",
        "What is the program duration?": "The program lasts 3 to 6 months, depending on the program type.",
        "Is the program online or offline?": "The program is available both online and offline. We offer flexible options.",
        "Are certificates provided?": "Yes, participants will receive a certificate upon successful completion of the program.",
        "Who are the mentors/coaches?": "Our mentors are experienced leaders in the fields of entrepreneurship, leadership, and personal development."
    }

    # Check if user input matches any FAQ
    if user_input in faq_answers:
        return faq_answers[user_input]

    # Use Gemini API if the question is not in the FAQ
    try:
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process your request."

# Route to serve the chat interface
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle chat interactions
@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("user_input")
    bot_response = get_bot_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)

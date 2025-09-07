# Iron Lady Chatbot

This project is a simple FAQ chatbot web application built with Flask and Google Gemini API. It provides instant answers to frequently asked questions about Iron Lady's programs and can handle general queries using the Gemini generative AI model.

## Features
- Web-based chat interface
- Predefined FAQ answers for common questions
- Integration with Google Gemini API for open-ended queries
- Simple, customizable UI (HTML/CSS)

## Project Structure
```
Chatbot/
  app.py                # Main Flask application
  list_gemini_models.py # (Optional) Script to list Gemini models
  static/
    style.css           # Stylesheet for the chat UI
  templates/
    index.html          # Main chat interface
SimpleApp/
  index.html            # (Not used by the chatbot)
```

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/DheerajNair123/IronLady_ChatBot.git
cd IronLady_Chatbot
```

### 2. Install Dependencies
Make sure you have Python 3.7+ installed.

```
pip install flask google-generativeai
```

### 3. Set the Gemini API Key
Set your Google Gemini API key as an environment variable:

**Windows (PowerShell):**
```
$env:GEMINI_API_KEY = "your-gemini-api-key"
```
**Linux/macOS:**
```
export GEMINI_API_KEY="your-gemini-api-key"
```

Alternatively, you can edit `app.py` to hardcode your API key (not recommended for production).

### 4. Run the Application
```
python app.py
```
The app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage
- Open the web interface in your browser.
- Type your question in the chat box.
- The bot will respond with either a predefined FAQ answer or a generative response from Gemini.

## Customization
- Edit `faq_answers` in `app.py` to add or modify FAQ responses.
- Update the UI in `templates/index.html` and `static/style.css` as needed.

## License
This project is for demo purposes. 

import google.generativeai as genai
import os

def list_gemini_models():
    api_key = os.environ.get("GEMINI_API_KEY", "AIzaSyAfvdrhX6IVC0sWlE2w8z9BD08DOMefJhQ")
    genai.configure(api_key=api_key)
    models = genai.list_models()
    for model in models:
        print(model)

if __name__ == "__main__":
    list_gemini_models()

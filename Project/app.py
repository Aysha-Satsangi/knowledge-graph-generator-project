import openai
import google.generativeai as genai
import pdfplumber
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# ====== Configure your Gemini or OpenAI API key here ======
use_gemini = True

if use_gemini:
    genai.configure(api_key="AIzaSyB1O1oLZYErxpkmKE0VZE1tXeewpBHP34c")
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_pdf_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_url_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # only grab main <article> if present, otherwise fall back to full page
        article = soup.find("article")
        if article:
            content = article.get_text(separator=" ", strip=True)
        else:
            content = soup.get_text(separator=" ", strip=True)
        return content
    except Exception as e:
        return f"Error fetching URL: {str(e)}"

# def generate_structured_json(text):
#     prompt = f"""
# You are an AI assistant. Given the following content, extract a structured, contextual JSON with:
# - entities (id, name, type, description)
# - relations (source, target, relation)

# Return only the JSON. Text:
# {text}
# """
#     if use_gemini:
#         response = model.generate_content(prompt)
#         return response.text
#     else:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response['choices'][0]['message']['content']

def generate_structured_json(text):
    prompt = f"""
You are an AI assistant. Given the following content, extract a structured, contextual JSON with:
- entities (id, name, type, description)
- relations (source, target, relation)

Return only the JSON. No explanation, no formatting, no markdown.

Text:
{text}
"""

    if use_gemini:
        response = model.generate_content(prompt)
        result_text = response.text.strip()

        # Remove any leading junk (like "json" or ```json)
        if result_text.lower().startswith("json"):
            result_text = result_text[result_text.lower().find("{"):].strip()
        elif result_text.startswith("```"):
            result_text = result_text.split("```")[1].strip()
            if result_text.lower().startswith("json"):
                result_text = result_text[result_text.lower().find("{"):].strip()

        print("=== Cleaned Gemini Output ===")
        print(result_text)

        return result_text
    else:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/extract", methods=["POST"])
def extract():
    input_type = request.form.get("type")
    input_text = ""

    if input_type == "text":
        input_text = request.form.get("data")
    elif input_type == "url":
        url = request.form.get("data")
        input_text = extract_url_text(url)
    elif input_type == "pdf":
        pdf_file = request.files['data']
        input_text = extract_pdf_text(pdf_file)
    else:
        return jsonify({"error": "Invalid input type"}), 400

    structured_json = generate_structured_json(input_text)
    return jsonify({"structured_json": structured_json})

if __name__ == "__main__":
    app.run(debug=True)

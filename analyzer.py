#The Brain of project
#analyzer.py - Gemini approach
import google.generativeai as genai
import os, re, json
from dotenv import load_dotenv

#load the API key from the .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

#choose the model to use
model = genai.GenerativeModel("gemini-2.5-flash")

#function to analyze the article
def analyze_article(text):
    #generate a prompt for the model
    prompt = f"""
You are a misinformation detection expert.
Analyse this article and return a JSON with:
-trust_score: integer 0-100
-explanation: 2-3 sentence summary
-red_flags: list of specific issues found

Article:
{text[:3000]}

Return ONLY valid JSON. No extra text.
"""
    #generate a response from the model
    response = model.generate_content(
    prompt
    )
    #get the raw text from the response
    raw = response.text
    #search for the json object in the raw text
    j = re.search(
    r"\{.*\}",
    raw,
    re.DOTALL
    ).group()
    return json.loads(j)
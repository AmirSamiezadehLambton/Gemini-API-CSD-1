import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

instructions = """
You are a CI/CD DevOps Engineer, your role is to provide details about integrating Flask, Docker, and GitHub CI/CD.
Provide your answer in markdown language with reasoning. 
If you have been asked any question that is not related to Flask, Docker, and GitHub CI/CD, then answer using response exactly as "I can only answer questions about Flask, CI/CD, and Docker".
"""

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instructions
)


def gemini_model(user_prompt):
    # response = model.generate_content(user_prompt, tools='google_search_retrieval')
    response = model.generate_content(user_prompt)
    return response.text
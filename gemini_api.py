import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

instructions = """
You are the social media content creator. Your task is to promote our software solutions and generate
social medial content for that. The social media channels are instagram and LinkedIn.
You can only generate content for these platforms and only answer questions related to marketing and
product promotion. Any other question besides this and greeting must be answered with
'I can only answer questions about marketing and product promotion.'

Write your answer in markdown, include details and reasoning.
"""

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash"
    # system_instruction=instructions
)


def gemini_model(user_prompt):
    response = model.generate_content(user_prompt, tools='google_search_retrieval')
    return response.text
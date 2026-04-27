#This agent will compare the extracted details (resume JSON and job description JSON) of two JSON data and tell whether the candidate is "Selected" or "Rejected" with reason and skills matched score. 
from openai import OpenAI
from dotenv import load_dotenv
import os
from app.prompts import CANDIDATE_EVALUATION
import json

#Load environmental variables from .env file
load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=my_api_key)

#To compare the extracted resume details and job description detials
def evaluate_candidate(candidate_details: str, jd: str) -> str:
    prompt = CANDIDATE_EVALUATION.format(resume_json = candidate_details, jd_json = jd)

    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [{"role": "user", "content": prompt}]
        )

        print("Response from OpenAI API: ", response.choices[0].message.content)

        return response.choices[0].message.content

    except Exception as e:
        return json.dumps({"error": str(e)})
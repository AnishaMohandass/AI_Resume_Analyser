#This agent will extract the details of job description from the job_description.pdf file.
from openai import OpenAI
from dotenv import load_dotenv
import os
from app.prompts import EXTRACT_JD_DETAILS
import json

#Load environmental variables from .env file
load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=my_api_key)

#To extract details from the job_description.pdf file
def analyse_jd(text: str) -> str:
    prompt = EXTRACT_JD_DETAILS.format(jd_text = text)

    try:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [{"role": "user", "content": prompt}]
        )

        print("Response from OpenAI API for JD: ", response.choices[0].message.content)
        
        return response.choices[0].message.content
    
    except Exception as e:
        return json.dumps({"error": str(e)})
#This agent will extract the skills and experience of the candidate from the uploaded resume and provides the data in JSON format.
from openai import OpenAI
from dotenv import load_dotenv
import os
from app.prompts import EXTRACT_CANDIDATE_DETAILS
import json

#Load environmental variables from .env file
load_dotenv(dotenv_path=".env")
my_api_key = os.getenv("OPENAI_API_KEY")

#Initialize OpenAI Client
client = OpenAI(api_key=my_api_key)

#To extract details from the resume
def analyse_resume(text: str) -> str:
    prompt = EXTRACT_CANDIDATE_DETAILS.format(resume_text = text)

    try:
        #Using chat.completions API to communicate with OpenAI
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [{"role": "user", "content": prompt}]
        )
        print("Response from Resume Extractor Agent: ", response.choices[0].message.content) #['content']

        return response.choices[0].message.content #['content']
    
    except Exception as e:
        return json.dumps({"error": str(e)})
from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
from app.parsepdf import parse_pdf
from app.agents.resume_extractor import analyse_resume
from app.agents.jd_extractor import analyse_jd
from app.agents.candidate_evaluation import evaluate_candidate
import json

#Creating an API using FastAPI
app = FastAPI()

@app.post("/resume_analyser/")
async def upload_resume(resume: UploadFile):
    print("Received resume file: ", resume.filename)

    #Converting the resume PDF file into text using parsepdf.py file
    resume_text = parse_pdf(resume.file)

    #To send the converted resume text to Agent-1 (resume_extractor) 
    candidate_details = analyse_resume(resume_text)

    #Converting the job_description PDF file into text using parsepdf.py file
    jd_text = ""
    with open ("resources/job_description.pdf", "rb") as file:
        jd_text = parse_pdf(file)

    #To send the converted job_description text to Agent-2 (jd_extractor) 
    jd_details = analyse_jd(jd_text)

    #To send the extracted resume details and job description details to Agent-3 (candidate_evaluation)
    evaluation = evaluate_candidate(candidate_details, jd_details)

    print("Evaluation result: ", evaluation)

    result_json = json.loads(evaluation)
    return JSONResponse(content=result_json)
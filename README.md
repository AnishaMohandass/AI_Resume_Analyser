# AI_Resume_Analyser
Displaying candidate status by analyzing the resume against the job description file.

## Steps:
<b>Step 1 -</b> Create the folder structure.
-> app
	-> agents
	   -> candidate_evaluation.py
	   -> jd_extractor.py
	   -> resume_extractor.py
	-> ui
		-> streamlit.py
	-> main.py
	-> parsepdf.py
	-> prompts.py
-> resources
   -> job_description.pdf
   -> resume.pdf
-> .env 
-> requirements.txt


<b>Step 2 -</b> Run requirements.txt file to install the python libraries defined in the file.
Open terminal and run this command
pip install -r requirements.txt

Step 3 - In .env file, paste the OpenAI API key.

Step 4 - Create parsepdf.py file to convert PDF file to text.

Step 5 - Create streamlit.py file to create the User Interface (UI).
To run the UI file, open terminal and go to project folder (app/ui) and run this command.
streamlit run streamlit.py

Step 6 - Type the "EXTRACT_CANDIDATE_DETAILS" prompt in prompts.py file.

Step 7 - Creat Agent-1 "resume_extractor".
This agent will extract the skills and experience of the candidate from the uploaded resume and provides the data in JSON format.

Step 8 - Type the "EXTRACT_JD_DETAILS" prompt in prompts.py file.

Step 9 - Creat Agent-2 "jd_extractor".
This agent will extract the details of job description from the job_description.pdf file and provides the data in JSON format.

Step 10 - Type the "CANDIDATE_EVALUATION" prompt in prompts.py file.

Step 11 - Creat Agent-3 "candidate_evaluation".
This agent will compare the extracted details (resume JSON and job description JSON) of two JSON data and tell whether the candidate is "Selected" or "Rejected" with reason and skills matched score. 

Step 12 - Create main.py file to execute all 3 created agents.
Open terminal and run this command
uvicorn app.main:app --reload

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


<b>Step 2 -</b> Run <b>requirements.txt</b> file to install the python libraries defined in the file.

Open terminal and run this command:

<i>pip install -r requirements.txt</i>


<b>Step 3 -</b> In <b>.env</b> file, paste the OpenAI API key.

<b>Step 4 -</b> Create <b>parsepdf.py</b> file to convert PDF file to text.

<b>Step 5 -</b> Create <b>streamlit.py</b> file to create the User Interface (UI).

To run the UI file, open terminal and go to project folder (app/ui) and run this command:

<i>streamlit run streamlit.py</i>

<b>Step 6 -</b> Type the "EXTRACT_CANDIDATE_DETAILS" prompt in <b>prompts.py</b> file.

<b>Step 7 -</b> Creat <b>Agent-1 "resume_extractor"</b>.

This agent will extract the skills and experience of the candidate from the uploaded resume and provides the data in JSON format.

<b>Step 8 -</b> Type the "EXTRACT_JD_DETAILS" prompt in <b>prompts.py</b> file.

<b>Step 9 -</b> Creat <b>Agent-2 "jd_extractor"</b>.

This agent will extract the details of job description from the job_description.pdf file and provides the data in JSON format.

<b>Step 10 -</b> Type the "CANDIDATE_EVALUATION" prompt in <b>prompts.py</b> file.

<b>Step 11 -</b> Creat <b>Agent-3 "candidate_evaluation"</b>.

This agent will compare the extracted details (resume JSON and job description JSON) of two JSON data and tell whether the candidate is "Selected" or "Rejected" with reason and skills matched score. 

<b>Step 12 -</b> Create <b>main.py</b> file to execute all 3 created agents.

Open terminal and run this command:

<i>uvicorn app.main:app --reload</i>


# UI code to upload a PDF resume, analysing it with OpenAI's API and displaying the results 
# Streamlit is a python library to create an User Interface (UI) 

import streamlit as st
import requests

st.title("Resume Analyser")

uploaded_file = st.file_uploader("Upload a resume in PDF format only", type="pdf")

if uploaded_file is not None:
    st.write("File uploaded successfully!", uploaded_file.name)
    print("File uploaded successfully!", uploaded_file.name)

    if st.button("Analyse Resume"):
        response = requests.post("http://localhost:8000/resume_analyser/", files={"resume": uploaded_file})

        if response.status_code == 200:
            st.write("Resume processed successfully!")
            response_data = response.json()
            st.write("Candidate status: ", response_data.get("candidate_status"))
            st.write("Feedback: ", response_data.get("reason"))
            st.write("Skills matched: ", response_data.get("skill_match_percentage"), "%")

        else:
            st.write("Error in analysing the resume: ", response.text)
            print("Error in analysing the resume: ", response.text)
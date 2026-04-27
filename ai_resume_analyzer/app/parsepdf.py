#Read a PDF file and extract text

import PyPDF2 as pypdf2

def parse_pdf(file) -> str: #(-> str): Returns a string containing the raw text found in the PDF
    print("Parsing the PDF File...")
    try:
        reader = pypdf2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip() #To remove specific characters (spaces, tabs(\t), newlines(\n)) from both the beginning and the end of a string
    
    except Exception as e:
        return str(e)
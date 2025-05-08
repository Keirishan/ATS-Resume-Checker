# 📝 ATS Resume Checker

A web-based tool to evaluate how well a resume matches a job description using keyword extraction, scoring, and visualizations. Built with Streamlit.

---

## 🔗 Live Demo

You can try out the ATS Score Checker app live here:

👉 [Click to Open the App](https://ats-resume-checker-ugika56gnb6xbswkw6u8dm.streamlit.app/)

This app helps users evaluate their resumes against job descriptions using ATS-friendly scoring.


## 🚀 Tech Stack

- **Frontend/UI**: Streamlit  
- **Backend**: Python  
- **Text Processing**: spaCy, scikit-learn, pdfplumber (for PDF), docx2txt (for DOCX)  
- **Visualization**: Plotly

---

## 🛠️ Installation

### 1. Clone this repository
```bash
git clone https://github.com/Keirishan/ATS-Resume-Checker.git
cd ATS-Resume-Checker
```

### 2. Install dependencies
``` bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Run the app
``` bash
streamlit run app.py
```

## 💡 Features
- Upload your resume in .pdf, .docx, or .txt
- Paste job description
- Get ATS score based on keyword matching
- View interactive pie chart of matched vs unmatched keywords

## 📌 Coming Soon
- Highlight keywords directly in resume text
- Download report as PDF
- Resume formatting tips

## 👨‍💻 Author
- Keirishan Balachandran - [LinkedIn](https://www.linkedin.com/in/balachandran-keirishan-6a5a66197/)

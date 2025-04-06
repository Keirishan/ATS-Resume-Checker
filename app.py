import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from resume_parser import extract_text
import re

st.set_page_config(page_title="ATS Resume Checker", layout="centered")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def extract_keywords(text):
    vectorizer = CountVectorizer(stop_words='english')
    vectorizer.fit([text])
    return set(vectorizer.get_feature_names_out())

def compute_score(jd_keywords, resume_keywords):
    matches = jd_keywords & resume_keywords
    score = len(matches) / len(jd_keywords) * 100 if jd_keywords else 0
    return round(score, 2), matches

st.title("ATS Resume Checker")
st.markdown("Compare your resume against a job description.")

job_desc = st.text_area("Paste the Job Description", height=200)
resume_file = st.file_uploader("Upload Your Resume (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])

if st.button("Check ATS Score") and job_desc and resume_file:
    with st.spinner("Analyzing..."):
        resume_text = extract_text(resume_file)
        jd_keywords = extract_keywords(clean_text(job_desc))
        resume_keywords = extract_keywords(clean_text(resume_text))
        score, matched = compute_score(jd_keywords, resume_keywords)

        st.success(f"ATS Match Score: **{score}%**")
        st.markdown("###Matched Keywords:")
        st.write(", ".join(sorted(matched)))

        unmatched = jd_keywords - matched
        if unmatched:
            st.markdown("###Missing Keywords:")
            st.write(", ".join(sorted(unmatched)))

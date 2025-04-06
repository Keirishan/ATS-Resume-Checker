import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from resume_parser import extract_text
import re
import plotly.graph_objects as go

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

        # Pie Chart: Match vs Unmatch
        matched_count = len(matched)
        unmatched_count = len(jd_keywords - matched)

        pie_fig = go.Figure(data=[go.Pie(
            labels=["Matched", "Unmatched"],
            values=[matched_count, unmatched_count],
            marker=dict(colors=["green", "red"]),
            hole=0.4
        )])
        pie_fig.update_layout(title="Keyword Match Overview")
        st.plotly_chart(pie_fig, use_container_width=True)

        st.markdown("### Matched Keywords:")
        st.write(", ".join(sorted(matched)))

        if unmatched_count:
            st.markdown("### Missing Keywords:")
            st.write(", ".join(sorted(jd_keywords - matched)))

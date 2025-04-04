import streamlit as st
import yaml
import os

st.set_page_config(page_title="AISecGuard Dashboard", layout="wide")

st.markdown("<style>" + open("sample_files/streamlit_theme.css").read() + "</style>", unsafe_allow_html=True)

st.title("🛡️ AISecGuard - AI Security Testing Results")
st.markdown("Upload or select a test report to view analysis results:")

uploaded_file = st.file_uploader("Upload Report", type=["md", "json"])
if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    st.markdown("---")
    st.subheader("📄 Report Content")
    st.text_area("Report Preview", content, height=500)
elif os.path.exists("sample_files/example_output_report.md"):
    st.subheader("📄 Example Report")
    with open("sample_files/example_output_report.md") as f:
        st.markdown(f.read())

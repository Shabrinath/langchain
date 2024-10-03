import streamlit as st
import langchain_helper

st.title("Skill Generator")

job_role = st.sidebar.selectbox("Pick a role", ("devOps Engineer", "Data Engineer", "AI Engineer", "QA engineer", "Java developer"))

if job_role:
    response = langchain_helper.generate_technologies_for_role(job_role)
    skills_list = response['skills_list'].strip().split(",")
    for item in skills_list:
       st.write(item)


import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="AI Salary Predictor",
    page_icon="💼",
    layout="wide"
)

# ---------------------- LOAD MODEL ----------------------
@st.cache_resource
def load_files():
    model = pickle.load(open("model.pkl", "rb"))
    columns = pickle.load(open("columns.pkl", "rb"))
    return model, columns

model, columns = load_files()

# ---------------------- HEADER ----------------------
st.markdown("""
<h1 style='text-align: center; color: #00ADB5;'>💼 AI Job Salary Predictor</h1>
<p style='text-align: center;'>Predict salaries using Machine Learning 🚀</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------- SIDEBAR ----------------------
st.sidebar.header("📊 Input Features")

experience_level = st.sidebar.selectbox(
    "Experience Level", ["Entry", "Mid", "Senior"]
)

job_title = st.sidebar.selectbox(
    "Job Role",
    ["Data Scientist", "Machine Learning Engineer", "AI Engineer", "Data Analyst"]
)

company_size = st.sidebar.selectbox(
    "Company Size", ["Startup", "Medium", "MNC"]
)

company_industry = st.sidebar.selectbox(
    "Industry",
    ["Technology", "Finance", "Healthcare", "Education", "Retail"]
)

skills_ml = st.sidebar.checkbox("Machine Learning")
skills_dl = st.sidebar.checkbox("Deep Learning")
skills_python = st.sidebar.checkbox("Python")
skills_sql = st.sidebar.checkbox("SQL")

# ---------------------- PREPROCESS ----------------------
def preprocess():
    input_dict = dict.fromkeys(columns, 0)

    # Experience
    if experience_level == "Senior" and "experience_level_Senior" in input_dict:
        input_dict["experience_level_Senior"] = 1
    elif experience_level == "Mid" and "experience_level_Mid" in input_dict:
        input_dict["experience_level_Mid"] = 1

    # Job Title
    jt_map = {
        "Machine Learning Engineer": "job_title_Machine Learning Engineer",
        "Data Scientist": "job_title_Data Scientist",
        "AI Engineer": "job_title_AI Engineer",
        "Data Analyst": "job_title_Data Analyst"
    }
    col = jt_map.get(job_title)
    if col in input_dict:
        input_dict[col] = 1

    # Company Size
    cs_map = {
        "MNC": "company_size_MNC",
        "Medium": "company_size_Medium"
    }
    col = cs_map.get(company_size)
    if col in input_dict:
        input_dict[col] = 1

    # Industry
    industry_col = f"company_industry_{company_industry}"
    if industry_col in input_dict:
        input_dict[industry_col] = 1

    # Skills
    skill_map = {
        "skills_ml": skills_ml,
        "skills_deep_learning": skills_dl,
        "skills_python": skills_python,
        "skills_sql": skills_sql
    }

    for key, val in skill_map.items():
        if key in input_dict:
            input_dict[key] = int(val)

    return pd.DataFrame([input_dict])

# ---------------------- MAIN ----------------------
st.subheader("💰 Predict Salary")

if st.button("Predict Salary"):
    input_data = preprocess()
    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Salary: ₹ {int(prediction):,}")

# ---------------------- VISUAL ----------------------
st.markdown("---")
st.subheader("📈 Sample Salary Distribution")

data = np.random.normal(100000, 20000, 500)

fig, ax = plt.subplots()
sns.histplot(data, kde=True, ax=ax)
st.pyplot(fig)

# ---------------------- FOOTER ----------------------
st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:20px;">

<p>Made with ❤️ by <b>Moh Azeem</b></p>

<a href="https://github.com/MohAzeem1" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30">
</a>

&nbsp;&nbsp;&nbsp;

<a href="https://www.linkedin.com/in/moh-azeem-5381a2225/" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30">
</a>

</div>
""", unsafe_allow_html=True)
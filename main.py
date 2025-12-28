import streamlit as st
from prediction_helper import predict

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Finlytics | Credit Risk Modelling",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #f8f5ff, #efe9ff);
}

/* Headings */
h1, h2, h3 {
    color: #3b2f63;
}

/* Buttons */
div.stButton > button {
    background-color: #7b5cff;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
}

div.stButton > button:hover {
    background-color: #6846f2;
}

/* Metric card */
[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 12px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE & INTRO ----------------
st.title("📊 Finlytics")
st.markdown(
    "### 💡 Smart credit insights powered by data"
)

st.markdown("---")

# ---------------- INPUT LAYOUT ----------------
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input("Age", 18, 100, 28)

with row1[1]:
    income = st.number_input("Annual Income", min_value=1, value=1200000)

with row1[2]:
    loan_amount = st.number_input("Loan Amount", min_value=0, value=256000)

# Derived feature
loan_percent_income = loan_amount / income

with row2[0]:
    st.metric("Loan to Income Ratio", f"{loan_percent_income:.2f}")

with row2[1]:
    emp_length = st.number_input("Employment Length (years)", 0, 40, 3)

with row2[2]:
    interest_rate = st.number_input("Interest Rate (%)", 1.0, 40.0, 10.0)

with row3[0]:
    credit_hist_length = st.number_input("Credit History Length (years)", 0, 40, 5)

with row3[1]:
    residence_type = st.selectbox(
        "Residence Type",
        ["OWN", "RENT", "MORTGAGE"]
    )

with row3[2]:
    loan_purpose = st.selectbox(
        "Loan Purpose",
        ["EDUCATION", "HOME_IMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE", "DEBT_CONSOLIDATION"]
    )

with row4[0]:
    loan_grade = st.selectbox(
        "Loan Grade",
        ["A", "B", "C", "D", "E", "F", "G"]
    )

with row4[1]:
    default_flag = st.selectbox(
        "Previous Default on File?",
        ["N", "Y"]
    )

st.markdown("")

# ---------------- PREDICTION ----------------
if st.button("🔍 Calculate Risk"):
    probability, credit_score, rating = predict(
        age=age,
        income=income,
        emp_length=emp_length,
        loan_amount=loan_amount,
        interest_rate=interest_rate,
        loan_percent_income=loan_percent_income,
        credit_hist_length=credit_hist_length,
        residence_type=residence_type,
        loan_purpose=loan_purpose,
        loan_grade=loan_grade,
        default_flag=default_flag
    )

    st.markdown("---")
    st.subheader("📈 Risk Assessment Result")

    st.write(f"**Default Probability:** {probability:.2%}")
    st.write(f"**Credit Score:** {credit_score}")
    st.write(f"**Rating:** {rating}")

import joblib
import pandas as pd

MODEL_PATH = "artifacts/model_data.joblib"
model = joblib.load(MODEL_PATH)

def predict(
    age,
    income,
    emp_length,
    loan_amount,
    interest_rate,
    loan_percent_income,
    credit_hist_length,
    residence_type,
    loan_purpose,
    loan_grade,
    default_flag
):
    input_dict = {
        "person_age": age,
        "person_income": income,
        "person_emp_length": emp_length,
        "loan_amnt": loan_amount,
        "loan_int_rate": interest_rate,
        "loan_percent_income": loan_percent_income,
        "cb_person_cred_hist_length": credit_hist_length,
        "person_home_ownership": residence_type,
        "loan_intent": loan_purpose,
        "loan_grade": loan_grade,
        "cb_person_default_on_file": default_flag
    }

    df = pd.DataFrame([input_dict])

    # One-hot encoding
    df = pd.get_dummies(df)

    # Align with training columns
    model_features = model.named_steps["scaler"].feature_names_in_
    df = df.reindex(columns=model_features, fill_value=0)

    # Prediction
    default_probability = model.predict_proba(df)[0][1]
    credit_score = int(300 + (1 - default_probability) * 600)

    if credit_score < 500:
        rating = "Poor"
    elif credit_score < 650:
        rating = "Average"
    elif credit_score < 750:
        rating = "Good"
    else:
        rating = "Excellent"

    return default_probability, credit_score, rating

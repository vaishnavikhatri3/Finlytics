<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Finlytics – Credit Risk Modelling</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            background-color: #f8f5ff;
            color: #2c2541;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #3b2f63;
        }
        code {
            background-color: #eee;
            padding: 3px 6px;
            border-radius: 4px;
        }
        .box {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            margin: 15px 0;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
    </style>
</head>

<body>

<h1>📊 Finlytics</h1>
<h3>Smart credit insights powered by data, not guesswork.</h3>

<div class="box">
<p>
<strong>Finlytics</strong> is a machine learning–based credit risk assessment system that predicts
<strong>default probability, credit score, and credit rating</strong> using real-world financial data.
The project focuses on accuracy, explainability, and practical financial decision-making.
</p>
</div>

<hr>

<h2>📁 Dataset Information (Kaggle)</h2>

<div class="box">
<p>
The model is trained using the <strong>Credit Risk Dataset</strong> from Kaggle.
This dataset contains real-world inspired financial and personal attributes of loan applicants.
</p>

<ul>
    <li><strong>Source:</strong> Kaggle – Credit Risk Dataset</li>
    <li><strong>Target Variable:</strong> <code>loan_status</code></li>
    <li><strong>Problem Type:</strong> Binary Classification (Default / Non-Default)</li>
</ul>

<h4>Key Features Used:</h4>
<ul>
    <li>person_age</li>
    <li>person_income</li>
    <li>person_emp_length</li>
    <li>loan_amnt</li>
    <li>loan_int_rate</li>
    <li>loan_percent_income</li>
    <li>cb_person_cred_hist_length</li>
    <li>person_home_ownership</li>
    <li>loan_intent</li>
    <li>loan_grade</li>
    <li>cb_person_default_on_file</li>
</ul>
</div>

<hr>

<h2>🧠 Model Training Process</h2>

<div class="box">
<ol>
    <li>Loaded the Kaggle dataset using Pandas</li>
    <li>Performed data cleaning by removing missing values</li>
    <li>Selected relevant financial and behavioral features</li>
    <li>Converted categorical variables using One-Hot Encoding</li>
    <li>Split data into training and testing sets (80/20)</li>
    <li>Built a Machine Learning pipeline with:
        <ul>
            <li>StandardScaler for feature scaling</li>
            <li>RandomForestClassifier for prediction</li>
        </ul>
    </li>
    <li>Trained the model on training data</li>
    <li>Evaluated accuracy and performance on test data</li>
    <li>Saved the trained pipeline as a <code>.joblib</code> file</li>
</ol>
</div>

<hr>

<h2>⚙️ Technology Stack</h2>

<div class="box">
<ul>
    <li>Python</li>
    <li>Streamlit (Frontend)</li>
    <li>Pandas & NumPy (Data Processing)</li>
    <li>Scikit-learn (Machine Learning)</li>
    <li>Joblib (Model Serialization)</li>
</ul>
</div>

<hr>

<h2>🖥️ Application Workflow</h2>

<div class="box">
<ol>
    <li>User enters personal and financial details through the UI</li>
    <li>Derived features like Loan-to-Income Ratio are calculated internally</li>
    <li>Inputs are aligned with the trained feature space</li>
    <li>Model predicts:
        <ul>
            <li>Default Probability</li>
            <li>Credit Score (300–900)</li>
            <li>Credit Rating (Poor / Average / Good / Excellent)</li>
        </ul>
    </li>
    <li>Results are displayed in real-time on the Streamlit interface</li>
</ol>
</div>

<hr>

<h2>📂 Project Structure</h2>

<div class="box">
<pre>
Finlytics/
├── artifacts/
│   └── model_data.joblib
├── data/
│   └── credit_data.csv
├── notebooks/
│   └── Credit_risk.ipynb
├── main.py
├── prediction_helper.py
├── requirements.txt
└── README.html
</pre>
</div>

<hr>

<h2>🎯 Key Highlights</h2>

<div class="box">
<ul>
    <li>Real-world Kaggle dataset</li>
    <li>End-to-end ML pipeline</li>
    <li>Derived feature engineering</li>
    <li>Business-aligned risk scoring</li>
    <li>Clean and user-friendly UI</li>
</ul>
</div>

<hr>

<h2>👩‍💻 Author</h2>

<div class="box">
<p>
<strong>Vaishnavi Khatri</strong><br>
International Institue Of Professional Studies (IIPS)<br>
Devi Ahilya Vishwavidyalaya (DAVV), Indore
</p>
</div>

</body>
</html>

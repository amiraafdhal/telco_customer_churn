
import streamlit as st
import pandas as pd
import pickle

# Load model
with open("tuned_logistic_regression.pkl", "rb") as f:
    model = pickle.load(f)

st.title("📊 Telco Customer Churn Prediction App")

st.sidebar.header("Choose Prediction Mode")
mode = st.sidebar.radio("Select input mode", ["Single Customer", "Batch Prediction (CSV)"])

# Load a sample structure for reference columns
sample_data = pd.read_csv("df_clean.csv").drop(columns=["customerID", "Churn"])
required_columns = sample_data.columns.tolist()

def predict(df_input):
    predictions = model.predict(df_input)
    probabilities = model.predict_proba(df_input)[:, 1]
    result = df_input.copy()
    result["Churn_Predicted"] = predictions
    result["Churn_Probability"] = probabilities
    return result

if mode == "Single Customer":
    st.subheader("Enter Customer Details")

    input_data = {}
    for col in required_columns:
        if sample_data[col].dtype == "object":
            options = sample_data[col].dropna().unique().tolist()
            input_data[col] = st.selectbox(f"{col}:", options)
        else:
            min_val = float(sample_data[col].min())
            max_val = float(sample_data[col].max())
            input_data[col] = st.slider(f"{col}:", min_val, max_val, float(sample_data[col].mean()))

    input_df = pd.DataFrame([input_data])

    if st.button("Predict Churn"):
        result = predict(input_df)
        st.write("### 🔍 Prediction Result:")
        st.write(result[["Churn_Predicted", "Churn_Probability"]])
        if result["Churn_Predicted"].iloc[0] == 1:
            st.error("⚠️ This customer is likely to churn!")
        else:
            st.success("✅ This customer is likely to stay.")

else:
    st.subheader("Upload CSV File for Bulk Prediction")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        df_uploaded = pd.read_csv(uploaded_file)
        missing_cols = set(required_columns) - set(df_uploaded.columns)
        if missing_cols:
            st.error(f"The uploaded file is missing required columns: {missing_cols}")
        else:
            results = predict(df_uploaded)
            st.write("### 🧾 Prediction Results")
            st.dataframe(results[["Churn_Predicted", "Churn_Probability"]])
            csv = results.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Results CSV", data=csv, file_name="churn_predictions.csv", mime="text/csv")

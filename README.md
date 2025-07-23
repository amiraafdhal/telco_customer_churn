# 📉 Telco Customer Churn Prediction

Welcome to our machine learning project focused on predicting customer churn in the telecom industry. Using real-world inspired data, we developed and evaluated models to identify at-risk customers and uncover key drivers of churn.

## 👥 Team Members

- [Christian](https://github.com/Christian-Chrata)  
- [Ditya Anjani](https://github.com/itzjanietz)  
- [Amira Afdhal](https://github.com/amiraafdhal)  

---

## 🎯 Project Goals

1. **Predict Churn**  
   Build a model to accurately classify whether a customer will churn.

2. **Identify Churn Drivers**  
   Extract insights into which features most influence churn.

3. **Customer Segmentation**  
   Enable better decision-making by grouping customers based on usage and risk.

---

## 🛠️ Technologies Used

- Python (Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn)
- XGBoost & LightGBM
- Jupyter Notebook
- Pickle for model serialization
- Tableau (for visual dashboards)
- Streamlit (for app interface)

---

## 🧠 Model Highlights

- **Final Model**: Logistic Regression (Tuned)
- **F2 Score**: 0.878
- **ROC AUC**: 0.987
- **True Churns Predicted**: 1,611 out of 1,869

---

## 🔍 Key Insights

- Customers with **low satisfaction**, **fiber internet**, and **high monthly charges** are more likely to churn.
- Customers with **Online Security**, **Tech Support**, or **Device Protection**, and those with **high satisfaction scores**, are more loyal.

---

## 📊 Interactive Dashboards

- **📈 Tableau Dashboard**:
  ![alt text](ETC/Dashboard.png)
  [View on Tableau Public](https://public.tableau.com/app/profile/ditya.ayu.anjani/viz/DashboardTelcoChurnatTelcoTechnologyFinpro/Dashboard)

- **🚀 Streamlit Web App**:  
  [View on streamlit](https://telco-customer-churn-alpha.streamlit.app/)
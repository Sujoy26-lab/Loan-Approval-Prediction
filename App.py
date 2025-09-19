import pandas as pd
import pickle as pk
import streamlit as st
from sklearn.preprocessing import StandardScaler


model = pk.load(open("Open DAta.pkl", "rb"))
scaler = pk.load(open("Scaled DAta.pkl","rb"))

st.header("Your Loan Predictor \n By - Sujoy Mukherjee")


Gender=st.selectbox("Your Gender",["Male","Female"])
Married=st.selectbox("Married ?",["Yes","No"])
Dependents=st.slider("No of Dependents",0,4)
edu= st.selectbox("Education ?",["Graduate","Non-graduate"])
s_emp= st.selectbox("Self Employed ?",["Yes","No"])
co_ap=st.slider("Co-Applicant Income",0,9999999)
loan_amnt= st.slider("Loan Needed ?",0,9999999)
Loan_dur=st.slider("Loan Duration (in months)",3,48)
credit_hist=st.slider("CIBIL SCORE",300,900)
prop=st.selectbox("AREA OF HOUSE",["RURAL","Semi-Urban","urban"])
Income= st.slider("Your Income",0,99999999)

gender_map = {"Male": 1, "Female": 0}
married_map = {"Yes": 1, "No": 0}
edu_map = {"Graduate": 1, "Non-graduate": 0}
s_emp_map = {"Yes": 1, "No": 0}
prop_map = {"urban": 0, "Semi-Urban": 1, "RURAL": -1}

Gender = gender_map[Gender]
Married = married_map[Married]
edu = edu_map[edu]
s_emp = s_emp_map[s_emp]
prop = prop_map[prop]


if st.button("Predict"):
    st.balloons()

    
    pred_data = pd.DataFrame([[Gender,Married,Dependents,edu,s_emp,co_ap,loan_amnt,Loan_dur,credit_hist,prop,Income]],
        columns=["Gender","Married","Dependents","Education","Self_Employed","CoapplicantIncome",
                 "LoanAmount","Loan_Amount_Term","Credit_History","Property_Area","TOTAL ASSESTS"])

    
    pred_data = scaler.transform(pred_data)

    
    predict = model.predict(pred_data)

    
    if predict[0]==1:
        st.markdown("✅ You are Eligible for Loan")
    else:
        st.markdown("❌ Work Hard, Loan Not Approved")

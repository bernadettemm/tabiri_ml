# Core packages
import streamlit as st
from PIL import Image 

# EDA Pkgs
import pandas as pd
import numpy as np

# Utilities
import os
import joblib
import hashlib
# passlib, bcrypt

#Data visualization
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Database
from managed_db import *

# Password
def generate_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def verify_hashes(password,hashed_text):
    if generate_hashes(password) == hashed_text:
        return hashed_text
    return False

feature_names_best = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke', 'PhysicalHealth', 'MentalHealth', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease', 'SkinCancer']
gender_dict = {"male":1,"female":0}
feature_dict = {"Yes":1,"No":0}
age_dict = {"18-24":0,"25-29":1,"30-34":2,"35-39":3,"40-44":4,"45-49":5,"50-54":6,"55-59":7,"60-64":8,"65-69":9,"70-74":10,"75-79":11,"80+":12}
race_dict = {"Black":4,"White":5,"Indian":1,"Asian":3,"Other":0,}
health_dict = {"Excellent":4,"Very good":3,"Good":2,"Fair":1,"Poor":0,}

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value
        
def get_key(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return key
        
def get_fvalue(val):
    feature_dict = {"Yes":1,"No":0}
    for key,value in feature_dict.items():
        if val == key:
            return value
        
def get_agevalue(val):
    age_dict = {"18-24":0,"25-29":1,"30-34":2,"35-39":3,"40-44":4,"45-49":5,"50-54":6,"55-59":7,"60-64":8,"65-69":9,"70-74":10,"75-79":11,"80+":12}
    for key,value in age_dict.items():
        if val == key:
            return value
        
def get_racevalue(val):
    race_dict = {"Black":4,"White":5,"Indian":1,"Asian":3,"Other":0,}
    for key,value in race_dict.items():
        if val == key:
            return value
        
def get_hvalue(val):
    health_dict = {"Excellent":4,"Very good":3,"Good":2,"Fair":1,"Poor":0,}
    for key,value in health_dict.items():
        if val == key:
            return value
        
# Load ML Model
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model

html_temp = """
		<div style="background-color:;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">TABIRI - Heart Disease Prediction System </h1>
		</div>
		"""

# Avatar Image using a url
avatar1 ="https://www.w3schools.com/howto/img_avatar1.png"
avatar2 ="https://www.w3schools.com/howto/img_avatar2.png"

result_temp ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>	
	<p style="text-align:justify;color:white">{} % probalibilty that Patient {}s</p>
	</div>
	"""

result_temp2 ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">Algorithm:: {}</h4>
	<img src="https://www.w3schools.com/howto/{}" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>	
	<p style="text-align:justify;color:white">{} % probalibilty that Patient {}s</p>
	</div>
	"""

prescriptive_message_temp ="""
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<h3 style="text-align:justify;color:black;padding:10px">Recommended Life style modification</h3>
		<ul>
		<li style="text-align:justify;color:black;padding:10px">Exercise Daily</li>
		<li style="text-align:justify;color:black;padding:10px">Get Plenty of Rest</li>
		<li style="text-align:justify;color:black;padding:10px">Exercise Daily</li>
		<li style="text-align:justify;color:black;padding:10px">Avoid Alchol</li>
		<li style="text-align:justify;color:black;padding:10px">Proper diet</li>
		<ul>
		<h3 style="text-align:justify;color:black;padding:10px">Medical Mgmt</h3>
		<ul>
		<li style="text-align:justify;color:black;padding:10px">Consult your doctor</li>
		<li style="text-align:justify;color:black;padding:10px">Take your interferons</li>
		<li style="text-align:justify;color:black;padding:10px">Go for checkups</li>
		<ul>
	</div>
	"""


descriptive_message_temp ="""
	<div style="background-color:;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<p>Coronary heart disease (CHD), also known as coronary artery disease, is a cardiovascular condition that affects the arteries 
      supplying blood to the heart muscle.</p>
	</div>
	"""
@st.cache_data
def load_image(img):
	im =Image.open(os.path.join(img))
	return im
	

def change_avatar(sex):
	if sex == "male":
		avatar_img = 'img_avatar.png'
	else:
		avatar_img = 'img_avatar2.png'
	return avatar_img

def main():
    """TABIRI -Heart Disease Risk Prediction"""
    #st.title("Heart Disease Prediction App")
    st.markdown(html_temp.format('royalblue'),unsafe_allow_html=True)

    menu = ["Home", "Login", "SignUp"]
    submenu = ["Plot", "Prediction"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        #st.text("What is Coronary Heart Disease?")
        st.markdown(descriptive_message_temp,unsafe_allow_html=True)
        st.image(load_image('images/photo1.jpg'))

    elif choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_pswd = generate_hashes(password)
            result = login_user(username, verify_hashes(password,hashed_pswd))

            if result:
                st.success("Welcome {}".format(username))

                activity = st.selectbox("Activity",submenu)
                if activity == "Plot":
                   st.subheader("Data Vis Plot")
                   df = pd.read_csv("data/heart_2020_cleaned.csv")
                   st.dataframe(df)


                   #Frequecy distribution Plot
                   freq_df = pd.read_csv("data/heart_2020_cleaned.csv")
                   st.bar_chart(freq_df['HeartDisease'])

                   if st.checkbox("Area Chart"):
                       all_columns = df.columns.to_list()
                       feature_choices = st.multiselect("Choose a Feature", all_columns)
                       new_df = df[feature_choices]
                       st.area_chart(new_df)

                   

                elif activity == "Prediction":
                    st.subheader("Predictive Analytics")

                    BMI = st.number_input("BMI",1.0,80.0)
                    Sex = st.radio("Gender", tuple(gender_dict.keys()))
                    Smoking = st.radio("Have you smoked at least 100 cigarettes in your life?", tuple(feature_dict.keys()))
                    AlcoholDrinking = st.radio("Do you drink alcohol?", tuple(feature_dict.keys()))
                    Stroke = st.radio("Ever had stoke?", tuple(feature_dict.keys()))
                    PhysicalHealth = st.number_input("How many days during the past 30 days was your physical health not good?",0,30)
                    MentalHealth = st.number_input("How many days during the past 30 days was your mental health not good?",0,30)
                    DiffWalking = st.radio("Do you have difficulties while walking?", tuple(feature_dict.keys()))
                    AgeCategory = st.radio("What is your age?", tuple(age_dict.keys()), key="age_category")
                    Race = st.radio("What is your race?", tuple(race_dict.keys()))
                    Diabetic = st.radio("Do you have/had diabetes?", tuple(feature_dict.keys()))
                    PhysicalActivity = st.radio("Have you participated in any physical activity apart from your regular job in the past month?", tuple(feature_dict.keys()))
                    GenHealth = st.radio("Would you say that your general health is good?", tuple(health_dict.keys()))
                    SleepTime = st.number_input("On average, how many hows do you sleep?",1,24)
                    Asthma = st.radio("Do you have Asthma?", tuple(feature_dict.keys()))
                    KidneyDisease = st.radio("Do you have/had kidney disease?", tuple(feature_dict.keys()))
                    SkinCancer = st.radio("Do you have/had Skin Cancer?", tuple(feature_dict.keys())) 
                    feature_list = [BMI,get_value(Sex,gender_dict),get_fvalue(Smoking),get_fvalue(AlcoholDrinking),get_fvalue(Stroke),PhysicalHealth,MentalHealth,get_fvalue(DiffWalking),get_agevalue(AgeCategory),
                                    get_racevalue(Race),get_fvalue(Diabetic),get_fvalue(PhysicalActivity),get_hvalue(GenHealth),SleepTime,get_fvalue(Asthma),get_fvalue(KidneyDisease),
                                    get_fvalue(SkinCancer)]
                    #st.write(len(feature_list))
                    #st.write(feature_list)
                    single_sample = np.array(feature_list).reshape(1,-1)

                    # ML
                    model_choice = st.selectbox("Select prediction model", ["Logistic Regression","KNN",])
                    if st.button("Predict"):
                        if model_choice == "Logistic Regression":
                            loaded_model = load_model("models/tabirimodel.joblib")
                            prediction = loaded_model.predict(single_sample)
                            pred_prob = loaded_model.predict_proba(single_sample)
                        elif model_choice == "KNN":
                            loaded_model = load_model("models/knntabiri.joblib")
                            prediction = loaded_model.predict(single_sample)
                            pred_prob = loaded_model.predict_proba(single_sample)
                        else:
                            loaded_model = load_model("models/tabirimodel.joblib")
                            prediction = loaded_model.predict(single_sample)
                            pred_prob = loaded_model.predict_proba(single_sample)

                        if prediction == 1:
                            st.warning("Your Heart is at risk")
                            pred_probability_score = {"Healthy Heart":pred_prob[0][0]*100,"Heart at Risk":pred_prob[0][1]*100}
                            st.subheader("Prediction Probability Score using {}".format(model_choice))
                            st.write(pred_probability_score)
                        else:
                            st.success("Your Heart is healthy. Keep up")
                            pred_probability_score = {"Healthy Heart":pred_prob[0][0]*100,"Heart at Risk":pred_prob[0][1]*100}
                            st.subheader("Prediction Probability Score using {}".format(model_choice))
                            st.write(pred_probability_score)

            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        new_username = st.text_input("User name")
        new_password = st.text_input("Password", type='password')

        confirm_password = st.text_input("Confirm Password", type='password')
        if new_password == confirm_password:
            st.success("Password Confirmed")
        else:
            st.warning("Passwords not the same")

        if st.button("Submit"):
            create_usertable()
            hashed_new_password = generate_hashes(new_password)
            add_userdata(new_username, hashed_new_password)
            st.success("You have successfully created a new account")
            st.info("Login to Get Started")
            pass

if __name__ == '__main__':
    main()


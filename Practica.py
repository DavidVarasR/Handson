import streamlit as st
import numpy as np
import pandas as pd
import joblib

model2= joblib.load("xgbpipe.joblib")


st.title("# Lung Cancer probability predictor")
st.markdown("Data collection")
st.sidebar.markdown("Predictor")

st.write("# Objective")
st.write("Cancer is the first cause of death in the world, in 2020 almost 10 million deaths are related to this disease being lung cancer the second most common type with 2.21 million cases as the WHO reports.")
st.write("A lot of fake news and magical treatments have appeared along the years scamming and harming people's lives due to the increasing fear in society to this disease.")
st.write("The objective of this web page is to provide and user-friendly interface in where you will be able to check the probability of developing lung cancer related to your daily habits.")
st.write("This interface is connected to a classification Machine Learning model. In the Data base section, you can find in the left side you can find the database and the data analysis performed for this predictor")

st.write("# Formulary :clipboard:")
st.write("To predict your lung cancer probability you just have to fill the following formulary:")

st.write("Do you live in a polluted place? :house_with_garden:")
polutionst= st.radio(
	"Choose one of the following:",
	("Countryside","Village","Small town","Big town", "Samll city","Big city","Very polluted city (ex.Pekin)"))

if polutionst=="Countryside":
	polution=1
elif polutionst=="Small town":
	polution=2
elif polutionst=="Big town":
	polution=3
elif polutionst=="Small city":
	polution=5
elif polutionst=="Big city":
	polution=6
else:
	polution=8


st.write("How many times do you consume alcohol a day? :beer:")
alcohol = st.number_input("Insert the number",0)
if alcohol > 8: 
	alcohol=8
elif alcohol ==0:
	alcohol=1

st.write("How sensible are you to dust?")
dust = st.slider("Select between 1 (no problem) and 8 (sever allergy)", min_value=1, max_value=8, step=1)

st.write("Are you exposed to any hazard in your daily work? :biohazard_sign:")
hazardst = st.radio("Select one",
	("None","High or Low temperatures","Biological hazard","Smoke","Radiation","Other"))
if hazardst=="None":
	hazard=1
elif hazardst=="High or Low temperatures":
	hazard=2
elif hazardst=="Biological hazard":
	hazard=3
elif hazardst=="Smoke":
	hazard=4
elif hazardst=="Radiation":
	hazard=6
elif hazardst=="Other":
	hazard=2
else:
	st.write("Please select one above")

st.write("Any of your family members has a previous history of cancer?")
genetic = st.number_input("Not unrelated family mebers",0)
if genetic > 8:
	genetic=8
elif genetic==0:
	genetic=1

st.write("Do you suffer any sever chronic lung disease")
chronic = st.slider("Choose a value between 1 (Non or not important) to 8 (Several or very relevant)", min_value=1, max_value=8, step=1)

st.write("Is your diet balanced? :broccoli:")
dietst = st.select_slider("Select based on the quality and quantity of food you regularly consume",
	 ["Healthy","Balanced","Not conscious","Usually fats food","Unhealthy"])
if dietst=="Healthy":
	diet=1
elif dietst=="Balanced":
	diet=2
elif dietst=="Not conscious":
	diet=3
elif dietst=="Usually fats food":
	diet=5
elif dietst=="Unhealthy":
	diet=7
else:
	st.write("Please select one above")

st.write("What is your weight range")
obesityst= st.selectbox("Select the range in where you moved the last 2 months",
	('40-60', '60-75', '75-90', '90-100', '100-110','110-120','120-130',"More than 130" ))

if obesityst=='40-60':
	obesity=1
elif obesityst=='60-75':
	obesity=1
elif obesityst=='75-90':
	obesity=2
elif obesityst=='90-100':
	obesity=3
elif obesityst=='100-110':
	obesity=4
elif obesityst=='110-120':
	obesity=5
elif obesityst=='120-130':
	obesity=6
elif obesityst=="More than 130":
	obesity=7
else:
	st.write("Please select one above")

st.write("Are you a usual smoker? 	:smoking:")
smokingst = st.radio("Choose how regular you smoke",
	("Never","Rarely","Once a month","Usually", "Several days a week", "Every day"))

if smokingst=="Never":
	smoking=1
elif smokingst=="Rarely":
	smoking=2
elif smokingst=="Once a month":
	smoking=3
elif smokingst=="Usually":
	smoking=4
elif smokingst=="Several days a week":
	smoking=6
elif smokingst=="Every day":
	smoking=8
else:
	st.write("Please select one above")

st.write("And are you an usual passive smoker?")
passivest =st.radio("Choose one",
	("Never","Rarely","Once a week","Usually", "Several days a week", "Every day"))

if passivest=="Never":
	passive=1
elif passivest=="Rarely":
	passive=2
elif passivest=="Once a week":
	passive=3
elif passivest=="Usually":
	passive=4
elif passivest=="Several days a week":
	passive=6
elif passivest=="Every day":
	passive=8
else:
	st.write("Please select one above")

st.write("When you suffer from chest pain, how intense is it?")
chest = st.slider("Choose between 1(Don't have usually) and 8(Regular and heavy pain)",min_value=1, max_value=8, step=1)

st.write("Have you ever coughed blood?")
coughing =st.number_input("Insert as many times as you remember:",0)

if coughing > 8:
	coughing=8
elif coughing ==0:
	coughing=1

st.write("Do you usually feel fatigated? 	:sleeping:")
fatigest= st.select_slider(
	"Select one",
	["Never","Rarely","Once a week","Usually", "Several days a week", "Every day"])

if fatigest=="Never":
	fatige=1
elif fatigest=="Rarely":
	fatige=2
elif fatigest=="Once a week":
	fatige=3
elif fatigest=="Usually":
	fatige=4
elif fatigest=="Several days a week":
	fatige=6
elif fatigest=="Every day":
	fatige=8
else:
	st.write("Please select one above")

def predict():
	row = np.array([polution,alcohol,dust,hazard,genetic,chronic,diet,obesity,smoking,passive,chest,coughing,fatige])
	X=pd.DataFrame([row])
	prediction = model2.predict(X)

	if prediction [0] == "Low":
			st.success("Congratulations, you have a low probability of haveing cancer")
	elif  prediction [0] == "Medium":
			st.warning("Take care, you have a medium probability of haveing cancer. You should improve your habits")
	elif prediction [0] == "High":
			st.error("Your probability of having cancer is High. You should visit a doctor in case you fell sick to have a clear result.")
	else:
		st.error("Error")
		st.write(row)
		st.write(prediction)

but1=st.button("Predict", on_click=predict)

if but1:
	st.write("The formulary has been submitted. You can find the results at the top of this web page.")
	st.write("Remember you should not fully trust any web page that predicts if you have cancer and the best option if you feel sick is to visit a doctor.")
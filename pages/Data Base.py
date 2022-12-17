import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("# Data base and it's analisis :bar_chart:")
st.sidebar.markdown("Data Base")
st.markdown("In this page we will show the database and the different features we took into acount")
	
df = pd.read_excel(
	io="cancer patient data sets.xlsx",
	engine="openpyxl")
st.dataframe(df,1000)

st.write("# Description")
st.write("In the data frame above you can explore the different data values.")
st.write("This data was obtained from Kaggle. The acknowledgements indicates that the data comes from: https://data.world/cancerdatahp/lung-cancer-data/workspace/file?filename=cancer+patient+level%20data+sets.xlsx.")
st.write("In a quick look we can see that the values of the data move from 1 (low or unfrequently) to 8 (high or frequent).")
st.write("In the main page we have change these values to a format more user friendly to augment the engagement with the user.")

st.write("# Data Analysis")
st.write("Also we can see that it is composed of 25 different categories where the last one is the level probability of cancer.")
st.write("After plotting and analysing the different categories we could be sure that on one hand the dataset is balanced in the number of levels of cancer and gender:")

levele= Image.open('Level by Age.png')
st.image(levele, caption='Level of cancer by Age')

agee= Image.open('Level Count.png')
st.image(agee, caption='Level of cancer agains the age of the patient')

st.write("Some other data has been also plotted to be sure that the data is balance and can be find in the code of the ML program.")
st.write("To reduce the number of features, we have performed a score analysis to check what variables contribute the most to our cancer varibale:")

feat= Image.open('Feature Importance.png')
st.image(feat, caption='Score of the different features')

st.write("Form the data above we have only taken into account the data that scored over 200 as they are the most relevant.")

st.write("# Fallbacks")
st.write("As shown in the code of the ML, the SVM model predicts the probability with maximum accuracy due to the simplicity of the data and the size of the data base.")
st.write("The fallbacks introduced are related to the interface and can be found in the code of the main page.")
st.write("They are implemented in case the user introduces a variable that the system can not understand and a message is shown on screen asking for a valid value. ")

st.write("# Heroku:")
st.write("This web page was successfully deployed in Heroku during the practical session in Perugia. In the Git Hub repository you can find the necessary files used.")
st.write("As Heroku is no longer a free service I have tried to deploy using Google Cloud service.")
st.write("The problem I found when using this service is that a credit card is mandatory, and a debit card is not allowed. This disables me from using this service.")
st.write("Heroku was an easy and straightforward platform for the deployment of the web page where I just needed to create three different files to run it.")
st.write("The first one was setup.sh, file for the configuration, second the Procfile. where we include the name of the main page: Practica.py and third requirements.txt with the streamlit version.")
st.write("Even do these advantages, Heroku has the problem that it was slow when you want to access the web page ( around 1 minute to charge).")
st.write("This indicates that if the webpage is used buy even a not relatively high number of people (50 or hundred people at the same time) probably the server will collapse.")
st.write("If this where the case the best option we have is to use other services like Microsoft IIS or HTTP Apache to deploy the web page that will provide a better infrastructure but will have a monthly cost.")
st.write("Git Hub repository with the files for this app: https://github.com/DavidVarasR/Handson.")
st.write("Link obtained for the Heroku web page when it was free (not working now as explained): https://mastertccmreal.herokuapp.com/")
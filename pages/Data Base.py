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

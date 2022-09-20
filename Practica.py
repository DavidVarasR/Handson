import streamlit as st

st.title("My first Ml APP")
st.markdown("Main Page")
st.sidebar.markdown("Main page")

st.write("Hello world")

but1=st.button("Como me van a ir las practicas?")
if but1:
	from PIL import Image
	image = Image.open('pepowhy.png') 
	st.image(image,caption='buahsoy yo literal')

else:
	st.write("bye :wave:")

#but2=st.button("Pero, ¿y el bicho?")
#if but2:

#else
# st.write("¿el bicho?")

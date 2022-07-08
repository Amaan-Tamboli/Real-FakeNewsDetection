import streamlit as st
import joblib
model = joblib.load('Real-Fake')
st.title('Real-Fake News Detection')
ip = st.text_input('Enter the message : ')
st.subheader('Note:- ')
st.caption('The input format should be : title - text')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])

import streamlit as st
import time
import plotly.express as px 
st.header("my first app ")
st.sidebar.title("calculate Area app 1")
name = st.text_input("enter your name")
btn=st.button("show")
if btn:
    st.write("hello",name)

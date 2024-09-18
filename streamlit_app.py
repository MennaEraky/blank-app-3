import streamlit as st
import time
st.header("my first app ")
st.sidebar.title("calculate Area app 1")
name = st.text_input("enter your name")
btn=st.button("show")
if btn:
    st.write("hello",name)
#app 1
area=None
#st.header("calculate Area")

with st.sidebar:
  choose=st.selectbox('choose the shape',['circle','rectangle'])
  if choose == 'circle':
      r=st.number_input("enter the radius",min_value=1,max_value=100)
      area=r*r*3.14
      st.write("area of circle is",area)
  elif choose == 'rectangle':
      w=st.number_input("enter the width",min_value=1,max_value=100)
      h=st.number_input("enter the highet",min_value=1,max_value=100)
      area=w*h
      st.write("area of rectangle is",area)

  btn=st.button('calculate')
  if btn:
      with st.spinner('calculating...'):
        time.sleep(5)
      st.write("the area is",area)
#app 2
import pandas as pd
st.header("file upload app2")
file = st.file_uploader("upload a file",type=['csv'])
if file is not None:
  df=pd.read_csv(file)
  st.write(df)
num_row=st.slider('choose num rows',min_value=0,max_value=len(df),step=1)
names_col=st.multiselect('choose names of columns',df.columns.to_list())
st.write(df[:num_row][names_col])

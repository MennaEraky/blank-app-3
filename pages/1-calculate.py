import streamlit as st
st.header("session state ")
if 'fruits' not in st.session_state:
  st.session_state.fruits=[]
item = st.text_input("add item")
btn=st.button("add")
if btn:
    st.session_state.fruits.append(item)
st.write(st.session_state.fruits)

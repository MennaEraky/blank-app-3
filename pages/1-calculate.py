import streamlit as st
st.header("session state ")
item = st.text_input("add item")
st.session_state.fruits=[]
btn=st.button("add")
if btn:
    st.session_state.fruits.append(item)
st.write(st.session_state.fruits)

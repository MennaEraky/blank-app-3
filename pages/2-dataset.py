import streamlit as st
import time
import plotly.express as px 


#app 2
import pandas as pd
st.header("file upload app2")
file = st.file_uploader("upload a file",type=['csv'])
if file is not None:
    df=pd.read_csv(file)
    st.write(df)
    num_row=st.slider('choose num rows',min_value=0,max_value=len(df),step=1)
    names_col=st.multiselect('choose names of columns',df.columns.to_list())
    if names_col:
      st.write(df[:num_row][names_col])
    else:
      st.write(df[:num_row])
    num_col=df.select_dtypes(include='number').columns.to_list()
    
    tab1,tab2=st.tab(['scatter','histogram'])
    with tab1:
        col1,col2,col3=st.columns(3)
        with col1:
          x_col=st.selectbox('choose x axis',num_col)
        with col2:
          y_col=st.selectbox('choose y axis',num_col)
        with col3:
          color=st.selectbox('choose color',num_col)
    
        fig=px.scatter(df,x=x_col,y=y_col,color=color)
        st.plotly_chart(fig)
    with tab2:
        st.selectbox('choose value',num_col)
        fig2=px.histogram(df,x=num_col)
        st.plotly_chart(fig2)

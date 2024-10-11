import streamlit as st
import pandas
st.set_page_config(layout = "wide")


col1,col2 = st.columns(2)

with col1:
    st.image("image/file.png")

with col2:
    st.title("Himanshu")
    content = """
    Hi, Iam Hiamnshu! Himanshu Rana graduated 
    with a B.Tech degree in 2022. 
    After graduation, he completed a course 
    in Data Science and Machine Learning. 
    He is now equipped with skills to pursue 
    opportunities in the tech industry.
"""  
    st.info(content)

content2 = """
Blow yo can find some of the apps I have built in python.feel free to contact me!
"""
st.write(content2)

col3,col4 = st.columns(2)

df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df.iterrows():
        st.header(row["title"])


with col4:
    for index,row in df.iterrows():
        st.header(row["title"])

import streamlit as st

st.title("Streamlit text input")

name = st.text_input("Enter your name : ")
age = st.slider("Enter your age : ",10,80,25)

language = st.selectbox("What is your favourite programming language?",["Python","Javascript","C++","Java"])

if name:
    st.write(f'Hello {name}')
    st.write(f"Your age is {age}")
    st.write(f'Your favourite language is {language}')

import streamlit as st
import numpy as np
import pandas as pd

# Title of the application here
st.title("Hello by streamlit")

# For displaying a simple text
st.write("Kya haal bhai? ye hai ek simple text")

# Creating a simple dataframe
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

# Displaying the dataframe
st.write("Here is the dataframe : ")
st.write(df)

# Creating chart data
chart_data= pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
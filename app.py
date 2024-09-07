#to run open the terminal
# streamlit run app.py
import streamlit as st
import pandas as py
import numpy as np
import plotly.express as px

#set pandas plotting backend to plotly
pd.options.plotting.backend ="plotly"

@st.cache_data
def load_dataset():
    return pd.read_csv("datasets/canada_clean.csv")

st.title("Canada analysis")

with st.spinner("loading data..."):
    df=load_dataset()
    st.balloons()

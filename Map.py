import pandas as pd  #we need pandas for dataframes,  pip install pandas
# import plotly.express as px  #we need ploty for graphs, pip install plotly-express
import matplotlib.pyplot as plt
import streamlit as st  #we need streamlit for visualisation, pip install streamlit
import seaborn as sns
import sqlite3

st.set_page_config(
    page_title="Question_1",
    layout="wide",
    page_icon="Resources/Logo.jpg"
)


#DB----------------------------------------------
@st.cache
def get_data_low(path):
  df = pd.read_csv(path,low_memory=False)
  return df

df_address = get_data_low('CSV/address.csv')

#SIDEBAR------------------------------------------
st.sidebar.header("Crossroads Bank for Enterprises")

#FILTER A
filter_A = st.sidebar.multiselect(  #Variable defirnition
    "By Country:",  #Title of the filter
    options=['Belgium','France','Germany','Nederlands'],
    default=['Belgium','France','Germany','Nederlands']
    #options=df["Classification"].unique(),  #Column to filter
    #default="ANCI"  #Set default value to all
)

#FILTER A
filter_B = st.sidebar.multiselect(  #Variable defirnition
    "By Zipcode:",  #Title of the filter
    options=[1180,1000,3102],
    default=[1180,1000,3102]
    #options=df["Classification"].unique(),  #Column to filter
    #default="ANCI"  #Set default value to all
)


st.markdown("#### Companies by Foreing Country")
st.markdown("""
#### Remarks
Netherlands is the country with most active companies in Belgium, followed by France, Germany, UK, and Luxemburg.
""")
st.markdown('---')
st.image('Resources/Screenshot from 2022-10-28 14-44-25.png')
col_a, col_b = st.columns(2)
with col_a:
    st.dataframe(df_address)
with col_b:
    st.image('Resources/map.png')


import pandas as pd  #we need pandas for dataframes,  pip install pandas
# import plotly.express as px  #we need ploty for graphs, pip install plotly-express
import streamlit as st  #we need streamlit for visualisation, pip install streamlit
import seaborn as sns
import sqlite3

#VIEW--------------------------------------------
st.set_page_config(
    page_title="SQL Dashboard", #Web page title
    page_icon=":bar_chart:", #Web page icon
    layout="wide")  #Web page layout

#DB----------------------------------------------
@st.cache
def get_data():
  df = pd.read_csv('CSV/activity.csv')
  return df

df = get_data()

#SIDEBAR------------------------------------------

#Filter setup
#FILTER HEADER
st.sidebar.header("Filter data")

#FILTER A
filter_classification = st.sidebar.multiselect(  #Variable defirnition
    "By Classification:",  #Title of the filter
    options=df["Classification"].unique(),  #Column to filter
    default="ANCI"  #Set default value to all
)

#FILTER B
filter_activity = st.sidebar.multiselect(  #Variable defirnition
    "By Activity group:",  #Title of the filter
    options=df["ActivityGroup"].unique(),  #Column to filter
    default=df["ActivityGroup"].unique()  #Set default value to all
)

#FILTER C
filter_NaceVersion = st.sidebar.multiselect(  #Variable defirnition
    "By Nace version:",  #Title of the filter
    options=df["NaceVersion"].unique(),  #Column to filter
    default=df["NaceVersion"].unique()  #Set default value to all
)




#FILTERED INFORMATION-----------------------------
#Filtered information
df_filtered_data = df.query(
    "Classification == @filter_classification & ActivityGroup == @filter_activity & NaceVersion == @filter_NaceVersion"
)

#MAIN PAGE----------------------------------------

#Title
#st.title("SQL Dashboard")
st.markdown("# SQL Dashboard")
#st.markdown("## Title")
#st.markdown("* Description text")

#Section1-----------------------------------------
st.markdown('## Must-have features')
col_a, col_b, col_c, col_d = st.columns(4)
with col_a:
     st.markdown("### Question 1")
     st.markdown("**Which percentage of the companies are under which juridical form?**")
     st.markdown("Response")
with col_b:
     st.markdown("### Question 2")
     st.markdown("**Which percentage of the companies are under which Status?**")
     st.markdown("Response")
with col_c:
     st.markdown("### Question 3")
     st.markdown("**Which percentage of the companies are which type of entreprise?**")
     st.markdown("Response")
with col_d:
     st.markdown("### Question 4")
     st.markdown("**What is the average company's age in each sector (hint: look what is the NACE code)?**")
     st.markdown("Response")


st.markdown("---")
#Section2-----------------------------------------

#Hide streamlit style
st_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style> 
"""

st.markdown(st_style, unsafe_allow_html=True)

st.dataframe(df_filtered_data)  #returns the dataframe

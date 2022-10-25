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
st.markdown("## Title")
st.markdown("* Description text")

#Section1-----------------------------------------
col_a, col_b = st.columns(2)
with col_a:
     st.markdown("### Column A")
     st.markdown("* Description text")
     st.markdown("* Description text")
with col_b:
     st.markdown("### Column B")
     st.markdown("* Description text")
     st.markdown("* Description text")
#column_1, column_2, column_3 = st.columns(3)
#with column_1:
#    st.subheader("Total companies:")
#    st.subheader(f"#")
#with column_2:
#    st.subheader("?:")
#    st.subheader(f"?")
#with column_3:
#    st.subheader("average company's age in each sector")
#    st.subheader(f"years")

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

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
def get_data(path):
  df = pd.read_csv(path)
  return df

df = get_data('CSV/activity.csv')
df_activity = get_data('CSV/activity.csv')
df_code = get_data('CSV/code.csv')
df_enterprise = get_data('CSV/enterprise.csv')

df_enterprise['PercentageQ1'] = 1 / df_enterprise.shape[0]

#Question1--------------------------------------
df_q1 =  df_enterprise.groupby('JuridicalForm').sum().sort_values(by='PercentageQ1',ascending=False)

df_JuridicalForm = df_code.loc[(df_code['Category'] == 'JuridicalForm') & (df_code['Language'] == 'FR')]
df_JuridicalForm = df_JuridicalForm.rename(columns ={'Category':'Category','Code':'JuridicalForm','Language':'Language','Description':'Description'})
df_JuridicalForm = df_JuridicalForm.drop(columns=['Category','Language'],axis=1)
df_JuridicalForm['JuridicalForm'] = df_JuridicalForm['JuridicalForm'].astype(int)

df_q1 = pd.merge(df_q1, df_JuridicalForm,
    how='left', on='JuridicalForm')

df_q1 = df_q1[['JuridicalForm','Description','PercentageQ1']]

result_q1 = df_q1

#Question2--------------------------------------

df_q2 = df_enterprise
df_q2 = df_q2['Status'].value_counts()

result_q2 = df_q2

#Question3--------------------------------------

df_q3 = df_enterprise
df_q3 = df_q3.groupby('TypeOfEnterprise').sum().sort_values(by='PercentageQ1',ascending=False)

result_q3 = df_q3

#Question4--------------------------------------

df_q4 = df_activity
#Lose the Nace 2003 from the table
df_q4 = df_q4.query('NaceVersion == 2008') 
df_q4_enterprise = df_enterprise.drop(["Status","JuridicalSituation","TypeOfEnterprise","JuridicalForm"], axis=1)
df_q4_enterprise['age'] = pd.Timestamp('now') - (pd.to_datetime(df_q4_enterprise['StartDate'], format='%Y-%m-%d %H:%M:%S'))
df_q4_enterprise['age'] = df_q4_enterprise['age'].astype("timedelta64[D]")/ 365.2425
df_q4_enterprise = df_q4_enterprise.drop(['StartDate','PercentageQ1'], axis=1)
df_q4_enterprise = df_q4_enterprise.rename(columns={'EnterpriseNumber':	'EntityNumber','age':'age'})
df_q4 = pd.merge(df_q4, df_q4_enterprise,
    how='left', on='EntityNumber')
df_q4 = df_q4.dropna(subset='age')
df_q4['Nace_xx'] = df_q4['NaceCode'].apply(lambda x : str(x)[:2])
df_Nace2008 = df_code.loc[(df_code['Category'] == 'Nace2008') & (df_code['Language'] == 'FR')]
df_Nace2008 = df_Nace2008.drop(columns=['Category','Language'],axis=1)
df_Nace2008 = df_Nace2008.loc[(df_Nace2008['Code'].str.len() == 2)]
df_Nace2008 = df_Nace2008.rename(columns={'Code':'Nace_xx','Description':'Description'})
df_q4 = df_q4.groupby('Nace_xx').mean().sort_values(by='age',ascending=False)
df_q4 = pd.merge(df_q4, df_Nace2008,
    how='left', on='Nace_xx')

result_q4 = df_q4


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
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("### Question 1")
    st.markdown("**Which percentage of the companies are under which juridical form?**")
    st.markdown("Response")
    st.dataframe(result_q1)
with col_b:
    st.markdown("### Question 2")
    st.markdown("**Which percentage of the companies are under which Status?**")
    st.markdown("Response")
    st.dataframe(result_q2)

#Section2-----------------------------------------
st.markdown('## Must-have features')
col_c, col_d = st.columns(2)
with col_c:
    st.markdown("### Question 3")
    st.markdown("**Which percentage of the companies are which type of entreprise?**")
    st.markdown("Response")
    st.dataframe(result_q3)
with col_d:
    st.markdown("### Question 4")
    st.markdown("**What is the average company's age in each sector (hint: look what is the NACE code)?**")
    st.markdown("Response")
    st.dataframe(result_q4)


st.markdown("---")
#Section3-----------------------------------------

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

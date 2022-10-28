import pandas as pd  #we need pandas for dataframes,  pip install pandas
# import plotly.express as px  #we need ploty for graphs, pip install plotly-express
import streamlit as st  #we need streamlit for visualisation, pip install streamlit
import seaborn as sns
import sqlite3

st.set_page_config(
    page_title="Question_4",
    layout="wide",
    page_icon="Resources/Logo.jpg"
)

#DB----------------------------------------------
@st.cache
def get_data(path):
  df = pd.read_csv(path)
  return df

df_activity = get_data('CSV/activity.csv')
df_code = get_data('CSV/code.csv')
df_enterprise = get_data('CSV/enterprise.csv')

df_enterprise['Percentage'] = 100 / df_enterprise.shape[0]

#Question4--------------------------------------

df_q4 = df_activity
#Lose the Nace 2003 from the table
df_q4 = df_q4.query('NaceVersion == 2008') 
df_q4_enterprise = df_enterprise.drop(["Status","JuridicalSituation","TypeOfEnterprise","JuridicalForm"], axis=1)
df_q4_enterprise['age'] = pd.Timestamp('now') - (pd.to_datetime(df_q4_enterprise['StartDate'], format='%Y-%m-%d %H:%M:%S'))
df_q4_enterprise['age'] = df_q4_enterprise['age'].astype("timedelta64[D]")/ 365.2425
df_q4_enterprise = df_q4_enterprise.drop(['StartDate','Percentage'], axis=1)
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
st.sidebar.header("Crossroads Bank for Enterprises")

#FILTER A
filter_A = st.sidebar.multiselect(  #Variable defirnition
    "By Filter A:",  #Title of the filter
    options=result_q4['Description'].unique(),
    default=['Administration publique et défense; sécurité sociale obligatoire',"Captage, traitement et distribution d'eau",'Activités des organisations et organismes extraterritoriaux']
    #options=df["Classification"].unique(),  #Column to filter
    #default="ANCI"  #Set default value to all
)

#PAGE CONTENT-------------------------------------
st.markdown("## Q4_What is the average company's age in each sector?")
st.markdown("""
#### Remarks
Most companies were created after 2000
""")    
st.markdown('---')
st.markdown("#### Average Age")
st.dataframe(result_q4)
# col_a, col_b = st.columns(2)
# with col_a:
#     st.markdown("#### Table name")
#     st.dataframe(result_q4)
# with col_b:
#     st.markdown("#### Chart title")
#     st.markdown("Response")




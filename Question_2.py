import pandas as pd  #we need pandas for dataframes,  pip install pandas
# import plotly.express as px  #we need ploty for graphs, pip install plotly-express
import matplotlib.pyplot as plt
import streamlit as st  #we need streamlit for visualisation, pip install streamlit
import seaborn as sns
import sqlite3


st.set_page_config(
    page_title="Question_2",
    layout="wide",
    page_icon="Resources/Logo.jpg"
)

#DB----------------------------------------------
@st.cache
def get_data(path):
  df = pd.read_csv(path)
  return df

df_enterprise = get_data('CSV/enterprise.csv')
df_code = get_data('CSV/code.csv')

df_enterprise['Percentage'] = 100 / df_enterprise.shape[0]

#Question2--------------------------------------

df_q2 = df_enterprise
df_q22 = df_q2['Status'].value_counts()

result_q2 = df_q22

df_JuridicalSituation =  df_enterprise.groupby('JuridicalSituation').sum().sort_values(by='Percentage',ascending=False)

df_JuridicalSituation =  df_enterprise.groupby('JuridicalSituation')['Percentage'].sum().sort_values(ascending=False)

df_JuridicalSituation = df_code.loc[(df_code['Category'] == 'JuridicalSituation') & (df_code['Language'] == 'FR')]
df_JuridicalSituation = df_JuridicalSituation.rename(columns ={'Category':'Category','Code':'JuridicalSituation','Language':'Language','Description':'Description'})
df_JuridicalSituation = df_JuridicalSituation.drop(columns=['Category','Language'],axis=1)
df_JuridicalSituation['JuridicalSituation'] = df_JuridicalSituation['JuridicalSituation'].astype(int)

df_q2 = pd.merge(df_q2, df_JuridicalSituation,
    how='left', on='JuridicalSituation')

df_q2_JuridicalSituation = df_q2.groupby('Description')['Percentage'].sum().sort_values(ascending=False)


#SIDEBAR------------------------------------------
st.sidebar.header("Crossroads Bank for Enterprises")

#FILTER A
filter_Description = st.sidebar.multiselect(  #Variable defirnition
    "By Juridical Situation:",  #Title of the filter
    options=df_q2['Description'].unique(),
    default=['Situation normale',
             'Ouverture de faillite',
             'Dissolution anticipée - Liquidation (dissolution volontaire)']
)

#FILTERED INFORMATION-----------------------------
#Filtered information
df_filtered_data = df_q2.query(
    "Description == @filter_Description")

#PAGE CONTENT-------------------------------------
st.markdown("## Q2_Which percentage of the companies are under which Status?")
st.markdown("""
#### Remarks
Of all the enterprises with active status, 94.2% are in a normal juridical situation. The rest are primarily enterprises that have entered bankruptcy proceedings (4%) or are being voluntarily dissolved (1.4%). The remaining ones (0.39%) are split across 16 other types of juridical situations, all related to business actually ending.
""")
st.dataframe(result_q2)    
st.markdown('---')
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("#### Companies by Juridical situation")
    st.dataframe(df_filtered_data)
with col_b:
    st.markdown("#### Enterprises split by Juridical Situation")
    st.image('Resources/outputQ2a.png')




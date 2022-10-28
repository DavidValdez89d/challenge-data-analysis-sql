import pandas as pd  #we need pandas for dataframes,  pip install pandas
# import plotly.express as px  #we need ploty for graphs, pip install plotly-express
import streamlit as st  #we need streamlit for visualisation, pip install streamlit
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3


st.set_page_config(
    page_title="Question_3",
    layout="wide",
    page_icon="Resources/Logo.jpg"
)

#DB----------------------------------------------
@st.cache
def get_data(path):
  df = pd.read_csv(path)
  return df

df_enterprise = get_data('CSV/enterprise.csv')

df_enterprise['Percentage'] = 100 / df_enterprise.shape[0]

#Question3--------------------------------------

df_q3 = df_enterprise
df_q3 = df_q3.groupby('TypeOfEnterprise').sum().sort_values(by='Percentage',ascending=False)

result_q3 = df_q3

#SIDEBAR------------------------------------------
st.sidebar.header("Crossroads Bank for Enterprises")

# #FILTER A
# filter_A = st.sidebar.multiselect(  #Variable defirnition
#     "By Filter A:",  #Title of the filter
#     options=['A','B','C'],
#     default=['A','B','C']
#     #options=df["Classification"].unique(),  #Column to filter
#     #default="ANCI"  #Set default value to all
# )

#Chart--------------------------------------------


#PAGE CONTENT-------------------------------------
st.markdown("## Q3_Which percentage of the companies are which type of entreprise?")
st.markdown("""
#### Remarks
About 59% of enterprises are corporations, the remaining 41% are physical persons. Contrarily to corporations, physical persons don't have defined juridical forms.
""")
   
st.markdown('---')

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("#### Enterprises split by type")
    st.dataframe(result_q3)
with col_b:
    st.markdown("#### Enterprises split by type")
    labels = ['Personne Morale','Personne Physique']
    sizes = [59.01646118804782,40.98353881195218]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)
    


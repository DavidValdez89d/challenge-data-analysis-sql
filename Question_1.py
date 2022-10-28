import pandas as pd  #we need pandas for dataframes,  pip install pandas
# import plotly.express as px  #we need ploty for graphs, pip install plotly-express
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
def get_data(path):
  df = pd.read_csv(path)
  return df

df_activity = get_data('CSV/activity.csv')
df_code = get_data('CSV/code.csv')
df_enterprise = get_data('CSV/enterprise.csv')

df_enterprise['Percentage'] = 100 / df_enterprise.shape[0]

#Question1--------------------------------------
df_q1 =  df_enterprise.groupby('JuridicalForm').sum().sort_values(by='Percentage',ascending=False)

df_JuridicalForm = df_code.loc[(df_code['Category'] == 'JuridicalForm') & (df_code['Language'] == 'FR')]
df_JuridicalForm = df_JuridicalForm.rename(columns ={'Category':'Category','Code':'JuridicalForm','Language':'Language','Description':'Description'})
df_JuridicalForm = df_JuridicalForm.drop(columns=['Category','Language'],axis=1)
df_JuridicalForm['JuridicalForm'] = df_JuridicalForm['JuridicalForm'].astype(int)

df_q1 = pd.merge(df_q1, df_JuridicalForm,
    how='left', on='JuridicalForm')

df_q1 = df_q1[['JuridicalForm','Description','Percentage']]

result_q1 = df_q1


#SIDEBAR------------------------------------------
st.sidebar.header("Crossroads Bank for Enterprises")

#FILTER A
filter_Description = st.sidebar.multiselect(  #Variable defirnition
    "By Juridical Form:",  #Title of the filter
    options=df_q1['Description'].unique(),  #Column to filter
    default=['Société privée à responsabilité limitée',
             'Société à responsabilité limitée',
             'Association sans but lucratif',
             'Société anonyme',
             'Association des copropriétaires',
             'Entité étrangère',
             'Société en commandite simple',
             'Société ou association sans personnalité juridique',
             'Société en nom collectif',
             'Société en commandite'
            ]  #Set default value to all
)

#FILTERED INFORMATION-----------------------------
#Filtered information
df_filtered_data = result_q1.query(
    "Description == @filter_Description")

#Chart--------------------------------------------
#label_list = ['SPRL','SRL','ASBL','SA','ACP','EE','SCS','Sans personalité juridique','SNC']
# yticks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# chart = df_filtered_data['Percentage'].plot(kind='bar',figsize=(18,6),yticks=yticks, title = "Juridical forms representing more than 1 percent of enterprises in database", xlabel='Juridical Form',ylabel='Percentage (%)',grid=True,legend=True, label='Percentage')

#PAGE CONTENT-------------------------------------
st.markdown("## Q1_Which percentage of the companies are under which juridical form?")
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("#### Enterprises by JuridicalForm")
    st.dataframe(df_filtered_data)
with col_b:
    st.markdown("#### Enterprises split by Juridical form")
    # st.pyplot(fig=df_filtered_data, x='Description',y='Percentage')
    # st.image('Resources/outputQ1 (1).png')
    st.image('Resources/outputQ1.png')
    
# st.markdown('---')

# st.markdown("""
# #### Remarks
# text
# """)

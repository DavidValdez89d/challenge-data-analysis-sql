import streamlit as st

def run():
    st.set_page_config(
        page_title="References",
        layout="wide"
    )
    
    #Content of the page
    
    st.markdown("# About this project")
    st.markdown("""
    This is a **BeCode** proyect made by **Bouman 5 promotion!**
    * The scenario: *'You are a data analysis consultant at a big company that has just migrated their data to a SQL DB. Your mission is to help the company find business insights from the data that will help their grow their business.'*
    ### DataBase source:
    Crossroads Bank for Enterprises
    
    
    Enterprise SQL Data, taked from [Open data](https://economie.fgov.be/en/themes/enterprises/crossroads-bank-enterprises/services-everyone/public-data-available-reuse/cbe-open-data)
    * Total Rows : 19,515,324
    * Active Entreprises : 1,863,292
    ### Want to learn how we did it?
    Check out the project's [Github](https://github.com/DavidValdez89d/challenge-data-analysis-sql)
    """)
    st.image('Resources/Logo.jpg')

if __name__ == "__main__":
    run()

# #DB----------------------------------------------
# @st.cache
# def get_data(path):
#   df = pd.read_csv(path)
#   return df

# @st.cache
# def get_data_low(path):
#   df = pd.read_csv(path,low_memory=False)
#   return df
         
# df_activity = get_data('CSV/activity.csv')
# df_address = get_data_low('CSV/address.csv')
# df_branch = get_data('CSV/branch.csv')
# df_code = get_data('CSV/code.csv')
# df_contact = get_data('CSV/contact.csv')
# df_denomination = get_data('CSV/denomination.csv')
# df_enterprise = get_data('CSV/enterprise.csv')
# df_establishment = get_data('CSV/establishment.csv')
# df_meta = get_data('CSV/meta.csv')
    

# def give_info(data):

#     info = (pd.concat([data.dtypes,
#                    data.nunique(),
#                    data.isnull().sum(),
#                    data.isnull().sum()*100/len(data)],axis=1))
#     info = info.rename(columns={0:'Data types',
#                             1:'Uniques values', # amount of possible values , 'cardinality' of variable
#                             2:'Number of null Values',
#                             3:'Percentage of null values'}) # amount of null values

#     return info

# st.markdown("#### DB_Activity")
# col_a, col_b = st.columns(2)
# with col_b:
#     st.markdown(f"Rows:")# {df_activity.shape[0]}")
#     st.markdown(f"Columns:")# {df_activity.shape[1]}")
# with col_a:
#     st.markdown("""
#     | |       Data types | Uniques values | Number of null Values | Percentage of null values |
#     |-----------------:|---------------:|----------------------:|--------------------------:|-----------|
#     |     EntityNumber |         object |               2706922 |                         0 |  0.000000 |
#     |    TypeOfAddress |         object |                     3 |                         0 |  0.000000 |
#     |        CountryNL |         object |                   212 |                   2627222 | 97.055696 |
#     |        CountryFR |         object |                   210 |                   2627222 | 97.055696 |
#     |          Zipcode |         object |                 36593 |                     11156 |  0.412129 |
#     |   MunicipalityNL |         object |                 27577 |                       164 |  0.006059 |
#     |   MunicipalityFR |         object |                 27576 |                       164 |  0.006059 |
#     |         StreetNL |         object |                152361 |                      9039 |  0.333922 |
#     |         StreetFR |         object |                152631 |                      9039 |  0.333922 |
#     |      HouseNumber |         object |                 26549 |                     17140 |  0.633191 |
#     |              Box |         object |                 10256 |                   2361856 | 87.252459 |
#     | ExtraAddressInfo |         object |                 20977 |                   2677589 | 98.916371 |
#     |  DateStrikingOff |         object |                  3194 |                   2681095 | 99.045890 |
#     """)
# st.dataframe(give_info(df_activity))

# st.markdown("#### DB_Adress")
# st.dataframe(give_info(df_address))
# st.markdown("#### DB_Adress")
# st.dataframe(give_info(df_address))

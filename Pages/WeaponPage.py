
import streamlit as st
import pandas as pd
from Scraper import Scraper
from Weapon import Weapon
from Database import *

def app(args=None):
    listWeapons = getAllWeapons()
    df = pd.DataFrame(listWeapons)
    st.title("Weapons DanMachi : " + str(len(listWeapons)))

    #st.dataframe(df[["name", "owner", "description", "price", ""]])
    st.markdown('<a href="/?app=Add+Weapon" class="link" target="_self" style="text-decoration: none"> <button class="css-5uatcg edgvbvh10 buttons_link"> Add Weapon </button> </a>', unsafe_allow_html=True)
    colms = st.columns((2, 1, 2, 1, 1))
    fields = ["Name", 'Owner', 'Description', 'Price', "Action"]
    for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)

    for x,name in enumerate(df['name']):
        col1, col2, col3, col4, col5 = st.columns((2, 1, 2, 1, 1))
        print(df['name'][x])
        col1.write(df['name'][x]) 
        col2.write(df['owner'][x]) 
        col3.write(df['description'][x]) 
        col4.write(df['price'][x]) 
        button_phold = col5.empty()  
        removeButton = button_phold.button("Remove", key=x)
        if removeButton:
            RemoveById(df["_id"][x])
            df.drop(index=x)
            button_phold.text("Has been removed")  # remove button


    
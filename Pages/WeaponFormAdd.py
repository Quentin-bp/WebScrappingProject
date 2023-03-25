
import streamlit as st
from Database import *
from Weapon import Weapon



def app(args=None):
    st.markdown(' <a href="/?app=Home" class="link" target="_self" style="text-decoration: none"> <button class="css-5uatcg edgvbvh10 buttons_link">Home</button></a> ', unsafe_allow_html=True)
    with st.form("my_form"):
        st.text("")  # br
        nameInputWeapon = st.text_input("Name weapon")
        priceInputWeapon = st.number_input("Price weapon")
        ownerInputWeapon = st.text_input("Owner weapon")
        descriptionInputWeapon = st.text_input("Description weapon")
        st.text("")  # br
        submitted = st.form_submit_button("Add Weapon")
        if submitted:
            #start = "The weapon", nameInputWeapon # si on met ca comme ca, va afficher en style json...
            if findWeaponByName(nameInputWeapon):
                st.write("The weapon", nameInputWeapon," already exists, change his name !" )
            else:
                st.write("The weapon", nameInputWeapon, "has been added, comeback to Home !")            
                insertWeapon(Weapon(nameInputWeapon, ownerInputWeapon,priceInputWeapon, descriptionInputWeapon))


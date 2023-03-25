from Scraper import Scraper
from Database import *
import streamlit as st
from MultiPage import MultiPage
from Pages import WeaponPage, WeaponFormAdd


def local_css():
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


scraper = Scraper("https://danmachi.fandom.com/wiki/Items")


def loadApp():
    app = MultiPage()
    local_css()

    app.add_page("Home", WeaponPage.app)
    app.add_page("Add Weapon", WeaponFormAdd.app)

    app.run()

loadApp()
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 23:21:37 2023

@author: edwar
"""

#Import package
import streamlit as st
import pandas as pd

#Set titles and sidebar header
st.set_page_config(page_title="History of Past Seasons", page_icon="🏆")
st.title('Korbel Fantasy Football Past Seasons')
st.text("Here you will find league history from 2015-2022")


url = 'https://raw.githubusercontent.com/hankshackleford/KorbelFantasyApp/main/FF%20history.csv'
df = pd.read_csv(url)
print(df)


#Set year and position selectors
selected_yr = st.sidebar.selectbox('Year',list(reversed(range(2015,2024))))

df_selected =  df[(df.Year == selected_yr)]
st.dataframe(data=df_selected)


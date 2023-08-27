# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:19:37 2023

@author: edwar
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Korbel Fantasy League",
    page_icon="🏈",
)

st.write("# Welcome to the Official App of the Korbel Fantasy League.")
st.text('Select a page from the sidebar to get started.')


st.sidebar.success("Select a page above.")

#Read in data from Github
url = 'https://raw.githubusercontent.com/hankshackleford/KorbelFantasyApp/main/owner%20data.csv'
df_selected = pd.read_csv(url)
print(df_selected)

#setting palette
colors=['#1A8A41','#521052']

win_loss = px.bar(
    data_frame = df_selected,
    x = "Owner",
    y = ["Wins","Losses"],
    orientation = "v",
    barmode = 'group',
    color_discrete_sequence=colors,
    opacity= .8,
    title='Wins and Losses',
)
st.plotly_chart(win_loss)

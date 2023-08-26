# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 11:26:36 2023

@author: edwar
"""


#Import package
import streamlit as st
import pandas as pd
import plotly.express as px



#Set titles and sidebar header
st.set_page_config(page_title="Team Owners", page_icon="🐍")
st.title('Team Owners')
st.text("Find info on team owners here.")

#Read in data from Github
url = 'https://raw.githubusercontent.com/hankshackleford/KorbelFantasyApp/main/owner%20data.csv'
df_selected = pd.read_csv(url)
print(df_selected)

st.dataframe(data=df_selected, hide_index=True)

#setting palette
colors=['#1A8A41','#521052']

wins = px.bar(df_selected, x='Owner', y='Win Rate',
              opacity= .8,
              color_discrete_sequence=colors,
              title='Win Rate',)
st.plotly_chart(wins)



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

moves = px.bar(df_selected, x='Owner', y='Average Moves',
               color_discrete_sequence=colors,
              opacity=.8,
              title='Average Moves Per Season',)
st.plotly_chart(moves)
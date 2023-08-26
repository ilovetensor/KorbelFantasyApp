# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 23:21:37 2023

@author: edwar
"""

#Import package
import streamlit as st
import pandas as pd
import json

#Set titles and sidebar header
st.set_page_config(page_title="History of Past Seasons", page_icon="🏆")
st.title('Korbel Fantasy Football Past Seasons')
st.text("Walk these hallowed halls of winners and losers, and relive glory of past seasons.")


url = 'https://raw.githubusercontent.com/hankshackleford/KorbelFantasyApp/main/FF%20history.csv'
df = pd.read_csv(url)
print(df)
df.drop(df.columns[[12, 13, 14, 15, 16, 17, 18, 19]], axis=1, inplace=True)


#Set year and position selectors
selected_yr = st.sidebar.selectbox('Year',list(reversed(range(2015,2023))))
df_selected =  df[(df.Year == selected_yr)]

#Set min/max references for databars
pf_min=df_selected['PF'].min()
pf_max=df_selected['PF'].max()
pa_min=df_selected['PA'].min()
pa_max=df_selected['PA'].max()
pfg_min=df_selected['PF/G'].min()
pfg_max=df_selected['PF/G'].max()
pag_min=df_selected['PA/G'].min()
pag_max=df_selected['PA/G'].max()
diff_min=df_selected['DIFF'].min()
diff_max=df_selected['DIFF'].max()
#moves_min=df_selected['MOVES'].min()
#moves_max=df_selected['MOVES'].max()





#Data Editor
st.data_editor(
    df_selected,
    column_config={
        "Year": st.column_config.NumberColumn(
            "Year",
            format="%f"),
        "PF": st.column_config.ProgressColumn(
            "PF",
            help="Total Points For",
            format="%6.0f", min_value=pf_min,max_value=pf_max),
        "PA": st.column_config.ProgressColumn(
            "PA",
            help="Total Points Allowed",
            format="%6.0f", min_value=pa_min,max_value=pa_max),
        "PF/G": st.column_config.ProgressColumn(
            "PF/G",
            help="Average Points Per Game",
            format="%6.1f", min_value=pfg_min,max_value=pfg_max),
        "PA/G": st.column_config.ProgressColumn(
            "PA/G",
            help="Average Points Allowed Per Game",
            format="%6.1f", min_value=pag_min,max_value=pag_max),     
        "DIFF": st.column_config.ProgressColumn(
            "DIFF",
            help="Average Difference Between Points For and Allowed Per Game",
            format="%6.1f", min_value=diff_min,max_value=diff_max),
        #"MOVES": st.column_config.ProgressColumn(
         #   "MOVES",
          #  help="Total Number of Moves Made In Season",
           # format="%6.0f", min_value=moves_min,max_value=moves_max)         
        },
    hide_index=True,
    width=1500,
)

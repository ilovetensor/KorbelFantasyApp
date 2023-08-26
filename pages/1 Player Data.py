# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Import package
import streamlit as st
import pandas as pd

#Set titles and sidebar header
st.set_page_config(page_title="Player Data", page_icon="📊")
st.title('Fantasy Football Analytics: Player Data')
st.sidebar.header('User Selections')
st.text("Here you will find 2022 actual data (including a draft recap) as well as 2023 projections, supplied by FantasyPros")
st.text("This page also contains advanced statistics, explained further below")
st.text("VORP: Value Over Replacement Player: number of points greater or less than the median starter in their position")
st.text("VONA: Value Over Next Available: number of points greater than the next available starter in their position")
st.text("VOLA: Value Over Last Starter: number of points greater than the last starter in their position")


#Read in data
#df = pd.read_excel(r'C:/Users/edwar/FFL 23.xlsx', sheet_name='All')
#del df['NAME']
#df.set_index('PLAYER', inplace=True)
#print(df)

url = 'https://raw.githubusercontent.com/hankshackleford/KorbelFantasyApp/main/FF23_for_github.csv'
df = pd.read_csv(url)
print(df)


#Set year and position selectors
selected_yr = st.sidebar.selectbox('Year',list(reversed(range(2022,2024))))

unique_pos = ['QB', 'RB', 'WR', 'TE']
selected_pos = st.sidebar.multiselect('POS',unique_pos,unique_pos)


df_selected =  df[(df.Year == selected_yr)]
df_selected = df_selected[(df_selected.POS.isin(selected_pos))]

#Set min/max references for databars
ppg_min=df_selected['PPG'].min()
ppg_max=df_selected['PPG'].max()
tp_min=df_selected['Total Points'].min()
tp_max=df_selected['Total Points'].max()
vorp_min=df_selected['VORP'].min()
vorp_max=df_selected['VORP'].max()
vona_min=df_selected['VONA'].min()
vona_max=df_selected['VONA'].max()
vols_min=df_selected['VOLS'].min()
vols_max=df_selected['VOLS'].max()
dv_min=df_selected['Draft Value'].min()
dv_max=df_selected['Draft Value'].max()

#Data Editor
st.data_editor(
    df_selected,
    column_config={
        "Year": st.column_config.NumberColumn(
            "Year",
            format="%f"),
        "PPG": st.column_config.ProgressColumn(
            "PPG",
            help="Expected 2023 Points per Game",
            format="%6.1f", min_value=ppg_min,max_value=ppg_max),
        "Total Points": st.column_config.ProgressColumn(
            "Total Points",
            help="Expected 2023 Total Points",
            format="%6.0f", min_value=tp_min,max_value=tp_max),
        "Draft Value": st.column_config.NumberColumn(
            "Draft Value",
            format="$%f"),
        "VORP": st.column_config.ProgressColumn(
            "VORP",
            help="Value Over Replacement Player: number of points greater or less than the median starter in their position",
            format="%6.0f", min_value=vorp_min,max_value=vorp_max),
        "VONA": st.column_config.ProgressColumn(
            "VONA",
            help="Value Over Next Available: number of points greater than the next available starter in their position",
            format="%6.0f", min_value=vona_min,max_value=vona_max),     
        "VOLS": st.column_config.ProgressColumn(
            "VOLS",
            help="Value Over Last Starter: number of points greater than the last starter in their position",
            format="%6.0f", min_value=vols_min,max_value=vols_max)        
        },
    hide_index=True,
    width=2500,
    height=2500,
)

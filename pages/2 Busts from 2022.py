# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:12:07 2023

@author: edwar
"""

#Import package
import streamlit as st
import pandas as pd

st.set_page_config(page_title="2022 Busts", page_icon="🤢")
st.title('2022 Busts')

pd.set_option('display.max_colwidth', 0)



df = pd.read_excel(r'C:/Users/edwar/22 busts.xlsx')

df.style.set_properties(
    **{
        'inline-size': '1000px',
        'overflow-wrap': 'break-word',
    }, 
    subset='user_agent'
)

st.dataframe(df, hide_index=True)
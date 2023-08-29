import streamlit as st
from streamlit_lottie import st_lottie

with st.echo():
    st_lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

import winsound
# Play Windows exit sound.
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
winsound.PlaySound("*", winsound.SND_ALIAS)
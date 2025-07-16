import streamlit as st

if st.button('Click'):
    st.text(True)

if data:= st.camera_input("Click a Snap"): 
    st.download_button('Download Source data', data, "my.png")

# This page script will be placed inside the 'pages/' directory.

import streamlit as st

def load_page():
    st.set_page_config(page_title="Regression", page_icon="🔍")
    st.title("Regression Analysis 🔍")
    
    if 'uploaded_data' in st.session_state:
        data = st.session_state['uploaded_data']
        st.dataframe(data.head())
        # Add your regression logic here
    else:
        st.warning("Please upload data through the 'Upload Data 📤' page.")

if __name__ == "__main__":
    load_page()

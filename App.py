# This page script will be placed inside the 'pages/' directory.

import streamlit as st
import pandas as pd

def load_page():
    st.set_page_config(page_title="Upload Data", page_icon="📤")
    st.title("Upload Data 📤")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.session_state['uploaded_data'] = data
        st.success("Data successfully uploaded! 👍")
        st.dataframe(data.head())  # Optionally display a preview of the uploaded data

if __name__ == "__main__":
    load_page()

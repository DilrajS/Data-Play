import streamlit as st
from pages import home, classification, regression, clustering

# Function to setup the main page layout and navigation
def main():
    st.sidebar.title("Navigation")
    page_selection = st.sidebar.radio("Go to", ["Home", "Classification", "Regression", "Clustering"])

    if page_selection == "Home":
        home.load_page()
    elif page_selection == "Classification":
        classification.load_page()
    elif page_selection == "Regression":
        regression.load_page()
    elif page_selection == "Clustering":
        clustering.load_page()

if __name__ == "__main__":
    main()

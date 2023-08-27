import csv

import streamlit as st
import pandas as pd
import requests
from streamlit import session_state

# your-LOCAL-repository/
# ├── .streamlit/
# │   ├── config.toml
# │   └── secrets.toml # Make sure to gitignore this!
# ├── your_app.py
# └── requirements.txt


st.title("Data Viewer and Loader")

# def fetch_data():
#     spreadsheet_data = pd.read_excel("spreadsheet_data.xlsx")
#
#     gcp_data_response = requests.get("https://your-gcp-service-url/data")
#     gcp_data = gcp_data_response.json()
#
#     return "spreadsheet_data", "gcp_data"


# https://docs.google.com/spreadsheets/d/1I0_H8hj5XYjiv4Oo1oKO5eEmb7Lp7bmfY8v08BUEPw0/edit?usp=sharing

@st.cache_data
def load_csv():
    return pd.read_csv("all_seasons.csv", delimiter=",", encoding="UTF-8")

if st.button("Button #1"):
    session_state.button_1 = True

if st.button("Button #2") and session_state.button_1:
    print("hello world!")
    st.write("Button #2 clicked!")

    df = load_csv()

    st.subheader("Spreadsheet Data")
    st.dataframe(df)

    session_state.button_1 = False



    # st.subheader("GCP Data")
    # st.json(gcp_data)

    # if st.button("Load to RDB or BigQuery"):
    #     pass

import pandas as pd
import streamlit as st

# Load your dataset
df = pd.read_csv("sample_data.csv")  # change to your actual CSV name

# Show first 5 rows
st.dataframe(df.head())

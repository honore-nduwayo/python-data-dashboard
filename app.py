import pandas as pd
import streamlit as st
import plotly.express as px

# ---------------------------
# 1. Load Dataset
# ---------------------------
st.title("Python Data Dashboard")

# Replace with your CSV file name
DATA_PATH = "sample_data.csv"

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(DATA_PATH)

# ---------------------------
# 2. Show Raw Data
# ---------------------------
st.subheader("Raw Data")
st.dataframe(df.head())

# ---------------------------
# 3. Interactive Filters
# ---------------------------
st.subheader("Filter Data")

# Example: filter by a column named "Category"
if "Category" in df.columns:
    categories = df["Category"].unique().tolist()
    selected_categories = st.multiselect("Select Category", categories, default=categories)
    df = df[df["Category"].isin(selected_categories)]

# Example: filter by a numeric column named "Value"
if "Value" in df.columns:
    min_val, max_val = int(df["Value"].min()), int(df["Value"].max())
    selected_range = st.slider("Select Value Range", min_val, max_val, (min_val, max_val))
    df = df[df["Value"].between(selected_range[0], selected_range[1])]

st.subheader("Filtered Data")
st.dataframe(df)

# ---------------------------
# 4. Charts
# ---------------------------
st.subheader("Charts")

# Bar chart example: sum of Value per Category
if "Category" in df.columns and "Value" in df.columns:
    chart_data = df.groupby("Category")["Value"].sum().reset_index()
    fig = px.bar(chart_data, x="Category", y="Value", title="Sum of Value per Category")
    st.plotly_chart(fig)

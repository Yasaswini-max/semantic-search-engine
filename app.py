import streamlit as st
from model import create_index, search

st.set_page_config(page_title="Semantic Search", layout="centered")

st.title("🔍 Semantic Search Engine")

# Load data
@st.cache_data
def load_data():
    with open("data.txt", "r") as f:
        return f.read().split("\n")

data = load_data()

# Create index
@st.cache_resource
def load_index(data):
    return create_index(data)

index = load_index(data)

# UI
query = st.text_input("Enter your query")

if st.button("Search"):
    if query:
        result = search(query, data, index)
        st.subheader("Result:")
        st.success(result)

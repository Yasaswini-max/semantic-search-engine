import streamlit as st
from model import create_index, search

st.title("🔍 Semantic Search Engine")

# Load data
with open("data.txt", "r") as f:
    data = f.read().split("\n")

# Create index
index = create_index(data)

query = st.text_input("Enter your query")

if st.button("Search"):
    if query:
        result = search(query, data, index)
        st.subheader("Result:")
        st.write(result)

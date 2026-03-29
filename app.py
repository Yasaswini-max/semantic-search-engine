import streamlit as st
import requests

st.title("🔍 Semantic Search Engine")

query = st.text_input("Enter your query")

if st.button("Search"):
    if query:
        res = requests.post("http://127.0.0.1:8000/query", json={"query": query})
        data = res.json()
        
        st.subheader("Result:")
        st.write(data["result"])
# 🔍 Semantic Search Engine

## 📌 Overview

This project is an AI-powered semantic search engine that retrieves contextually relevant results based on user queries. Unlike traditional keyword-based search, it leverages sentence embeddings to understand the meaning of text.

---

## 🚀 Features

* 🔎 Semantic search using transformer-based embeddings
* ⚡ FastAPI backend for efficient API handling
* 🖥️ Interactive UI built with Streamlit
* 📊 Real-time query processing
* 🧠 Uses pre-trained NLP models for better accuracy

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Model:** Sentence Transformers
* **Libraries:** NumPy, Requests

---

## 🏗️ Project Structure

```
semantic-search/
│── main.py          # FastAPI backend
│── model.py         # Embedding + search logic
│── app.py           # Streamlit UI
│── requirements.txt # Dependencies
│── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/semantic-search-engine.git
cd semantic-search-engine
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run backend server

```
uvicorn main:app --host 127.0.0.1 --port 8000
```

### 4️⃣ Run frontend UI

```
streamlit run app.py
```

---

## 📷 Output

* Enter a query in the UI
* System returns semantically similar results

---

## 🎯 Future Improvements

* Add large-scale dataset
* Improve ranking using cosine similarity tuning
* Deploy using cloud (AWS / Render / Hugging Face Spaces)
* Enhance UI design

---

## 👩‍💻 Author

**Yasaswini Rao Medikonda**

---

## ⭐ Acknowledgment

This project uses pre-trained models from the Sentence Transformers library.

import os
import sqlite3
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyDkw0vutLQGQw--2ArkGi1e6Cld-gsE-ZU"))

# Connect to SQLite
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Streamlit UI
st.title("🔮 Gemini SQL Chatbot")

user_question = st.text_input("Ask something about your database:")

def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([
        "You are an assistant that converts natural language to SQL query.",
        f"Convert this to an SQLite SQL query: {prompt}. Only return SQL with no explanation."
    ])
    return response.text.strip()

if user_question:
    with st.spinner("Thinking..."):
        sql_query = ask_gemini(user_question)
        st.code(sql_query, language="sql")

        try:
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            st.success("Query executed successfully!")
            st.write(rows)
        except Exception as e:
            st.error(f"Error: {e}")

import streamlit as st
import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load Gemini API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Set up Streamlit page
st.set_page_config(page_title="SQL Chatbot", layout="wide")
st.title("💬 Natural Language to SQL Chatbot")
st.markdown("Upload your CSV file and ask any question in plain English. The chatbot will convert it to SQL and show results with analysis.")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Function to clean up SQL output
def clean_sql_code(code):
    return code.replace("```sql", "").replace("```", "").strip()

# If a file is uploaded
if uploaded_file:
    # Load CSV into pandas DataFrame
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Uploaded Data")
    st.dataframe(df, use_container_width=True)

    # Save to SQLite temporary in-memory database
    conn = sqlite3.connect(":memory:")
    df.to_sql("data", conn, index=False, if_exists="replace")
    cursor = conn.cursor()

    # Ask user for question
    user_question = st.text_input("Ask a question in English (e.g., 'What is the average age?')")

    def ask_gemini(prompt):
        response = model.generate_content(
            f"Convert this to SQLite SQL: {prompt}. The table name is 'data'. Only return SQL without explanation."
        )
        return response.text.strip()

    def analyze_output_with_gemini(question, rows, columns):
        if not rows:
            return "No data returned from query."

        df_result = pd.DataFrame(rows, columns=columns)
        csv_data = df_result.to_csv(index=False)

        response = model.generate_content(
            [
                {
                    "role": "user",
                    "parts": [
                        {
                            "mime_type": "text/plain",
                            "text": f"Based on the following SQL query result, answer the question: '{question}'.\n\n{csv_data}"
                        }
                    ]
                }
            ]
        )
        return response.text.strip()

    if user_question:
        with st.spinner("Thinking..."):
            raw_sql_query = ask_gemini(user_question)
            sql_query = clean_sql_code(raw_sql_query)
            st.code(sql_query, language="sql")

            try:
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                col_names = [desc[0] for desc in cursor.description]

                result_df = pd.DataFrame(rows, columns=col_names)
                st.success("✅ Query executed successfully!")
                st.dataframe(result_df, use_container_width=True)

                # Generate natural language analysis
                explanation = analyze_output_with_gemini(user_question, rows, col_names)
                st.subheader("📝 Analysis")
                st.write(explanation)

            except Exception as e:
                st.error(f"❌ Error: {e}")

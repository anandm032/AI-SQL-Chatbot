# AI SQL Chatbot 🤖💬

An AI-powered chatbot that converts natural language questions into SQL queries and retrieves data from a MySQL database.

The project allows users to interact with a database using simple English instead of manually writing SQL queries.

## 📌 Problem Statement

Writing SQL queries can be difficult for users who do not have technical knowledge of databases.

This project provides a simple AI-based interface where users can ask questions in natural language. The chatbot converts the question into an SQL query, executes it on the connected database, and displays the result.

## 🚀 Features

* Natural language to SQL query generation
* AI-powered query understanding
* MySQL database integration
* Automatic SQL query execution
* Interactive chatbot interface
* Displays database results directly to the user

## 🧠 How It Works

1. The user enters a question in natural language.
2. The AI model analyzes the user's question.
3. The question is converted into an SQL query.
4. The generated SQL query is executed on the MySQL database.
5. The query result is displayed to the user.

## 🔄 Workflow

User Question
↓
AI Model
↓
SQL Query Generation
↓
MySQL Database
↓
Query Execution
↓
Result Display

## 🛠️ Tech Stack

* Python
* MySQL
* Groq API
* Llama Model
* Streamlit
* SQL

## 📂 Project Structure

AI-SQL-Chatbot/

├── chatbot.py
├── requirement.txt
└── README.md

## ⚙️ Installation

### 1. Clone the Repository

git clone https://github.com/anandm032/AI-SQL-Chatbot.git

### 2. Move to the Project Directory

cd AI-SQL-Chatbot

### 3. Install Required Libraries

pip install -r requirement.txt

### 4. Configure the Database

Create a MySQL database and update the database connection details in the project.

Configure the required API key before running the application.

> Do not upload API keys or database passwords to GitHub.

## ▶️ Run the Application

Run the Streamlit application using:

streamlit run chatbot.py

The chatbot interface will open in your browser.

Enter a question related to the connected database.

Example:

Show all customers from Chennai

The AI generates the required SQL query and retrieves the corresponding data from the database.

## 💡 Example Questions

* Show all customers
* Find the total number of customers
* Show customers from a specific city
* Display the highest sales records
* Find the average sales amount
* Show the top-performing products

The supported questions depend on the structure and data available in the connected database.

## 🔐 Security Note

AI-generated SQL queries should be validated before execution.

For production environments, database access should be restricted and only safe read-only queries should be permitted.

## 📈 Current Status

The current version supports natural language input, AI-based SQL query generation, MySQL database connectivity, and query result display.

## 🔮 Future Improvements

* SQL query validation
* Read-only query restrictions
* Support for multiple databases
* Improved error handling
* Query history
* Data visualization of query results
* Database schema understanding
* Improved chatbot user interface

## 👨‍💻 Author

**Anand M**

B.Tech Artificial Intelligence & Data Science Student

Interested in Artificial Intelligence, Machine Learning, Deep Learning, and Data Science.

# Airlines-Manager-LLM-with-SQL
# ✈️ AM4 Analyst – LLM-Powered Airline Simulation Data Agent

This is a LangChain + Gradio-based AI system built for interactive analysis of an **Airline Management Simulation Game** dataset. It uses OpenAI's GPT model to generate and run SQL queries on an SQLite database (`am4.db`), providing intelligent, context-aware answers based entirely on the in-game data.

---

## 🚀 Features

- 🔍 **Natural language querying** of SQLite game data  
- 🧠 Uses GPT-4o-mini (or GPT-3.5-turbo) via LangChain
- 🗂️ Context-aware memory via `ConversationBufferMemory`
- 📊 Smart SQL query generation with enforced rules
- 🖥️ Simple and clean Gradio web interface

---

## 🧱 Dataset Tables

- **Airplanes Table**: Includes aircraft specs like Range, Speed, Fuel cost, Capacity, Net Profit, Return/$ etc.
- **Airports Demand Table**: Contains route demand info by distance and passenger class (Economy, Business, First).

---

## 📦 Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
## 📦 Environment Setup
Create a .env file in the root directory:

env
Copy
Edit
OPENAI_API_KEY=your-openai-key
Make sure your SQLite DB is named am4.db and placed in the same directory.

## ▶️ Run the App
```
python main.py
```
This will launch a local Gradio interface in your browser where you can ask questions like:

"List all aircrafts with range over 7000km and high passenger capacity"

"Show me all routes longer than 14000km"

"What are the most profitable aircrafts under $100 million?"



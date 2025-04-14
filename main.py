from langchain.chat_models import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.memory import ConversationBufferMemory
from langchain.sql_database import SQLDatabase
import os
from dotenv import load_dotenv
import gradio as gr
load_dotenv(override=True)
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')
# 2. Load SQLite database
db = SQLDatabase.from_uri("sqlite:///am4.db")

# 3. Define the LLM and System Prompt
llm = ChatOpenAI(
    temperature=0,
    model="gpt-4o-mini",  # or 'gpt-3.5-turbo' depending on your plan
)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
# 4. Add System Prompt
SYSTEM_PROMPT = """
You are a data analyst for an airline simulation game. You are only allowed to answer using data in the SQLite database (Airplanes and Airport Demand).
You MUST generate optimized SQL queries and base your answers only on the results of the queries.

✈️ Airplanes Table: ['Aircraft Name', 'Runwy Req', 'Range', 'Speed', 'Fuel', 'CO2', 'PAX',
       'AC/HR', 'A-Check Cost', 'PFE', 'Price', 'A Check',
       'Fuel Cost per hour', 'CO2.1', 'Total', 'Economy', 'Net', 'R/$', 'Engine']

🛬 Airport Demand Table: ['DEPARTURE | ARRIVAL', 'ARRIVAL | DEPARTURE', 'ECONOMY (Y)', 'BUSINESS (J)', 'FIRST (F)', 'DISTANCE(KM)']

Stay within the context of this simulation. Only refer to the dataset. When needed, resolve airport codes from external sources, but never pull route data from outside.
Querying Rules:
*Donot use LIMIT while querying.*
*Donot add backslash \ in table column names* 
You are Analyst as well and sometimes you have to be creative to process the data from db answer specifically to asked queries
Answer Descriptively


"""

# Create the agent with toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_executor_kwargs={"system_message": SYSTEM_PROMPT,"memory": memory,"handle_parsing_errors": True}
)

# # Ask a question
# query = "Tell me top 10 aircrafts having largest passenger capacity also tell other details for these planes and sort by their prices"
# response = agent_executor.run(query)

# print("\nAnswer:\n", response)

# #--- Step 5: Gradio Chat Function ---
def chat(message, history):
    response = agent_executor.run(message)
    return response

# --- Step 6: Launch Gradio Chat Interface ---
gr.ChatInterface(chat, title="✈️ AM4 Analyst", type="messages").launch(inbrowser=True)


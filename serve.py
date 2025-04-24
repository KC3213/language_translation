import os
import threading
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pyngrok import ngrok
import uvicorn

# Load .env for GROQ_API_KEY
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq model
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Define prompt and parser
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])
parser = StrOutputParser()

# Define full chain
chain = prompt_template | model | parser

# Define FastAPI app
app = FastAPI(title="LangChain Server", description="Groq + LangChain API", version="1.0")

# Pydantic model for request body
class InputData(BaseModel):
    language: str
    text: str

@app.post("/chain/invoke")
async def invoke_chain(input: InputData):
    result = chain.invoke({"language": input.language, "text": input.text})
    return {"result": result}

# Start FastAPI in a thread
def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Give server time to start
import time
time.sleep(2)

# Start ngrok tunnel
public_url = ngrok.connect(8000)
print(f"🚀 Server live at: {public_url}/docs")

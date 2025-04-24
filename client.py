import requests
import streamlit as st

def get_groq_response(input_text):
    # Send the correct JSON structure expected by FastAPI
    json_body = {
        "language": "French",
        "text": input_text
    }
    try:
        response = requests.post("http://localhost:8000/chain/invoke", json=json_body)
        if response.status_code == 200:
            return response.json().get("result", "No output available")
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Request failed: {e}"

# Streamlit UI
st.title("LLM App using LangChain + Groq")
input_text = st.text_input("Enter English text to convert to French")

if input_text:
    output = get_groq_response(input_text)
    st.success(output)

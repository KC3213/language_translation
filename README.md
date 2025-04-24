# language_translation
# 🌍 Language Translation App

This project is a **language translation app** that allows users to input text and choose a target language to translate into. The app is built using **Streamlit** for the frontend, with backend logic powered by a custom `serve.py` module and translation handled using a **Groq API key** as the LLM model.

---

## 🚀 Features

- Translate text into any language specified by the user
- Clean and interactive frontend using **Streamlit**
- Backend logic structured for clear input-output handling
- Integration with **Groq LLM API** for language processing
- Requirements managed through `requirements.txt`

---

## 🧠 Project Motivation

I created this project to **deepen my understanding of how LLM-based pipelines work**, especially using tools like **Langchain**. Working on this helped me understand core Langchain components like:

- 🔗 **Chains**: To structure the flow of translation logic
- 🔄 **Invoke**: To interact with the model in a controlled and modular way

It also gave me hands-on experience in tying frontend UI with backend language logic seamlessly using Streamlit.

---

## 🧱 Project Structure
- `client.py` is what the user interacts with directly via the browser.
- `serve.py` acts like a controller that manages all the backend operations, including the language model logic.
- `main_notebook.ipynb` is your working sandbox for logic experiments and additional LLM workflows. This notebook was primarily run and tested in **Google Colab**, allowing for easy integration with cloud resources.
- `requirements.txt` ensures environment reproducibility.

---

## 📦 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/KC3213/language_translation.git
   cd language_translation
2. install the dependencies
   ```bash
   pip install -r requirements.txt
3 run the cells in the notebook and finally run the cell !streamlit run client.py

## note the commands are written with respect to google colab


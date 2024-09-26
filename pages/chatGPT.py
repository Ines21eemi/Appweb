import streamlit as st
st.title("ChatGPT - Rédacteur Web")
user_input = st.text_input("Choisissez une thématique")
openai_key = st.sidebar.text_input("Tapez une clé OpenAI")

import os
from openai import OpenAI

client = OpenAI(api_key=openai_key)

prompt = input('Tapez votre text : ')


chat_completion = client.chat.completions.create(
    messages=[
         {
          "role": "system",
         "content": f"Tu es un rédacteur web."
         },
         ],
    model="gpt-3.5-turbo",
    temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


# Réponse de ChapGPT
chat_completion.choices[0].message.content

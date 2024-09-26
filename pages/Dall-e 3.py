import streamlit as st
#titre
st.title ("Dall-e 3")

#champ de saisi
user_input = st.text_input ("Open IA")
st.write(user_input)

recherche_input = st.sidebar.text_input("Clé")
st.write(recherche_input)

#sidebar
st.sidebar 

#clé
from openai import OpenAI
st.sidebar
client = OpenAI(api_key=OpenAIKEY)
prompt = "A cute baby sea otter"
image = client.images.generate(
    model="dall-e-2",
    prompt=user_input,
    size="512x512",
    quality="standard",
    n=1,
)
image_url = image.data[0].url
print(image_url)

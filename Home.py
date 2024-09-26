import streamlit as st
#Titre
st.title("Mon formulaire")
#Texte
st.write("Ceci est un formulaire de contact")
#Champ de saisi
user_input = st.text_input("Tapez votre texte : ")
st.write(user_input)
#Image
st.image("https://www.mercedes-benz-mag.fr/wp-content/uploads/2021/09/HP-img-1680x842-22_Hamilton-1600x630.png")
#Sidbar
st.sidebar.title ("Ines Romain")
#Video dans la sidebar
st.sidebar.video("https://www.youtube.com/watch?v=lofb298wDFc")

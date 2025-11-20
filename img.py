import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Exibir Imagem", layout="centered")

# menu lateral 
menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Carregar Imagem"]
)

# --- TELA HOME ---
if menu == "Home":
    st.title("Bem-vindo!")
    st.write("Escolha *Carregar Imagem* no menu à esquerda.")

# --- TELA CARREGAR IMAGEM ---
elif menu == "Carregar Imagem":
    st.title("Carregar e Exibir Imagem")

    opcao = st.radio(
        "Escolha o método:",
        ["Selecionar arquivo", "Digitar caminho do arquivo"]
    )

    image = None

    # UPLOAD
    if opcao == "Selecionar arquivo":
        file = st.file_uploader("Envie uma imagem", type=["png", "jpg", "jpeg"])
        if file:
            image = Image.open(file)

    # CAMINHO LOCAL
    else:
        caminho = st.text_input("Digite o caminho completo da imagem:", "")
        if caminho and os.path.exists(caminho):
            image = Image.open(caminho)
        elif caminho:
            st.error("Caminho inválido!")

    # MOSTRAR A IMAGEM
    if image:
        st.image(image, caption="Imagem carregada", use_column_width=True)

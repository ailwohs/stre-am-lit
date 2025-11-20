import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Menu Central", layout="centered")

st.title("🖼️ Exibir Imagem")
st.write("Escolha uma opção abaixo:")

# --- MENU CENTRAL ---
opcao_menu = st.selectbox(
    "Menu",
    ["Selecione...", "Carregar Imagem"],
    index=0
)

# --- SE O USUÁRIO ESCOLHER CARREGAR IMAGEM ---
if opcao_menu == "Carregar Imagem":
    st.subheader("Escolha como carregar a imagem:")

    opcao = st.radio(
        "Método:",
        ["Selecionar arquivo", "Digitar caminho"]
    )

    image = None

    # Upload tradicional
    if opcao == "Selecionar arquivo":
        file = st.file_uploader("Envie uma imagem", type=["png", "jpg", "jpeg"])
        if file:
            image = Image.open(file)

    # Caminho local
    else:
        caminho = st.text_input("Digite o caminho completo da imagem:")
        if caminho:
            if os.path.exists(caminho):
                image = Image.open(caminho)
            else:
                st.error("Caminho inválido!")

    # Mostrar imagem se existir
    if image:
        st.image(image, caption="Imagem carregada", use_column_width=True)

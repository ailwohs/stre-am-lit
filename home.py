import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Exibir Imagem", layout="centered")

st.sidebar.title("Menu")

# menu lateral COM ABA 
menu = st.sidebar.selectbox(
    "ABAS- Menu box", 
    ["Home", "Carregar Imagem", "Informações"]
)


#MENU DE BUTTOM

if st.sidebar.button("Home"):
    st.session_state["page"] = "home"

if st.sidebar.button("Relatórios"):
    st.session_state["page"] = "relatorios"

if st.sidebar.button("Configurações"):
    st.session_state["page"] = "config"

page = st.session_state.get("page", "home")

if page == "home":
    st.title("Home")
    st.write("Bem-vindo!")
elif page == "relatorios":
    st.title("Relatórios")
    st.write("Aqui ficam os relatórios...")
elif page == "config":
    st.title("Configurações")
    st.write("Ajustes e preferências...")


# -tela inicial de bem vindo
if menu == "Home":
    st.title("Bem-vindo!")
    st.write("Escolha *Carregar Imagem* no menu à esquerda.")

# --tela pra carregar a imagem
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

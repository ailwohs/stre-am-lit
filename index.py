import streamlit as st

# ⚙️ Configuração da página — deve vir antes de qualquer outro comando Streamlit
st.set_page_config(
    page_title="Unos Loucos 🚗",
    page_icon="🚛",  # você pode trocar o emoji aqui!
    layout="centered"
)

# 🩷 Título e cabeçalho
st.title("Rogério Sena GaydoUno")
st.header("Vamos aprender sobre como deixar o Unofeio")

# 🧮 Entradas numéricas
num1 = st.number_input("Digite o valor do PCX ou Uno:", value=5)
num2 = st.number_input("Digite o valor do PCXBlack ou Uno:", value=5)
num3 = st.number_input("Digite o valor do PCXCinza ou Uno:", value=5)

# 💡 Cálculo e exibição
soma = num1 + num2 + num3
st.write(f"A soma dos valores é: **{soma}**")
























































































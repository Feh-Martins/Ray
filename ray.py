import streamlit as st
from datetime import datetime
import time
import base64
from pytz import timezone

# Função para converter imagem em base64
def imagem_base64(caminho):
    with open(caminho, "rb") as imagem:
        dados = imagem.read()
    return base64.b64encode(dados).decode()

# Converta a imagem para base64
imagem_fundo = imagem_base64("fundo.jpeg")

# Estilo CSS ajustado para imagem de fundo mais suave e discreta
st.markdown(
    f"""
    <style>
    .stApp {{
    background: url("data:image/jpeg;base64,{imagem_fundo}");
    background-size: 100%;
    background-repeat: no-repeat;
    background-position: center;
    }}

    h1, h2, h3, h4, h5, h6, p {{
        color: whith !important;
    }}
    
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🎉Viva a Rayane")
st.write("Contagem Regressiva para o maior evento astronomico do planeta")

# Data alvo: 21 de julho de 2025
data_aniversario = datetime(2025, 7, 21, 0, 0, 0)
fuso_brasil = timezone("America/Sao_Paulo")
agora = datetime.now(fuso_brasil)

# Placeholder da contagem
contador = st.empty()

# Loop da contagem com tempo real
while True:
    agora = datetime.now()
    restante = data_aniversario - agora

    if restante.total_seconds() <= 0:
        contador.markdown("## 🎂 Feliz aniversário minha querida! Parabéns!")
        break

    dias = restante.days
    horas, resto = divmod(restante.seconds, 3600)
    minutos, segundos = divmod(resto, 60)

    contador.markdown(f"""
    ### ⏳ Tempo restante:
    - **{dias}** dias  
    - **{horas:02d}:{minutos:02d}:{segundos:02d}** (horas:minutos:segundos)
    """)

    time.sleep(1)

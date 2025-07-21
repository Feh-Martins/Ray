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

# Estilo CSS com imagem de fundo e texto branco
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("data:image/jpeg;base64,{imagem_fundo}");
        background-size: 120%;
        background-repeat: no-repeat;
        background-position: center;
    }}

    h1, h2, h3, h4, h5, h6, p {{
        color: white !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Título e subtítulo
st.title("🎉 Viva a Rayane 🎉")
st.write("Contagem Regressiva para o maior evento astronômico do planeta")
st.write("Não é sempre que se faz 20 aninhos")

# Fuso horário do Brasil
fuso_brasil = timezone("America/Sao_Paulo")

# Data e hora do evento (ajuste aqui se quiser outro horário!)
data_aniversario = fuso_brasil.localize(datetime(2025, 7, 21, 0, 0, 0))

# Placeholder para a contagem
contador = st.empty()

# Loop da contagem regressiva
while True:
    agora = datetime.now(fuso_brasil)
    restante = data_aniversario - agora

    if restante.total_seconds() <= 0:
        contador.markdown("## 🎂 Parabéns querida Rayane, que seu dia seja tão especial quanto você🎉! ")
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

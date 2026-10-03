import streamlit as st

st.set_page_config(page_title="Portal de Jogos ENEM", page_icon="🎓", layout="wide")

# Menu Principal de Matérias
st.sidebar.title("🎓 Portal ENEM")
materia = st.sidebar.selectbox(
    "Escolha a Matéria:",
    ["⚡ Física", "🧪 Química", "📐 Matemática", "🧬 Biologia"]
)

# Direcionamento do código por matéria
if materia == "⚡ Física":
    import app_física
elif materia == "🧪 Química":
    import app_quimica
elif materia == "📐 Matemática":
    import app_matematica
elif materia == "🧬 Biologia":
    import app_biologia
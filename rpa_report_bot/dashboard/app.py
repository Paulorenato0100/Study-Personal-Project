import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="RPA Dashboard", layout="wide")

st.title("📊 Dashboard Automatizado - RPA")

# caminho da pasta output
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join(base_dir, "output")

# 🔥 FILTRO CORRETO (resolve seu erro)
files = [
    f for f in os.listdir(output_path)
    if f.endswith(".xlsx") and not f.startswith("~$")
]

# ordena do mais recente
files.sort(reverse=True)

if files:
    file_path = os.path.join(output_path, files[0])

    try:
        df = pd.read_excel(file_path)

        st.success("Dados carregados com sucesso!")
        st.dataframe(df)

        st.subheader("📈 Métricas")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total de Registros", len(df))

        with col2:
            st.metric("Média de Palavras", int(df["Qtd_Palavras"].mean()))

        st.subheader("📊 Frases por Autor")
        st.bar_chart(df["Autor"].value_counts())

    except Exception:
        st.error("⚠️ Feche o Excel antes de rodar o dashboard.")

else:
    st.warning("Nenhum arquivo válido encontrado.")
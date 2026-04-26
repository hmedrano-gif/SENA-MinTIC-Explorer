import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="MinTIC Data Explorer Pro", layout="wide", page_icon="SEARCH")
APP_TOKEN = "e0umakk5lo0xz8m7cfh7lccic"

st.markdown("""
<style>
.stApp { background-color: #f8f9fa; }
.main-title { color: #00324d; font-size: 32px; font-weight: bold; text-align: center; }
.ai-box { background-color: #e3f2fd; padding: 15px; border-radius: 10px; border-left: 5px solid #1976d2; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>SEARCH MinTIC Data Discovery & AI Mentor</div>", unsafe_allow_html=True)

st.subheader("1. FIND Buscar un Tema (Dataset)")
query = st.text_input("Que tema quieren investigar? (Ej: Salud, Empleo, Agro)", placeholder="Escribe aqui...")

def suggest_ai(columns):
      cols = [str(c).upper() for c in columns]
      ideas = []
      if any(x in " ".join(cols) for x in ["VALOR", "PRECIO", "MONTO"]):
                ideas.append("**IA Predictiva:** Estimar costos futuros o detectar sobrecostos.")
            if any(x in " ".join(cols) for x in ["OBJETO", "DESCRIPCION", "NOMBRE"]):
                      ideas.append("**IA de Clasificacion:** Categorizar automaticamente los registros.")
                  return ideas

if query:
      url = f"https://www.datos.gov.co/resource/{APP_TOKEN}.json?$q={query}"
    resp = requests.get(url)
    if resp.status_code == 200:
              data = resp.json()
              if data:
            df = pd.DataFrame(data)
            st.success(f"Se encontraron {len(df)} registros!")
            st.dataframe(df)

            st.markdown("<div class='ai-box'>", unsafe_allow_html=True)
            st.write("### AI Mentor Sugiere:")
            suggestions = suggest_ai(df.columns)
            for s in suggestions:
                              st.write(f"- {s}")
                          st.markdown("</div>", unsafe_allow_html=True)
else:
            st.warning("No se encontraron resultados para esa busqueda.")
else:
        st.error("Error al conectar con la API de Datos Abiertos.")
  

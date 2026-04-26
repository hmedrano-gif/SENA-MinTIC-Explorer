import streamlit as st
import pandas as pd
import requests

# Configuración de la App
st.set_page_config(page_title="MinTIC Data Explorer Pro", layout="wide", page_icon="🔎")
APP_TOKEN = "e0umakk5lo0xz8m7cfh7lccic"

# Estilos SENA/MinTIC
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .main-title { color: #00324d; font-size: 32px; font-weight: bold; text-align: center; }
    .ai-box { background-color: #e3f2fd; padding: 15px; border-radius: 10px; border-left: 5px solid #1976d2; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🔎 MinTIC Data Discovery & AI Mentor</div>", unsafe_allow_html=True)

# --- PASO 1: BÚSQUEDA ---
st.subheader("1. 🔍 Buscar un Tema (Dataset)")
query = st.text_input("¿Qué tema quieren investigar? (Ej: Salud, Empleo, Agro)", placeholder="Escribe aquí...")

def suggest_ai(columns):
    cols = [str(c).upper() for c in columns]
    ideas = []
    if any(x in " ".join(cols) for x in ["VALOR", "PRECIO", "MONTO"]):
        ideas.append("📈 **IA Predictiva:** Estimar costos futuros o detectar sobrecostos.")
    if any(x in " ".join(cols) for x in ["OBJETO", "DESCRIPCION", "NOMBRE"]):
        ideas.append("📝 **IA NLP:** Clasificar categorías de texto o detectar anomalías en descripciones.")
    if any(x in " ".join(cols) for x in ["DEPARTAMENTO", "MUNICIPIO", "CIUDAD"]):
        ideas.append("🗺️ **IA Espacial:** Agrupar regiones por niveles de riesgo o inversión.")
    return ideas if ideas else ["🧠 **IA General:** Encontrar patrones y correlaciones entre las variables."]

if query:
    with st.spinner("Buscando en el catálogo nacional..."):
        try:
            res = requests.get("https://www.datos.gov.co/api/views/metadata/v1.json", params={"query": query})
            datasets = res.json()
        except Exception as e:
            st.error(f"Error de conexión: {e}")
            datasets = []
    
    if datasets:
        dataset_options = {d['name']: d['id'] for d in datasets}
        selected_name = st.selectbox("🎯 Elige un dataset para trabajar:", list(dataset_options.keys()))
        selected_id = dataset_options[selected_name]

        # --- PASO 2: ANÁLISIS IA MENTOR ---
        st.markdown("---")
        try:
            meta_res = requests.get(f"https://www.datos.gov.co/api/views/{selected_id}.json").json()
            cols_names = [c.get('name') for c in meta_res.get('columns', [])]
            
            st.subheader("💡 Sugerencias del Mentor IA")
            st.markdown("<div class='ai-box'>", unsafe_allow_html=True)
            for idea in suggest_ai(cols_names):
                st.write(idea)
            st.markdown("</div>", unsafe_allow_html=True)

            # --- PASO 3: EXPLORACIÓN LOCAL ---
            st.markdown("---")
            st.subheader("3. 🎯 Explorador y Buscador Local")
            
            limit = st.slider("Registros a cargar localmente:", 100, 10000, 1000)
            data_url = f"https://www.datos.gov.co/resource/{selected_id}.json?$limit={limit}"
            
            with st.spinner("Cargando datos a memoria local..."):
                resp = requests.get(data_url, headers={"X-App-Token": APP_TOKEN})
                df = pd.DataFrame(resp.json())
                
                # Buscador por Campo
                if not df.empty:
                    col_sel, val_sel = st.columns([1, 2])
                    with col_sel:
                        campo = st.selectbox("Buscar en el campo:", df.columns.tolist())
                    with val_sel:
                        valor = st.text_input(f"Escribe lo que buscas en {campo}:")
                    
                    filtered_df = df[df[campo].astype(str).str.contains(valor, case=False, na=False)] if valor else df
                    
                    st.write(f"Mostrando {len(filtered_df)} resultados:")
                    st.dataframe(filtered_df, use_container_width=True)

                    # --- PASO 4: CONEXIÓN FINAL ---
                    st.markdown("---")
                    st.subheader("🔗 URL para su Proyecto (Power BI / Python)")
                    st.code(f"https://www.datos.gov.co/resource/{selected_id}.json")
                    st.success("¡Copia esta URL y llévala a Power BI!")
                else:
                    st.warning("El dataset seleccionado no devolvió datos.")
        except Exception as e:
            st.error(f"Error al procesar el dataset: {e}")

st.markdown("---")
st.caption("Aislamiento de Datos Garantizado | Mentoría SENA 2026")

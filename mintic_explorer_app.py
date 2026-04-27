import streamlit as st
import pandas as pd
import requests
import json
import re
import os
import google.generativeai as genai

st.set_page_config(page_title="Mentor MinTIC 2026: Elite Edition", layout="wide", page_icon="medal")

GEMINI_KEY = "AIzaSyA-Aybc_CO_UxqM7f0nd0r2JJjeqJ3YfEU"
genai.configure(api_key=GEMINI_KEY, transport='rest')

WORKSPACE_PATH = os.getcwd()

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
            html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
                .stApp { background-color: #0f172a; color: #f8fafc; }
                    .header-container {
                            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
                                    padding: 50px; border-radius: 0 0 50px 50px; text-align: center;
                                            margin-bottom: 40px; border-bottom: 2px solid #38bdf8;
                                                }
                                                    .pillar-box { 
                                                            background: #1e293b; padding: 25px; border-radius: 15px; 
                                                                    border-left: 6px solid #38bdf8; margin-bottom: 20px;
                                                                            box-shadow: 0 10px 20px rgba(0,0,0,0.2); line-height: 1.7;
                                                                                }
                                                                                    .coach-msg { background: #0ea5e9; color: white; padding: 15px; border-radius: 12px; font-weight: 600; margin-bottom: 20px; border-left: 10px solid #0369a1; }
                                                                                        .big-data-badge { background: #38bdf8; color: #0f172a; padding: 8px 18px; border-radius: 40px; font-size: 14px; font-weight: 800; }
                                                                                            .stButton>button { border-radius: 12px; font-weight: 700; transition: all 0.3s; }
                                                                                                .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(56,189,248,0.4); }
                                                                                                    </style>
                                                                                                        """, unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
            <div style="color:#38bdf8; font-weight:800; letter-spacing:4px; margin-bottom:10px;">ESTRATEGIA | RIGOR | IMPACTO</div>
                    <div class="main-title" style="font-size:42px; font-weight:800; text-transform:uppercase;">[Elite] MENTOR MINTIC 2026: ELITE v13.0</div>
                            <div style="opacity:0.8; font-size:18px;">Transformando Datos en Liderazgo Sistemico</div>
                                </div>
                                    """, unsafe_allow_html=True)

class EliteMentor:
      def __init__(self):
                self.model_name = 'gemini-1.5-flash'

      def analyze_deep(self, idea, ds_name, rows, columns):
                model = genai.GenerativeModel(self.model_name)
                prompt = f"Actua como un Mentor de Datos Senior. Analiza '{idea}' with '{ds_name}'. Variables: {columns}. Registros: {rows}. JSON: problema, reto, solucion, impacto_social."
                try:
                              res = model.generate_content(prompt)
                              match = re.search(r'\{.*\}', res.text, re.DOTALL)
                              return json.loads(match.group(0)) if match else self._coach_fallback(ds_name)
                          except:
            return self._coach_fallback(ds_name)

      def _coach_fallback(self, name):
                return {
                              "problema": f"Fragmentacion de informacion en '{name}'.",
                              "reto": "Automatizar identificacion de riesgos sistemicos.",
                              "solucion": "Modelos de analitica avanzada and deteccion de anomalias.",
                              "impacto_social": "Transparencia institucional en beneficio ciudadano."
                }

  mentor = EliteMentor()

if "step" not in st.session_state: st.session_state.step = 1

with st.sidebar:
      st.markdown("### (Mentor) MENTOR ESTRATEGICO")
      if st.button("REINICIAR CONSULTORIA"):
                for k in list(st.session_state.keys()): del st.session_state[k]
                          st.rerun()

  if st.session_state.step == 1:
        st.markdown('<div class="coach-msg">Bienvenido! Buscamos soluciones estructurales para el pais.</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns([2, 1, 1])
        q = c1.text_input("Ingresa tu Reto Estrategico:")
        depto = c2.selectbox("Dpto:", ["NACIONAL", "BOGOTA", "ANTIOQUIA", "VALLE"])
        ciudad = c3.text_input("Ciudad:")

    if st.button("INICIAR DESCUBRIMIENTO", use_container_width=True):
              if q:
                            with st.status("Auditando Datos...") as status:
                                              query = f"{q} {depto if depto != 'NACIONAL' else ''} {ciudad}"
                                              res = requests.get(f"https://www.datos.gov.co/api/catalog/v1?q={query}&limit=5").json()
                                              results = []
                                              for item in res.get('results', []):
                                                                    r = item.get('resource', {})
                                                                    ds_id = r.get('id')
                                                                    try:
                                                                                              cat = requests.get(f"https://api.us.socrata.com/api/catalog/v1?ids={ds_id}", timeout=3).json()
                                                                                              rows = cat['results'][0]['resource']['row_count']
                                                                                              v_res = requests.get(f"https://www.datos.gov.co/api/views/{ds_id}.json").json()
                                                                                              cols = [c['name'] for c in v_res.get('columns', [])]
                                                                                          except: rows = 0; cols = []
                                                                    analysis = mentor.analyze_deep(q, r.get('name'), rows, cols)
                                                                    results.append({"id": ds_id, "name": r.get('name'), "rows": rows, "entidad": r.get('attribution'), **analysis})
                                                                st.session_state.results = results
                                              status.update(label="Vision Generada!", state="complete")

                    if "results" in st.session_state:
                              for d in st.session_state.results:
                                            with st.container():
                                                              st.markdown(f"### {d['name']}")
                                                              cl, cr = st.columns(2)
                                                              cl.markdown(f"<div class='pillar-box'>PROBLEMA:<br>{d['problema']}</div>", unsafe_allow_html=True)
                                                              cr.markdown(f"<div class='pillar-box'>SOLUCION:<br>{d['solucion']}</div>", unsafe_allow_html=True)
                                                              if st.button(f"DESARROLLAR: {d['id']}", key=f"btn_{d['id']}"):
                                                                                    st.session_state.selected = d; st.session_state.step = 2; st.
                                                                                    st.session_state.selected = d; st.session_state.step = 2; st.rerun()

                    elif st.session_state.step == 2:
    ds = st.session_state.selected
    st.markdown(f"## Proyecto: {ds['name']}")
    if st.button("VOLVER"): st.session_state.step = 1; st.rerun()
          st.write(ds)

st.markdown("---")
st.caption("v13.0 | Elite Edition | MinTIC 2026")

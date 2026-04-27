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

class EliteMentor:
        def __init__(self):
                    self.model_name = 'gemini-1.5-flash'
                def analyze_deep(self, idea, ds_name, rows, columns):
                            model = genai.GenerativeModel(self.model_name)
                            prompt = f"Analiza {idea} con {ds_name}. JSON: problema, reto, solucion, impacto_social."
                            try:
                                            res = model.generate_content(prompt)
                                            m = re.search(r'\{.*\}', res.text, re.DOTALL)
                                            return json.loads(m.group(0)) if m else self._cf(ds_name)
                                        except: return self._cf(ds_name)
                                                def _cf(self, name):
                                                            return {"problema": f"Datos en {name}", "reto": "Analisis", "solucion": "IA", "impacto_social": "Mejora"}

mentor = EliteMentor()

if "step" not in st.session_state: st.session_state.step = 1

with st.sidebar:
        st.markdown("### MENTOR ESTRATEGICO")
    if st.button("REINICIAR"):
                for k in list(st.session_state.keys()): del st.session_state[k]
                            st.rerun()

if st.session_state.step == 1:
        st.title("MENTOR MINTIC 2026: ELITE")
    q = st.text_input("Reto Estrategico:")
    if st.button("INICIAR") and q:
                with st.status("Buscando...") as status:
                                res = requests.get(f"https://www.datos.gov.co/api/catalog/v1?q={q}&limit=3").json()
                                results = []
                                for item in res.get('results', []):
                                                    r = item.get('resource', {})
                                                    ds_id = r.get('id')
                                                    analysis = mentor.analyze_deep(q, r.get('name'), 0, [])
                                                    results.append({"id": ds_id, "name": r.get('name'), **analysis})
                                                st.session_state.results = results
            status.update(label="Listo!", state="complete")
    if "results" in st.session_state:
                for d in st.session_state.results:
                                st.subheader(d['name'])
            st.write(f"**SOLUCION:** {d['solucion']}")
            if st.button(f"VER {d['id']}", key=d['id']):
                                st.session_state.selected = d; st.session_state.step = 2; st.rerun()
elif st.session_state.step == 2:
    st.write(st.session_state.selected)
    if st.button("VOLVER"): st.session_state.step = 1; st.rerun()
        

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
            <div style="color:#38bdf8; font-weight:800; letter-spacing:4px; margin-bottom:10px;">ESTRATEGIA - RIGOR - IMPACTO</div>
                    <div class="main-title" style="font-size:42px; font-weight:800; text-transform:uppercase;">MENTOR MINTIC 2026: ELITE v13.0</div>
                            <div style="opacity:0.8; font-size:18px;">Transformando Datos en Liderazgo Sistemico</div>
                                </div>
                                    """, unsafe_allow_html=True)

class EliteMentor:
        def __init__(self):
                    self.model_name = 'gemini-1.5-flash'

        def analyze_deep(self, idea, ds_name, rows, columns):
                    model = genai.GenerativeModel(self.model_name)
                    prompt = f"Actua como un Mentor de Datos Senior. Analiza '{idea}' con '{ds_name}'. Vars: {columns}. Registros: {rows}. JSON: problema, reto, solucion, impacto_social."
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
                                    "solucion": "Modelos de Isolation Forest y analitica avanzada.",
                                    "impacto_social": "Transparencia institucional y beneficio ciudadano."
                    }

        def get_notebook(self, ds_id, ds_name, strategy, columns):
                    model = genai.GenerativeModel(self.model_name)
                    prompt = f"Genera JSON de un NOTEBOOK (.ipynb) para {ds_id}. Solo JSON."
                    try:
                                    res = model.generate_content(prompt)
                                    match = re.search(r'\{.*\}', res.text, re.DOT

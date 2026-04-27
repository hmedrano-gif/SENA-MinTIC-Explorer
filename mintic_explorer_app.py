import streamlit as st
import requests
import json
import re
import google.generativeai as genai

st.set_page_config(page_title="Mentor MinTIC", layout="wide")
GEMINI_KEY = "AIzaSyA-Aybc_CO_UxqM7f0nd0r2JJjeqJ3YfEU"
genai.configure(api_key=GEMINI_KEY, transport='rest')

def analyze(idea, name):
                model = genai.GenerativeModel('gemini-1.5-flash')
                try:
                                    res = model.generate_content(f"Analiza {idea} con {name}. JSON: problema, solucion.")
                                    m = re.search(r'\{.*\}', res.text, re.DOTALL)
                                    return json.loads(m.group(0)) if m else {"problema": "Error", "solucion": "Error"}
                                except:
        return {"problema": "Error", "solucion": "Error"}

st.title("MENTOR MINTIC 2026")
q = st.text_input("Reto:")
if st.button("BUSCAR") and q:
                res = requests.get(f"https://www.datos.gov.co/api/catalog/v1?q={q}&limit=3").json()
                for item in res.get('results', []):
                                    r = item.get('resource', {})
                                    st.subheader(r.get('name'))
                                    ans = analyze(q, r.get('name'))
                                    st.write(ans)
                            

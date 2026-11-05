# Mentor MinTIC 2026 · Explorador de datos abiertos con IA

Aplicación en Streamlit que ayuda a los equipos del concurso **Datos al Ecosistema 2026 (MinTIC)** a pasar de una idea a un proyecto con datos. Busca conjuntos de datos en **datos.gov.co** y, para cada uno, propone con IA el problema, el reto, la solución y el impacto social.

> Autor: **Heyder Medrano Olier** · Mentoría de IA y datos (SENA, 2026) · Estado: prototipo de apoyo a la mentoría.

## Cómo funciona

1. El equipo escribe su reto y, si quiere, el departamento y la ciudad.
2. La aplicación consulta el catálogo de datos.gov.co (API Socrata) y trae los 5 conjuntos más relevantes, con su número de registros y sus columnas.
3. Para cada conjunto, Gemini propone el **problema**, el **reto**, la **solución** y el **impacto social**. Si no hay clave configurada, la aplicación muestra respuestas de referencia y sigue funcionando.
4. El equipo elige un conjunto para desarrollarlo.

La guía para los equipos está en [GUIA_GRUPOS.md](GUIA_GRUPOS.md): reglas, acceso a los datos, selección de variables y evaluación.

## Stack

Python · Streamlit · Requests · API de catálogo de Socrata (datos.gov.co) · Google Gemini (`google-generativeai`).

## Ejecutar

```bash
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml   # y escribe tus claves
streamlit run mintic_explorer_app.py
```

| Secreto | Para qué | Obligatorio |
|---|---|---|
| `GEMINI_API_KEY` | Análisis con IA | No: sin la clave se usan respuestas de referencia |
| `DATOS_GOV_APP_TOKEN` | Mayor cuota en la API de datos.gov.co | No |

También pueden darse como variables de entorno.

## Seguridad

Las claves **no van en el código**. Se leen de `.streamlit/secrets.toml`, que está en `.gitignore`, o de variables de entorno.

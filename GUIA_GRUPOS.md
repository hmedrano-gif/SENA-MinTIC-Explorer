# Guía de participación · Datos al Ecosistema 2026 (MinTIC)

Mentoría de IA y datos para los equipos SENA.

## 1. Reglas de oro
- **Equipo:** de 2 a 4 personas, con al menos una mujer por grupo.
- **Datos:** es obligatorio usar datos.gov.co.
- **IA:** el proyecto debe usar inteligencia artificial.
- **Metodología:** CRISP-ML(Q).

## 2. Acceso a los datos
- Cada equipo crea **su propio App Token** en datos.gov.co (perfil → *Developer settings* → *Create new app token*).
- El token va en la cabecera `X-App-Token`. **Nunca lo escriban en el código ni en un documento público:** guárdenlo en `.streamlit/secrets.toml` como `DATOS_GOV_APP_TOKEN`.

## 3. Selección de variables
- **Varianza:** eliminar las columnas constantes.
- **Correlación:** eliminar las variables redundantes.
- **IA:** usar Random Forest para medir la importancia de las variables.

## 4. Estructura de la evaluación
| Criterio | Peso |
|---|---|
| Innovación | 20 % |
| Uso de datos | 20 % |
| Rigor técnico | 20 % |
| Uso de IA | 20 % |

## 5. Ejecución
```bash
pip install -r requirements.txt
streamlit run mintic_explorer_app.py
```

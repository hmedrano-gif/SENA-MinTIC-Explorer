# [Insertar después de los filtros en el código anterior]

if filtered_datasets:
    # --- PANEL DE TEMAS DETECTADOS ---
    st.subheader("📊 Temas Detectados en tu Búsqueda")
    
    # Extraer categorías y tags de los datasets filtrados
    all_categories = [d.get('category', 'General') for d in filtered_datasets if d.get('category')]
    unique_cats = list(set(all_categories))
    
    cols_tags = st.columns(len(unique_cats[:5])) # Mostrar los primeros 5 temas
    for i, cat in enumerate(unique_cats[:5]):
        cols_tags[i].markdown(f"**🏷️ {cat}**")
    
    st.markdown("---")
    
    # Selección de Dataset
    dataset_options = {f"{d['name']} (ID: {d['id']})": d['id'] for d in filtered_datasets}
    selected_name = st.selectbox("🎯 Elige un dataset para analizar:", list(dataset_options.keys()))
    
    # [Continuar con el resto de la lógica de IA...]

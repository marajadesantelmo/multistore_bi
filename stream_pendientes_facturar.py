import streamlit as st
import pandas as pd
from datetime import datetime

def show_page_pendientes_facturar():
    df = pd.read_csv('data/pendientes_facturar.csv')
    df['Fecha'] = pd.to_datetime(df['Fecha'])

    st.image('logo.png')
    st.title("Items pendientes de Facturar")

    col1, col2, col3 = st.columns(3)
    with col1:
        fecha_inicio = st.date_input("Fecha inicio", value=df['Fecha'].min())
    with col2:
        fecha_fin = st.date_input("Fecha fin", value=df['Fecha'].max())
    with col3:
        clientes = ["Todos los clientes"] + sorted(df['Cliente'].unique())
        cliente = st.selectbox("Cliente", clientes)

    # Filtrado
    mask = (df['Fecha'] >= pd.to_datetime(fecha_inicio)) & (df['Fecha'] <= pd.to_datetime(fecha_fin))
    if cliente != "Todos los clientes":
        mask = mask & (df['Cliente'] == cliente)
    filtered = df[mask].copy()

    # Formatear fecha en formato español para mostrar
    filtered['Fecha'] = filtered['Fecha'].dt.strftime('%d/%m/%Y')

    # Métricas
    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("Cantidad de ítems", filtered.shape[0])
    with col5:
        st.metric("Total estimado ($)", f"{filtered['Importe'].sum():,.2f}")
    with col6:
        st.metric("Clientes únicos", filtered['Cliente'].nunique())

    st.dataframe(filtered, hide_index=True, use_container_width=True)

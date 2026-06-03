import pandas as pd
import streamlit as st

st.title("Datos Explorer")

df = pd.read_csv("datos.csv")

st.write('Primeras filas del DataFrame:', df.head())
st.write('Descripción estadística del DataFrame:', df.describe())

columna = st.selectbox ('elige una columna para mostrar su distribución', df.columns)

st.bar_chart(df[columna].value_counts())

"""
Mini Data Explorer
==================
App de Streamlit para explorar visualmente cualquier CSV.
"""

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title='Mini Data Explorer',
    page_icon='🔍',
    layout='wide',
)

st.title('🔍 Mini Data Explorer')
st.markdown(
    'Sube un CSV y explóralo de forma interactiva. '
    'Si no subes nada, se usa el dataset de ejemplo.'
)


# 2. CARGA DE DATOS
st.sidebar.header('⚙️ Configuración')

archivo_subido = st.sidebar.file_uploader(
    'dtos.csv',
    type=['csv'],
)

if archivo_subido is not None:
    df = pd.read_csv(archivo_subido)
    st.sidebar.success('✅ Archivo cargado')
else:
    df = pd.read_csv('datos.csv')
    st.sidebar.info('ℹ️ Usando dataset de ejemplo')


# 3. MÉTRICAS
col1, col2, col3 = st.columns(3)
col1.metric('📏 Filas', df.shape[0])
col2.metric('📐 Columnas', df.shape[1])
col3.metric('❓ Valores nulos', df.isnull().sum().sum())
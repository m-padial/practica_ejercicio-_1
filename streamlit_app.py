#  streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scraping import scrapeo_opciones_y_futuros
from volatilidad import calcular_volatilidad

# --- 1. Scrapeo y cálculo de volatilidad
@st.cache_data
def cargar_datos():
    df_opciones, df_futuros = scrapeo_opciones_y_futuros()
    df_vol = calcular_volatilidad(df_opciones, df_futuros)
    return df_vol

df_resultado = cargar_datos()

# --- 2. Sidebar de selección
st.sidebar.title("Selecciona parámetros")

vencimientos = sorted(df_resultado['FV'].dropna().unique())
vencimiento_seleccionado = st.sidebar.selectbox(
    "Selecciona vencimiento:",
    options=vencimientos
)

# --- 3. Gráfico principal
st.title("Skew de Volatilidad - MINI IBEX")

# Filtrar por vencimiento
df_vto = df_resultado[df_resultado['FV'] == vencimiento_seleccionado]
df_calls = df_vto[df_vto['put/call'] == 'Call'].dropna(subset=['σ'])
df_puts = df_vto[df_vto['put/call'] == 'Put'].dropna(subset=['σ'])

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))

if not df_calls.empty:
    ax.plot(df_calls['strike'], df_calls['σ'], label='Calls', marker='o')
if not df_puts.empty:
    ax.plot(df_puts['strike'], df_puts['σ'], label='Puts', marker='o')

ax.set_title(f"Skew de Volatilidad - Vencimiento {vencimiento_seleccionado}")
ax.set_xlabel('Strike')
ax.set_ylabel('Volatilidad Implícita (%)')
ax.grid(True)
ax.legend()

st.pyplot(fig)

# --- 4. Mostrar datos
with st.expander("Ver datos usados en el gráfico"):
    st.dataframe(df_vto[['strike', 'put/call', 'ant', 'σ']])

import os
import subprocess

def handler(event=None, context=None):
    """
    Handler para AWS Lambda. Lanza el servidor Streamlit.
    """
    port = int(os.environ.get("PORT", 8501))
    cmd = f"streamlit run src/streamlit_app.py --server.port {port} --server.headless true"
    subprocess.Popen(cmd, shell=True)

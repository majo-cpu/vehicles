import streamlit as st
import pandas as pd

df_vehicles = pd.read_csv(r'C:\Users\nicol\OneDrive\Escritorio\vehicles_env\vehicles_us.csv', sep=',')

st.header('Análisis de Vehículos en EE.UU.')

st.write(df_vehicles)
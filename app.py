import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Panel Sprint 7 — Vehículos")
df = pd.read_csv("vehicles_us.csv")

if st.button("Mostrar histograma de odómetro"):
    st.write("Distribución de kilometraje")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.button("Mostrar dispersión odómetro vs precio"):
    st.write("Relación odometer vs price")
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

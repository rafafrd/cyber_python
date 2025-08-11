import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

# Set page configuration
st.set_page_config(
    page_title="sistema de vizualização de dados",
    page_icon="📊",
    layout="wide"
)
# Title of the app
st.title("Sistema de Visualização de Dados")
# Subtitle
st.subheader("Análise de Dados com Streamlit")
# Sidebar for navigation
st.sidebar.title("Navegação")
st.sidebar.markdown("Selecione uma opção para visualizar os dados.")
# Options for the sidebar
options = ["Introdução", "Gráfico de Linhas", "Gráfico de Barras", "Gráfico de Dispersão", "Tabela de Dados"]
choice = st.sidebar.selectbox("Selecione uma opção:", options)
# Load sample data
data = pd.DataFrame({
    "Ano": [2020, 2021, 2022, 2023],
    "Vendas": [150, 200, 250, 300],
    "Lucro": [50, 80, 100, 120],
    "Categoria": ["A", "B", "A", "B"]
})
# Function to display introduction
def show_introduction():
    st.write("Bem-vindo ao sistema de visualização de dados")
    st.write("Esta aplicação permite explorar diferentes tipos de gráficos e tabelas.")
    st.write("Use o menu lateral para navegar entre as opções disponíveis.")
# Function to display line chart
def show_line_chart():
    st.subheader("Gráfico de Linhas")
    metric = st.selectbox("Selecione a métrica:", ["Vendas", "Lucro"])
    fig = px.line(data, x="Ano", y=metric, title=f"{metric} ao Longo dos Anos")
    st.plotly_chart(fig)
# Function to display bar chart
def show_bar_chart():
    st.subheader("Gráfico de Barras")
    metric = st.selectbox("Selecione a métrica:", ["Vendas", "Lucro"])
    fig = px.bar(data, x="Ano", y=metric, title=f"{metric} por Ano")
    st.plotly_chart(fig)

# Function to display scatter plot
def show_scatter_plot():
    st.subheader("Gráfico de Dispersão")
    fig = px.scatter(data, x="Vendas", y="Lucro", color="Categoria", title="Relação entre Vendas e Lucro")
    st.plotly_chart(fig)

# Function to display data table
def show_data_table():
    st.subheader("Tabela de Dados")
    st.dataframe(data)
# Parte da lógica principal do sistema
if choice == "Introdução":
    show_introduction()
elif choice == "Gráfico de Linhas":
    show_line_chart()
elif choice == "Gráfico de Barras":
    show_bar_chart()
elif choice == "Gráfico de Dispersão":
    show_scatter_plot()
elif choice == "Tabela de Dados":
    show_data_table()
import streamlit as st
import pandas as ps
import plotly_express as px

st.header('Histograma de vendas de carros')

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um h')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

    # ---------------------------------------------------

# Criar botões
hist_button = st.button('Criar histograma')
scatter_button = st.button('Criar gráfico de dispersão')

# Ação ao clicar no botão de histograma
if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Ação ao clicar no botão de gráfico de dispersão
if scatter_button:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Dispersão de Preço vs Odômetro")
    st.plotly_chart(fig, use_container_width=True)

    # --------------------------------------------------

    # Criar caixas de seleção
hist_checkbox = st.checkbox('Criar histograma')
scatter_checkbox = st.checkbox('Criar gráfico de dispersão')

# Ação ao selecionar a caixa de seleção do histograma
if hist_checkbox:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Ação ao selecionar a caixa de seleção do gráfico de dispersão
if scatter_checkbox:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Dispersão de Preço vs Odômetro")
    st.plotly_chart(fig, use_container_width=True)

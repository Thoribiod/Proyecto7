import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón

    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:

    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre Odómetro y Precio")

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

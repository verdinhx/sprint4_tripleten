import streamlit as st 
import pandas as pd 
import plotly_express as px

# lendo os dados
car_data = pd.read_csv('notebooks/vehicles_us_modify.csv') 

# adicionando um cabeçalho
st.markdown("## Used car sales in usa")
st.markdown("The data displayed on this page are car sales advertisements in the period from May 2018 to April 2019")

# criando um botão
colors_button = st.button('Sales by colors') 
scatter_button = st.button('Price, Mileage and Conservation')

if colors_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Creating a histogram for the colors of cars on sale ads')
    
    # criar um histograma
    fig = px.histogram(
                        car_data, 
                        x='paint_color', 
                        title='Number of Vehicles by Color'
                    ).update_xaxes(categoryorder='total descending')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write('Creating a chart to visualize the price and mileage by vehicle condition')
    fig = px.scatter(
                    car_data, 
                    x='odometer', 
                    y='price', 
                    color='condition',
                    opacity=0.5,
                    title='Price vs. Mileage by State of Conservation'
                )
    st.plotly_chart(fig, use_container_width=True)
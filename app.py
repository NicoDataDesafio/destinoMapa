import streamlit as st
import psycopg2
import pandas as pd
import folium
import plotly.express as px
from streamlit_folium import folium_static

import os

my_database = os.environ.get('my_database')
my_host = os.environ.get('my_host')
my_password = os.environ.get('my_password')
my_port = os.environ.get('my_port')
my_user = os.environ.get('my_user')

# Configura las variables de conexión
HOST = my_host
DATABASE = my_database
USER = my_user
PASSWORD = my_password
PORT = my_port  # Asegúrate de que este valor sea un entero

# Configura la conexión a la base de datos
def get_db_connection():
    return psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT
    )

# Función para ejecutar consultas SQL y devolver un DataFrame de Pandas
def sql_query(query):
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Página de inicio
st.set_page_config(page_title="Inside", page_icon="img/cropped-Beyond-Education_Horizonatal-color.png")
st.markdown('# Inside Beyond Education', unsafe_allow_html=True)

# Menú lateral
option = st.sidebar.selectbox('Navigation', ['Home', 
                                             'Destinos de interés',
                                             'Destinos voluntariados', 
                                             'Destinos campamentos'])



# Si selecciona 'Destinos voluntariados', mostrar el mapa de folium.Marker
if option == 'Destinos voluntariados':


    
    # Crear un DataFrame con los destinos y sus coordenadas
    data = {
        'destinos': ['<a href=https://fr.wikipedia.org/wiki/Place_Guillaume_II target=_blank>Place Guillaume II</a>', 'Ecuador', 'Panamá', 'Australia', 'Cambodia', 'Fiji', 'Ghana', 'Grecia', 'Hawai', 'Marruecos', 'Perú', 'República Dominicana', 'Tailandia', 'Tanzania', 'Vietnam'],
        'latitud': [9.7489, -1.8312, 8.5380, -25.2744, 12.5657, -17.7134, 7.9465, 39.0742, 19.8968, 31.7917, -9.1899, 18.7357, 15.8700, -6.3690, 14.0583],
        'longitud': [-83.7534, -78.1834, -80.7821, 133.7751, 104.9910, 178.0650, -1.0232, 21.8243, -155.5828, -7.0926, -75.0152, -70.1627, 100.9925, 34.8888, 108.2772]
    }
    df_destinos = pd.DataFrame(data)

    # Crear el mapa con folium.Marker
    mymap = folium.Map(location=[0, 0], zoom_start=2)
    for _, row in df_destinos.iterrows():
        tooltip = "Click me!"
        folium.Marker([row['latitud'], row['longitud']], popup=row['destinos'],tooltip=tooltip).add_to(mymap)

    # Mostrar el mapa en Streamlit
    folium_static(mymap)

# Si selecciona 'Destinos campamentos', mostrar el mapa con los destinos de campamentos
elif option == 'Destinos campamentos':


    # Crear un DataFrame con los destinos de campamentos y sus coordenadas
    data_campamentos = {
        'destinos': ['West Sussex', 'Crawley', 'Northampton', 'Buckinghamshire', 'Dorset', 'London', 'Manchester', 
                     'Biarritz', 'French Alps', 'Switzerland', 'Swiss Alps', 'Maine', 'New Hampshire', 'Pennsylvania', 
                     'Florida', 'Santander', 'Barcelona', 'Madrid', 'León', 'Berlin', 'Canada', 'Dublin'],
        'latitud': [50.8091, 51.1092, 52.2405, 51.9943, 50.7151, 51.5074, 53.4808, 43.4832, 45.8325, 46.8182, 46.8182, 45.2538, 
                    43.1939, 40.7128, 27.9944, 43.4623, 41.3851, 40.4168, 42.5987, 52.5200, 53.3498, 53.3498],
        'longitud': [-0.7539, -0.1872, -0.9027, -0.7394, -2.4406, -0.1278, -2.2426, -1.5586, 6.6113, 8.2275, 8.2275, -69.4455, 
                     -71.5724, -77.0369, -81.7603, -3.8196, 2.1734, -3.7038, -5.5671, 13.4050, -106.3468, -6.2603]
    }

    df_campamentos = pd.DataFrame(data_campamentos)

    # Crear el mapa con folium.Marker
    mymap_campamentos = folium.Map(location=[0, 0], zoom_start=2)
    for _, row in df_campamentos.iterrows():
        folium.Marker([row['latitud'], row['longitud']], popup=row['destinos']).add_to(mymap_campamentos)
        folium.TileLayer('Stamen Terrain').add_to(mymap_campamentos)


    # Mostrar el mapa en Streamlit
    folium_static(mymap_campamentos)

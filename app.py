import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from streamlit_option_menu import option_menu


# Página de inicio
st.set_page_config(layout="wide", page_title="Destinos", page_icon="img/cropped-Beyond-Education_Horizonatal-color.png")

st.get_option("theme.primaryColor")
st.get_option("theme.secondaryBackgroundColor")
st.get_option("server.enableCORS")
st.get_option("server.enableXsrfProtection")

# Menú lateral
# Menú superior
selected = option_menu(
    menu_title=None,  # Dejar el título del menú vacío
    options=['Voluntariados', 'Campamentos'],  # Opciones del menú
    icons=['map', 'map'],  # Iconos de cada opción
    menu_icon="cast",  # Icono del menú
    default_index=0,  # Índice de la opción por defecto
    orientation="horizontal",  # Orientación del menú
)


# Si selecciona 'Destinos voluntariados', mostrar el mapa de folium.Marker
if selected == 'Voluntariados':


    
    # Crear un DataFrame con los destinos y sus coordenadas
    data = {
        'destinos': ['<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Costa Rica</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Ecuador</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Panama</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Australia</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Camboya</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Fiji</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Ghana</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Grecia</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Hawai</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Marruecos</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Perú</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Republica Dominicana</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Tailandia</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Tanzania</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Voluntariado2024_compressed.pdf target=_blank>Vietnam</a>'],

        'latitud': [9.7489, -1.8312, 8.5380, -25.2744, 12.5657, -17.7134, 7.9465, 39.0742, 19.8968, 31.7917, -9.1899, 18.7357, 15.8700, -6.3690, 14.0583],
        'longitud': [-83.7534, -78.1834, -80.7821, 133.7751, 104.9910, 178.0650, -1.0232, 21.8243, -155.5828, -7.0926, -75.0152, -70.1627, 100.9925, 34.8888, 108.2772]
    }
    df_destinos = pd.DataFrame(data)

    # Crear el mapa con folium.Marker
    mymap = folium.Map(location=[0, 0], zoom_start=2)
    for _, row in df_destinos.iterrows():
        
        folium.Marker([row['latitud'], row['longitud']], popup=row['destinos']).add_to(mymap)

    # Mostrar el mapa en Streamlit
    folium_static(mymap,width=1500)

# Si selecciona 'Destinos campamentos', mostrar el mapa con los destinos de campamentos
elif selected == 'Campamentos':


    # Crear un DataFrame con los destinos de campamentos y sus coordenadas
    data_campamentos = {
        'destinos': ['<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_ReinoUnido2024_compressed.pdf target=_blank>West Sussex</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_ReinoUnido2024_compressed.pdf target=_blank>Crawley</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_ReinoUnido2024_compressed.pdf target=_blank>Northampton</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_ReinoUnido2024_compressed.pdf target=_blank>Buckinghamshire</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_ReinoUnido2024_compressed.pdf target=_blank>Dorset</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_ReinoUnido2024_compressed.pdf target=_blank>London</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_ReinoUnido2024_compressed.pdf target=_blank>Manchester</a>', 
                     '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Francia2024_compressed.pdf target=_blank>Biarritz</a>', 
                     '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Francia2024_compressed.pdf target=_blank>French Alps</a>', 
                     '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Suiza2024_compressed.pdf target=_blank>Switzerland</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Suiza2024_compressed.pdf target=_blank>Swiss Alps</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_EstadosUnidos2024_compressed.pdf target=_blank>Maine</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_EstadosUnidos2024_compressed.pdf target=_blank>New Hampshire</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_EstadosUnidos2024_compressed.pdf target=_blank>Pennsylvania</a>', 
                     '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_EstadosUnidos2024_compressed.pdf target=_blank>Florida</a>', 
                     '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Espana2024_compressed.pdf target=_blank>Santander</a>', 
                     '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Espana2024_compressed.pdf target=_blank>Barcelona</a>', 
                     '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Espana2024_compressed.pdf target=_blank>Madrid</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Espana2024_compressed.pdf target=_blank>León</a>',
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Alemania2024-comprimido.pdf target=_blank>Berlin</a>', 
                    '<a href=https://beyondeducation.es/wp-content/uploads/2024/02/Catalogo_Campamentos_Canada2024-comprimido.pdf target=_blank>Canada</a>',
                    '<a href=https://beyondeducation.es/campamentos-verano/ target=_blank>Dublin</a>'],
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


    # Mostrar el mapa en Streamlit
    folium_static(mymap_campamentos,width=1500)

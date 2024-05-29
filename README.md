
# Aplicación de Visualización de Mapas con Streamlit

Esta aplicación está desarrollada con Streamlit y muestra mapas interactivos que señalan ubicaciones de voluntariados y campamentos. Al hacer clic en las banderas de cada ubicación, se abre un enlace con más información.

## Descripción

La aplicación tiene dos principales funcionalidades:
- **Voluntariados**: Muestra un mapa con las ubicaciones de varios programas de voluntariado.
- **Campamentos**: Muestra un mapa con las ubicaciones de diferentes campamentos.

## Tecnologías Utilizadas

- Python
- Streamlit
- psycopg2
- pandas
- folium
- plotly
- streamlit-folium
- streamlit-option-menu

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/NicoDataDesafio/destinoMapa.git
    cd tu_repositorio
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```


## Ejecución

Para ejecutar la aplicación de Streamlit, usa el siguiente comando:

```bash
streamlit run app.py
```

## Uso

Una vez que la aplicación esté en funcionamiento, puedes navegar por las diferentes secciones utilizando el menú superior:

    Voluntariados: Visualiza el mapa con las ubicaciones de programas de voluntariado. Haz clic en las banderas para abrir enlaces con más información.
    Campamentos: Visualiza el mapa con las ubicaciones de campamentos. Haz clic en las banderas para abrir enlaces con más información.
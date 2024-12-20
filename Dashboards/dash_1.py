import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Cargar el archivo CSV
file_path = "datasets/peliculasdatos_limpio.csv"
data = pd.read_csv(file_path)

#Para el menu
def dashboard():
    return html.Div(
        [
            html.H1("Calificación y Duración de Películas", style={"text-align": "center", "color": "#ffffff"}),

            # Dropdown para seleccionar una película o todas
            html.Div(
                style={"width": "50%", "margin": "auto", "padding": "10px"},
                children=[
                    dcc.Dropdown(
                        id='pelicula-dropdown',
                        options=[{'label': 'Todas las películas', 'value': 'todas'}] +  # Opción para mostrar todas
                                [{'label': title, 'value': title} for title in data['titulo'].unique()],
                        value='todas',  # Valor inicial (mostrar todas las películas)
                        style={
                            'backgroundColor': '#ffffff',  # Fondo oscuro
                            'color': '#000000',         # Texto negro
                            'border': '1px solid #555'  # Bordes oscuros
                        }
                    )
                ]
            ),

            # Div para mostrar los detalles de la película seleccionada
            html.Div(
                id='detalle-pelicula',
                style={
                    "text-align": "center",
                    "margin-top": "20px",
                    "font-size": "18px",
                    "backgroundColor": "#333",  # Fondo oscuro
                    "color": "#ffffff",  # Texto blanco
                    "padding": "10px",  # Espaciado interno
                    "border": "1px solid #555",  # Borde oscuro
                    "borderRadius": "5px",  # Bordes redondeados
                    "width": "50%",
                    "margin": "20px auto"  # Centrar el componente horizontalmente
                }
            ),

            # Gráfico para mostrar la duración y la calificación
            dcc.Graph(id='grafica', style={"margin-top": "20px"})
        ]
    )

# Callback para actualizar la gráfica al seleccionar una película o todas
def registrar_callbacks(app):
    @app.callback(
        [Output('grafica', 'figure'),
         Output('detalle-pelicula', 'children')],
        Input('pelicula-dropdown', 'value')
    )
    def actualizar_grafica_y_detalles(seleccion):
        if seleccion == 'todas':
            # Mostrar todas las películas en el gráfico
            fig = go.Figure(data=[
                go.Scatter(
                    x=data['duracion'],  # Todas las duraciones en el eje X
                    y=data['calificacion'],  # Todas las calificaciones en el eje Y
                    mode='markers',
                    hovertext=data['titulo'],  # Mostrar el título de la película como tooltip
                    marker=dict(size=10, color='cyan')  # Personalizar los marcadores
                )
            ])
            fig.update_layout(
                title="Todas las películas",
                xaxis_title="Duración",
                yaxis_title="Calificación",
                xaxis=dict(type='category'),  # Eje X como categorías para duraciones
                yaxis=dict(range=[0, 10]),  # Rango para calificaciones de 0 a 10
                template='plotly_dark'  # Tema oscuro para el gráfico
            )
            detalle = "Selecciona una película para ver más detalles."
        else:
            # Mostrar solo la película seleccionada en el gráfico
            pelicula = data[data['titulo'] == seleccion].iloc[0]
            fig = go.Figure(data=[
                go.Scatter(
                    x=[pelicula['duracion']],  # Duración de la película seleccionada
                    y=[pelicula['calificacion']],  # Calificación de la película seleccionada
                    mode='markers',
                    hovertext=[seleccion],  # Mostrar el título como tooltip
                    marker=dict(size=15, color='red')  # Personalizar el marcador
                )
            ])
            fig.update_layout(
                title=f"Película seleccionada: {seleccion}",
                xaxis_title="Duración",
                yaxis_title="Calificación",
                xaxis=dict(type='category'),  # Eje X como categorías para duraciones
                yaxis=dict(range=[0, 10]),  # Rango para calificaciones de 0 a 10
                template='plotly_dark'  # Tema oscuro para el gráfico
            )

            # Mostrar los detalles de la película seleccionada
            detalle = f"""
            Película: {seleccion}  
            Calificación: {pelicula['calificacion']}  
            Duración: {pelicula['duracion']}
            """

        return fig, detalle

# Código principal para ejecutar el archivo independiente
if __name__ == '__main__':
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
    app.layout = dashboard()
    registrar_callbacks(app)
    app.run_server(debug=True)


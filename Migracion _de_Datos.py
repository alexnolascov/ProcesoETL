import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Cargar el archivo CSV
file_path = r"datasets/peliculasdatos_limpio.csv"
data = pd.read_csv(file_path)

# Iniciar la aplicación Dash con el tema oscuro de Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# CSS personalizado para aplicar estilo oscuro al menú desplegable
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Temática Oscura</title>
        {%favicon%}
        {%css%}
        <style>
            .dropdown-menu {
                background-color: #333 !important; /* Fondo oscuro */
                color: #fff !important; /* Texto blanco */
                border: 1px solid #555 !important; /* Borde oscuro */
            }
            .dropdown-item {
                background-color: #060606  !important; /* Fondo oscuro para cada ítem */
                color: #fff !important; /* Texto blanco */
            }
            .dropdown-item:hover {
                background-color: #444 !important; /* Fondo más claro al pasar el cursor */
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""

# Layout de la aplicación
app.layout = html.Div(
    style={
        "backgroundColor": "#121212",  # Fondo general oscuro
        "padding": "20px",  # Espaciado general
    },
    children=[
        html.H1(
            "Calificación y Duración de Películas",
            style={"text-align": "center", "color": "#ffffff"},  # Título con texto blanco
        ),

        # Dropdown para seleccionar una película o todas
        html.Div(
            style={"width": "50%", "margin": "auto", "padding": "10px"},
            children=[
                dbc.Select(
                    id="pelicula-dropdown",
                    options=[
                        {"label": "Todas las películas", "value": "todas"}
                    ]
                    + [{"label": title, "value": title} for title in data["titulo"].unique()],
                    value="todas",  # Valor inicial
                    style={
                        "backgroundColor": "# 060606 ",  # Fondo oscuro del dropdown inicial
                        "color": "#ffffff",  # Texto blanco
                        "border": "1px solid #555",  # Borde oscuro
                    },
                )
            ],
        ),

        # Div para mostrar los detalles de la película seleccionada
        html.Div(
            id="detalle-pelicula",
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
                "margin": "20px auto",  # Centrar el componente horizontalmente
            },
        ),

        # Gráfico para mostrar la duración y la calificación
        dcc.Graph(id="grafica", style={"margin-top": "20px", "backgroundColor": "#333"}),
    ],
)


# Callback para actualizar la gráfica al seleccionar una película o todas
@app.callback(
    [Output("grafica", "figure"), Output("detalle-pelicula", "children")],
    Input("pelicula-dropdown", "value"),
)
def actualizar_grafica_y_detalles(seleccion):
    if seleccion == "todas":
        # Mostrar todas las películas en el gráfico
        fig = go.Figure(
            data=[
                go.Scatter(
                    x=data["duracion"],  # Todas las duraciones en el eje X
                    y=data["calificacion"],  # Todas las calificaciones en el eje Y
                    mode="markers",
                    hovertext=data["titulo"],  # Mostrar el título de la película como tooltip
                    marker=dict(size=10, color="cyan"),  # Personalizar los marcadores
                )
            ]
        )
        fig.update_layout(
            title="Todas las películas",
            xaxis_title="Duración",
            yaxis_title="Calificación",
            xaxis=dict(type="category"),  # Eje X como categorías para duraciones
            yaxis=dict(range=[0, 10]),  # Rango para calificaciones de 0 a 10
            template="plotly_dark",  # Tema oscuro para el gráfico
        )
        detalle = "Selecciona una película para ver más detalles."
    else:
        # Mostrar solo la película seleccionada en el gráfico
        pelicula = data[data["titulo"] == seleccion].iloc[0]
        fig = go.Figure(
            data=[
                go.Scatter(
                    x=[pelicula["duracion"]],  # Duración de la película seleccionada
                    y=[pelicula["calificacion"]],  # Calificación de la película seleccionada
                    mode="markers",
                    hovertext=[seleccion],  # Mostrar el título como tooltip
                    marker=dict(size=15, color="red"),  # Personalizar el marcador
                )
            ]
        )
        fig.update_layout(
            title=f"Película seleccionada: {seleccion}",
            xaxis_title="Duración",
            yaxis_title="Calificación",
            xaxis=dict(type="category"),  # Eje X como categorías para duraciones
            yaxis=dict(range=[0, 10]),  # Rango para calificaciones de 0 a 10
            template="plotly_dark",  # Tema oscuro para el gráfico
        )

        # Mostrar los detalles de la película seleccionada
        detalle = f"""
        Película: {seleccion}  
        Calificación: {pelicula['calificacion']}  
        Duración: {pelicula['duracion']}
        """

    return fig, detalle


# Ejecutar el servidor
if __name__ == "__main__":
    app.run_server(debug=True)
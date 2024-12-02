import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Cargar y procesar datos
data = pd.read_csv(r"datasets/peliculasdatos_limpio.csv")

# Asegurar que las columnas clave sean numéricas
data['ano'] = pd.to_numeric(data['ano'], errors='coerce')
data['calificacion'] = pd.to_numeric(data['calificacion'], errors='coerce')

# Crear una nueva columna para identificar la década
data['decada'] = (data['ano'] // 10) * 10

# Para el menú
def dashboard():
    return html.Div([
        html.H1("Películas por Década", style={'text-align': 'center'}),

        # Dropdown para seleccionar la década
        html.Div([
            html.Label("Selecciona una década:", style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='decada-dropdown',
                options=[
                    {'label': f"{int(decada)}s", 'value': decada} for decada in sorted(data['decada'].dropna().unique())
                ],
                value=1980,  # Década inicial seleccionada
                style={
                    'width': '50%',
                    'margin': 'auto',
                    'backgroundColor': '#ffffff',  # Color de fondo del dropdown
                    'color': 'black',  # Color del texto
                    'borderColor': '#444',  # Color del borde
                    'borderRadius': '5px',  # Esquinas redondeadas
                    'padding': '10px'
                }
            )
        ], style={'width': '80%', 'margin': 'auto', 'text-align': 'center', 'margin-bottom': '20px'}),

        # Gráfico interactivo
        dcc.Graph(id='grafica-decada', style={'margin-top': '20px'})
    ])

# Callback para actualizar la gráfica según la década seleccionada
def registrar_callbacks(app):
    @app.callback(
        Output('grafica-decada', 'figure'),
        Input('decada-dropdown', 'value')
    )
    def actualizar_grafica(decada_seleccionada):
        # Filtrar los datos según la década seleccionada
        peliculas_filtradas = data[data['decada'] == decada_seleccionada]

        # Si no hay películas para esa década, mostrar un mensaje vacío
        if peliculas_filtradas.empty:
            return {
                "data": [],
                "layout": {
                    "title": f"No hay películas registradas en la década de {int(decada_seleccionada)}s.",
                    "xaxis": {"title": "Películas"},
                    "yaxis": {"title": "Calificación", "range": [0, 10]}
                }
            }

        # Crear la gráfica
        fig = px.bar(
            peliculas_filtradas,
            x='titulo',
            y='calificacion',
            title=f"Películas de la Década de {int(decada_seleccionada)}s",
            labels={"titulo": "Título", "calificacion": "Calificación"},
            text='calificacion'
        )
        fig.update_traces(textposition='outside')  # Mostrar las calificaciones fuera de las barras
        fig.update_layout(xaxis_title="Películas", yaxis_title="Calificación", template="plotly_white")

        return fig


# Código principal para ejecutar el archivo independiente
if __name__ == "__main__":
    app = dash.Dash(__name__)
    app.layout = dashboard()
    registrar_callbacks(app)
    app.run_server(debug=True)


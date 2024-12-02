import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Cargar y procesar datos
data = pd.read_csv(r"Datasets/peliculasdatos_limpio.csv")

def convert_duration(duration):
    try:
        time_parts = duration.split("h")
        hours = int(time_parts[0].strip())
        minutes = int(time_parts[1].strip().replace("m", "").strip())
        return hours * 60 + minutes
    except:
        return 0  # Si la duración es desconocida o tiene formato incorrecto

data['duracion_minutos'] = data['duracion'].apply(convert_duration)
data['calificacion'] = pd.to_numeric(data['calificacion'], errors='coerce')  # Asegurar que calificación sea numérica

# Para el menú
def dashboard():
    return html.Div([
        html.H1("Películas Mejor Calificadas", style={'text-align': 'center'}),

        # Input para seleccionar calificaciones desde 8.0 hasta 10.0
        html.Div([
            html.Label("Selecciona la calificación:", style={'font-weight': 'bold'}),
            dcc.Input(
                id='calificacion-input',
                type='number',
                min=8.0,
                max=10.0,
                step=0.1,
                value=8.0,  # Valor inicial
                style={'width': '20%'}
            )
        ], style={'width': '80%', 'margin': 'auto', 'text-align': 'center', 'margin-bottom': '20px'}),

        # Gráfico interactivo
        dcc.Graph(id='grafica-peliculas', style={'margin-top': '20px'})
    ])

# Callback para actualizar la gráfica en función de la calificación seleccionada
def registrar_callbacks(app):
    @app.callback(
        Output('grafica-peliculas', 'figure'),
        Input('calificacion-input', 'value')
    )
    def actualizar_grafica(calificacion_seleccionada):
        # Asegurar que la calificación es válida (no nula)
        if calificacion_seleccionada is None:
            return {
                "data": [],
                "layout": {
                    "title": "Por favor selecciona una calificación válida.",
                    "xaxis": {"title": "Películas"},
                    "yaxis": {"title": "Calificación", "range": [0, 10]}
                }
            }

        # Filtrar las películas con calificación igual a la seleccionada
        peliculas_filtradas = data[data['calificacion'] == round(calificacion_seleccionada, 1)]

        # Si no hay películas que cumplan el criterio, mostrar un mensaje vacío
        if peliculas_filtradas.empty:
            return {
                "data": [],
                "layout": {
                    "title": f"No hay películas con calificación = {calificacion_seleccionada:.1f}",
                    "xaxis": {"title": "Películas"},
                    "yaxis": {"title": "Calificación", "range": [8, 10]}
                }
            }

        # Crear el gráfico
        fig = px.bar(
            peliculas_filtradas,
            x='titulo',
            y='calificacion',
            title=f"Películas con Calificación = {calificacion_seleccionada:.1f}",
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

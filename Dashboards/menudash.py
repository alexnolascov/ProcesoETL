import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import welcome as w
import dash_1 as d1
import dash_2 as d2
import dash_3 as d3

# Crear la aplicación principal
app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.DARKLY,  # Estilo general oscuro proporcionado por Bootstrap.
        'https://fonts.googleapis.com/css2?family=Fjalla+One&display=swap'  # Fuente Fjalla One para usar en toda la aplicación.
    ],
    suppress_callback_exceptions=True,  # Permite que existan callbacks en otros archivos.
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}]  # Permite que el diseño sea responsivo en dispositivos móviles.
)

# Sidebar del menú de navegación
sidebar = html.Div(
    [
        # Título del sidebar
        html.H2(
            "DashBoard Películas IMDB",
            className="display-5",  # Clase de Bootstrap para el tamaño del texto.
            style={
                'color': '#FFD700',  # Color dorado para el título.
                'font-family': 'Fjalla One, sans-serif',  # Fuente elegida
                'text-align': 'center',  # Centrado del texto
                'text-shadow': '2px 2px 4px rgba(0, 0, 0, 0.5)'  # Sombra suave en el texto
            }
        ),
        html.Hr(style={'border-color': '#FFD700'}),  # Línea divisoria con color dorado.

        # Navegación del sidebar
        dbc.Nav(
            [
                # Enlace 1: Home
                dbc.NavLink(
                    html.Div([html.I(className="fas fa-home"), " Inicio"]),
                    href="/",  # Ruta de la página de inicio
                    active="exact",  # Activo cuando la URL coincide exactamente
                    style={
                        'color': '#FFFFFF',  # Color del texto cuando no está activo
                        'font-family': 'Fjalla One, sans-serif',  # Fuente Fjalla One aplicada aquí.
                        'padding': '10px 15px',
                        'font-size': '18px',
                        'border-radius': '8px',
                        'margin-bottom': '10px',
                        'transition': 'background-color 0.3s ease',
                        'background-color': '#000000',  # Color de fondo cuando está activo (negro)
                        'color': '#FFFFFF',  # Color del texto cuando está activo
                        'font-weight': 'bold',  # Poner el texto en negrita cuando está activo
                        'text-shadow': '2px 2px 4px rgba(0, 0, 0, 0.5)'  # Sombra suave en el texto
                    },
                ),

                # Enlace 2: Dashboard 1
                dbc.NavLink(
                    html.Div([html.I(className="fas fa-chart-line"), " Dashboard 1"]),  # Ícono + texto.
                    href="/dash-1",
                    active="exact",
                    style={
                        'color': '#FFFFFF',
                        'font-family': 'Fjalla One, sans-serif',  # Fuente Fjalla One aplicada aquí.
                        'padding': '10px 15px',
                        'font-size': '18px',
                        'border-radius': '8px',
                        'margin-bottom': '10px',
                        'transition': 'background-color 0.3s ease',
                        'background-color': '#ffc51d',  # Color de fondo cuando está activo (amarillo)
                        'color': '#FFFFFF',  # Color del texto cuando está activo
                        'font-weight': 'bold',  # Poner el texto en negrita cuando está activo
                    }
                ),
                # Enlace 3: Dashboard 2
                dbc.NavLink(
                    html.Div([html.I(className="fas fa-chart-bar"), " Dashboard 2"]),
                    href="/dash-2",
                    active="exact",
                    style={
                        'color': '#FFFFFF',
                        'font-family': 'Fjalla One, sans-serif',  # Fuente Fjalla One aplicada aquí.
                        'padding': '10px 15px',
                        'font-size': '18px',
                        'border-radius': '8px',
                        'margin-bottom': '10px',
                        'transition': 'background-color 0.3s ease',
                        'background-color': '#ffc51d',  # Color de fondo cuando está activo (amarillo)
                        'color': '#FFFFFF',  # Color del texto cuando está activo
                        'font-weight': 'bold',  # Poner el texto en negrita cuando está activo
                    }
                ),
                # Enlace 4: Dashboard 3
                dbc.NavLink(
                    html.Div([html.I(className="fas fa-film"), " Dashboard 3"]),
                    href="/dash-3",
                    active="exact",
                    style={
                        'color': '#FFFFFF',
                        'font-family': 'Fjalla One, sans-serif',  # Fuente Fjalla One aplicada aquí.
                        'padding': '10px 15px',
                        'font-size': '18px',
                        'border-radius': '8px',
                        'margin-bottom': '10px',
                        'transition': 'background-color 0.3s ease',
                        'background-color': '#ffc51d',  # Color de fondo cuando está activo (amarillo)
                        'color': '#FFFFFF',  # Color del texto cuando está activo
                        'font-weight': 'bold',  # Poner el texto en negrita cuando está activo
                    }
                ),
            ],
            vertical=True,  # Alineación vertical de los enlaces.
            pills=True  # Estilo de pestañas que resalta la opción activa.
        ),
    ],
    style={
        "position": "fixed",  # La barra lateral está fija en su posición.
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",  # Ancho de la barra lateral.
        "padding": "2rem 1rem",  # Espaciado interno.
        "background-color": "#930b0b",  # Cambié el color de fondo a rojo.
        'color': '#FFFFFF',  # Color del texto por defecto.
        'box-shadow': '2px 0px 10px rgba(0,0,0,0.8)'  # Sombra para darle profundidad.
    }
)

# Contenido principal
content = html.Div(
    id="page-content",  # Este contenedor se actualizará dinámicamente con el contenido de cada página.
    style={
        "margin-left": "18rem",  # Margen izquierdo para dejar espacio a la barra lateral.
        "padding": "2rem 1rem",  # Espaciado interno.
        "background-color": "#ffc51d",  # Cambié el fondo a amarillo.
        "color": "#b60000",  # Color del texto ahora en rojo.
        "font-family": "Fjalla One, sans-serif"  # Fuente aplicada aquí.
    }
)

# Layout de la aplicación
app.layout = html.Div([  # Aquí se configura el layout de la app.
    dcc.Location(id="url"),  # Componente para detectar cambios de URL.
    sidebar,
    content
])

# Callback para cambiar el contenido según la URL
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def render_page_content(pathname):
    if pathname == "/":
        return w.welcome()  # Página de bienvenida.
    elif pathname == "/dash-1":
        return d1.dashboard()  # Dashboard 1.
    elif pathname == "/dash-2":
        return d2.dashboard()  # Dashboard 2.
    elif pathname == "/dash-3":
        return d3.dashboard()  # Dashboard 3.
    else:
        # Página 404 si la URL no coincide.
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ],
            className="p-3 bg-light rounded-3",
        )

# Registrar los callbacks de cada dashboard en sus respectivos módulos
d1.registrar_callbacks(app)
d2.registrar_callbacks(app)
d3.registrar_callbacks(app)

# Ejecutar el servidor principal
if __name__ == "__main__":
    app.run(debug=True)
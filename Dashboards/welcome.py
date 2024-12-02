from dash import Dash, html

def welcome():
    body = html.Div(
        [
            # Título centrado con Fjalla One
            html.H3(
                "BIENVENIDOS AQUÍ ESTÁN LOS MEJORES DATOS DE PELICULAS!!",
                style={
                    'font-family': 'Fjalla One, sans-serif',  # Cambié la fuente a Fjalla One
                    'textAlign': 'center',  # Centra el texto horizontalmente
                    'font-size': '2em',  # Ajuste de tamaño de la fuente
                    'text-shadow': '2px 2px 4px rgba(0, 0, 0, 0.5)'  # Sombra suave en el texto
                }
            ),

            # Imagen más grande y centrada
            html.Img(
                src="https://www.lavanguardia.com/andro4all/hero/2023/12/imdb-2023.jpg?width=1200&aspect_ratio=16:9",
                style={
                    'width': '80%',  # Ajuste de tamaño
                    'max-width': '800px',  # Tamaño máximo
                    'height': 'auto',  # Mantener proporción
                    'display': 'block',  # Centrado
                    'margin-left': 'auto',  # Centra imagen
                    'margin-right': 'auto',  # Centra imagen
                },
                title="Películas IMDB"
            ),

            html.Hr(),  # Separación horizontal

            # Listas
            html.H4(
                "Aquí tendrás una mayor información sobre alguna película que quieras ver en tus ratos libres.",
                style={
                    'font-family': 'Fjalla One, sans-serif',
                    'font-size': '1.5em'  # Tamaño de la fuente incrementado
                }
            ),
            html.Ul(
                [
                    html.Li("Acción", style={'font-family': 'Fjalla One, sans-serif', 'font-size': '1.2em'}),
                    html.Li("Terror", style={'font-family': 'Fjalla One, sans-serif', 'font-size': '1.2em'}),
                    html.Li("Amor", style={'font-family': 'Fjalla One, sans-serif', 'font-size': '1.2em'}),
                    html.Li("Suspenso", style={'font-family': 'Fjalla One, sans-serif', 'font-size': '1.2em'})
                ]
            ),
            html.H4(
                "Integrantes:",
                style={
                    'font-family': 'Fjalla One, sans-serif',
                    'font-size': '1.5em'  # Tamaño de la fuente incrementado
                }
            ),
            html.Ol(
                [
                    html.Li("Katherin Morales", style={'font-family': 'Fjalla One, sans-serif', 'font-size': '1.2em'}),
                    html.Li("Alejandro Nolasco", style={'font-family': 'Fjalla One, sans-serif', 'font-size': '1.2em'}),
                    html.Li("Paul Serrano", style={'font-family': 'Fjalla One, sans-serif', 'font-size': '1.2em'}),
                    html.Li("Linda Vazquez", style={'font-family': 'Fjalla One, sans-serif', 'font-size': '1.2em'})
                ]
            )
        ],
        style={'font-family': 'Fjalla One, sans-serif'}  # Aplica la fuente a todo el contenedor
    )
    return body

if __name__ == "__main__":
    # Crear la app
    app = Dash(__name__, external_stylesheets=[
        'https://fonts.googleapis.com/css2?family=Fjalla+One&display=swap'  # Enlaza la fuente Fjalla One
    ])

    # Asignar el layout de la app
    app.layout = welcome()

    # Ejecutar el servidor
    app.run(debug=True)
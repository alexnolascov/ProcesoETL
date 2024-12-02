#Webscraping IMDB
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def webscraping():
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size-1020,1200")
    navegador = webdriver.Chrome(service=s, options=opc)

    navegador.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    time.sleep(10)

    data = {"titulo": [], "ano": [], "calificacion": [], "duracion": []}

    # Obtener el contenido HTML de la página
    soup = BeautifulSoup(navegador.page_source, "html5lib")
    peliculas = soup.find_all("div", attrs={"class": "ipc-metadata-list-summary-item__tc"})

    for item in peliculas:
        titulo = item.find("h3", attrs={"class": "ipc-title__text"})
        ano = item.find("span", attrs={"class": "sc-300a8231-7 eaXxft cli-title-metadata-item"})
        calificacion = item.find("span", attrs={"class": "ipc-rating-star--rating"})
        duracion = item.find("span", attrs={"class": "ipc-duration__text"})  # Aquí agregamos la duración

        if titulo:
            data["titulo"].append(titulo.text)
        else:
            data["titulo"].append("Desconocido")

        if ano:
            data["ano"].append(ano.text)
        else:
            data["ano"].append("Desconocido")

        if calificacion:
            data["calificacion"].append(calificacion.text)
        else:
            data["calificacion"].append("Ninguna")

        if duracion:
            data["duracion"].append(duracion.text)
        else:
            data["duracion"].append("Desconocido")

    time.sleep(5)
    navegador.quit()

    df = pd.DataFrame(data)
    df.to_csv("datasetsproductostres.csv", index=False)
    print(df)



if __name__ == '__main__':
    webscraping()
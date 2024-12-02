#Checar Nulos
import pandas as pd

def checar_nulos(df):
    #Esta funcion checa los valores nulos en el DataFrame
    print("Valores nulos por columna:")
    print(df.isnull().sum())
    print("\nTotal de valores nulos en el DataFrame:", df.isnull().sum().sum())
    print("\nPorcentaje de valores nulos por columna:")
    print((df.isnull().sum() / len(df)) * 100)

def reemplazar_nulos(df):
    #Reemplaza valores nulos o "N/A" con el promedio si es numérico, o "Desconocido" si es texto
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:  # Si la columna es numérica
            promedio = df[col].mean()
            df[col] = df[col].fillna(promedio)
        else:  # Si la columna es de texto o categórica
            df[col] = df[col].fillna("Desconocido")
    return df

def verificar_duplicados(df):
    #Verifica duplicados en el DataFrame
    duplicados = df.duplicated()
    print(f"Duplicados encontrados: {duplicados.sum()}")
    return duplicados.sum()

def eliminar_duplicados(df):
    #Elimina filas duplicadas
    df_sin_duplicados = df.drop_duplicates()
    print(f"Filas duplicadas eliminadas: {len(df) - len(df_sin_duplicados)}")
    return df_sin_duplicados

if __name__ == "__main__":
    #Cargar el archivo CSV y tratar "N/A", "na", "", o " " como valores nulos
    df = pd.read_csv("datos/peliculasdatos.csv", na_values=["N/A", "na", "", " "])

    print("\n Verificando Nulos")
    checar_nulos(df)

    print("\n Reemplazando Nulos")
    df = reemplazar_nulos(df)

    print("\n Verificando y Eliminando Duplicados")
    verificar_duplicados(df)
    df = eliminar_duplicados(df)

    # Guardar el DataFrame limpio en un nuevo archivo CSV
    df.to_csv("datos/peliculasdatos_limpio.csv", index=False)
    print("\nArchivo limpio guardado como 'peliculasdatos_limpio.csv'.")
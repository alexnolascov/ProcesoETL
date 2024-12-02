-- Crear la base de datos
CREATE DATABASE PeliculasDB;
USE PeliculasDB;

-- Tabla 1: Anios
CREATE TABLE Anios (
    id_ano INT AUTO_INCREMENT PRIMARY KEY,
    ano INT NOT NULL
);

-- Tabla 2: Duraciones
CREATE TABLE Duraciones (
    id_duracion INT AUTO_INCREMENT PRIMARY KEY,
    duracion VARCHAR(10) NOT NULL,
    duracion_minutos FLOAT NOT NULL
);

-- Tabla 3: Peliculas
CREATE TABLE Peliculas (
    id_pelicula INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    id_ano INT NOT NULL,
    calificacion FLOAT NOT NULL,
    id_duracion INT NOT NULL,
    FOREIGN KEY (id_ano) REFERENCES Anios(id_ano),
    FOREIGN KEY (id_duracion) REFERENCES Duraciones(id_duracion)
);



select * from Peliculas;



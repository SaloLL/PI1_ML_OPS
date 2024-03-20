# <h1 align=center> **PROYECTO INDIVIDUAL PI**
# <h1 align=center> **Salomón Orozco Jaramillo**
### <h1 align=center> `Machine Learning Operations (MLOps)` 

Este proyecto se enfocó en el proceso para crear un MVP (Minimum Viable Product) que maneja los datos extraidos de una empresa de videojuegos llamada Steam, en este trabajo nos toca limpiar todos los archivos que nos entregan con datos (JSON) y convertirlos en estructuras de datos más legibles, y con las que podamos trabajar más adelante en el proyecto.

Enlaces del proyecto:
- Repositorio en GitHub: [SaloLL/PI1_ML_OPS](https://github.com/SaloLL/PI1_ML_OPS/blob/main/README.md)
- Video explicativo: [Video DEMO](https://drive.google.com/file/d/1dqeAzvLWxw8dyaWpSRVWB6iqCQq9MaNY/view?usp=sharing)
- Despliegue: [Deploy en Render](https://pi1-ml-ops.onrender.com/docs)


## <h1 align=center> **`ETL(Extract Transform Load)`**

(Documentos: ETL_SOJ_NBK.ipynb)

En el proyecto presente se muestra el proceso de ML OPS (Machine learning Operations)
Que pasó por los procesos de extracción, transformación y cargado de datos.

### Pasos del tratamiento de datos:

#### ETL general: Datasets - Documento: ETL_SOJ_NBK.ipynb
En el archivo ETL_SOJ_NBK.ipynb se encuentra el tratamiento de datos de australian_user_items, australian_user_reviews y 
output_steam_games, en los que se manejaron  las columnas no deseadas o con errores  tipográficos.
Posteriormente se realizó la limpieza de los datos  mediante la eliminación de filas vacías y valores nulos.
Luego se cargaron los datasets en archivos GZIP para ahorrar espacio porque algunos archivos aunque fueron bien limpiados
tienen una cantidad de datos muy grande.

En el archivo EDA_ML.ipynb  se presentan análisis exploratorios  básicos a través de gráficas para visualizar la distribución de los datos y posteriormente se tomaron decisiones para organizar los datos para el resto del proyecto. 

En el archivo ML_RECOMENDATION.ipynb se tomaron los datos limpios que preparamos anteriormente, y los organizamos para poder entregarlos a un modelo para que este pudiera responder a las predicciones que se le pedirían después.

---
DOCUMENTOS: 
(Se recomienda descargar los .ipynb, en especial ETL_SOJ_NBK.ipynb ya que es extenso)
1. [ETL's y DataFrames del proyecto](ETL_SOJ_NBK.ipynb)
2. [EDA y DataFrames para ML](EDA_ML.ipynb)
3. [Limpieza de Datos para la función de ML](ML_RECOMENDATION.ipynb)
---

## <H1 align=center> **`Documentación de API`**
# Descripción de las Funciones API
## max_playtime_year
Esta función devuelve el año con el mayor tiempo total de juego para juegos del género especificado.
### Parámetros
- `genre`: Género para filtrar los juegos.
### Devuelve
- `int`: Año con el mayor tiempo total de juego para el género especificado. Si no se encuentra el género, devuelve un mensaje.
---
## user_by_game_genre
Esta función devuelve el jugador con el mayor tiempo total de juego para juegos del género especificado.
### Parámetros
- `genre`: Género para filtrar los juegos.
### Devuelve
- `int`: Usuario con el mayor tiempo total de juego para el género especificado. Si no se encuentra el género, devuelve un mensaje.
---
## get_recommendations
Esta función devuelve juegos recomendados para el usuario especificado.
### Parámetros
- `user`: Usuario para quien se solicitan las recomendaciones.
### Devuelve
- `List[str]`: Lista de juegos recomendados. Si no se encuentra el usuario, devuelve un mensaje.


## <h1 align=center> **`Funciones`**

## max_playtime_year
Esta función devuelve el año con el mayor tiempo de juego total para el género especificado.
### Parámetros
- `hours_per_year` (DataFrame): DataFrame que contiene información sobre el tiempo de juego por año y género.
- `genre` (str): El género para buscar.
### Devuelve
- `int` o `str`: El año con el mayor tiempo de juego total para el género especificado, o un mensaje si el género no se encuentra.
### Funcionamiento
1. Convierte el género a minúsculas para realizar una búsqueda que no distinga mayúsculas de minúsculas.
2. Filtra el DataFrame para retener solo las filas con el género especificado.
3. Verifica si se encuentran filas para el género.
   - Si se encuentran filas, busca el año con el mayor tiempo de juego total para el género.
   - Si no se encuentran filas, devuelve un mensaje indicando que no se pudo encontrar el género.
4. Maneja cualquier excepción que pueda ocurrir durante el procesamiento y las imprime en la consola.
---
## max_player_time_per_genre
Esta función devuelve el jugador con el mayor tiempo de juego total para el género especificado, junto con el tiempo de juego por año para ese género.
### Parámetros
- `hours_per_year` (DataFrame): DataFrame que contiene información sobre el tiempo de juego por año y género.
- `player_maxtime_genre` (DataFrame): DataFrame que contiene información sobre el tiempo de juego máximo por jugador y género.
- `genre` (str): El género para buscar.
### Devuelve
- `dict`: Un diccionario que contiene el ID del usuario con más horas jugadas para el género especificado y el tiempo de juego por año para ese género. Si no se encuentra el género, devuelve un mensaje de error.
### Funcionamiento
1. Convierte la entrada del género a minúsculas y elimina los espacios en blanco al principio y al final.
2. Filtra el DataFrame para incluir solo las filas con el género especificado.
3. Verifica si se encuentran filas para el género.
   - Si no se encuentran filas, devuelve un mensaje de error.
   - Si se encuentran filas, agrupa el DataFrame `player_maxtime_genre` por 'Posted_Year' y suma el tiempo de juego.
4. Encuentra el usuario con el mayor tiempo de juego para el género.
5. Construye un diccionario de respuesta que contiene el ID del usuario y las horas jugadas por año.
6. Devuelve el diccionario de respuesta.
7. Maneja cualquier excepción que pueda ocurrir durante el procesamiento e imprime los detalles del error en la consola.
---
# Modelo de recomendación:
## recommend_games_for_user
Esta función recibe un DataFrame de revisiones y un identificador de usuario como entrada y devuelve recomendaciones de juegos para el usuario especificado.
### Parámetros
- `df_reviews`: DataFrame que contiene las revisiones de los juegos.
- `User_Id`: Identificador del usuario para quien se solicitan las recomendaciones.
### Devuelve
- `str`: Mensaje que contiene las recomendaciones de juegos para el usuario especificado. Si el nombre de usuario no se encuentra, devuelve un mensaje indicando que no se encontró el nombre de usuario.
### Funcionamiento
1. Transforma el DataFrame en una matriz de usuarios y juegos.
2. Divide los datos en conjuntos de entrenamiento y prueba.
3. Entrena un modelo de vecinos más cercanos (KNN).
4. Intenta encontrar el índice del usuario en los datos de entrenamiento.
5. Encuentra los vecinos más cercanos al usuario seleccionado.
6. Realiza recomendaciones basadas en los vecinos más cercanos, excluyendo al propio usuario.
7. Retorna un mensaje con las recomendaciones de juegos para el usuario especificado.
---
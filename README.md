# Clasificacion-de-texto
Este clasificador de texto es un sencillo modelo que sirve como herramienta para clasificar las frases en tres categorías: positivas, negativas y neutras. 

## En qué consiste el modelo

1. **Carga de Datos**: Es un archivo .csv con frases y comentarios.

2. **Procesamiento de Datos**: Una vez se ingresan los datos, la aplicación procesa la información y la prepara para la clasificación. Esto incluye aplicar train_test_split para dividir el conjunto de datos en conjunto de entrenamiento y prueba. Adicionalmente se aplicó un vectorizador TF-IDF el cual permite convertir texto en una matriz numérica que se puede utilizar para entrenar y probar modelos de aprendizaje automático.

3. **Clasificación con SVC**: Se entrena el modelo SVM con los datos proporcionados. El modelo analiza los patrones y las relaciones entre los diferentes parámetros.

4. **Evaluación del modelo**: Se aplica la métrica accuracy (número de predicciones correctas dividido por el número total de predicciones) para la evaluación del modelo. Se obtuvo un score de 0.8409. 

5. **Guadar modelo**: Se guarda el modelo en formato .pickle para posteriomente llevarlo a nuestra aplicación web. 

## En qué consiste la interfaz 

1. **Estructura**: La interfaz consiste en tres archivos basicamente: un archivo index.html (esquema de la aplicación web), styles.css (formas, estilos, colores de la interfaz) y app.py (codigo python usando el framework Flask)

2. **App**: La aplicación se basa en el framework Flask de python. Basicamente la aplicación web toma un archivo CSV con comentarios, los analiza y los clasifica utilizando un modelo previamente entrenado. Luego, muestra los resultados a través de una interfaz web, presentando el archivo subido y un gráfico de pastel que ilustra las categorías en las que se clasifican los comentarios.

## Cómo Utilizar    

1. Carga el archivo .csv con las frases / comentarios.
2. Haz clic en el botón "Cargar y Clasificar".
3. La aplicación procesará los datos y mostrará un pie chart con el % que representan las frases/comentarios según las tres categorias.
4. Haz clic en "Reiniciar" para hacer nuevas clasificaciones. 

## Requisitos del Sistema

- Python en su versión más reciente. 
- Navegador web moderno (Chrome, Edge, Mozilla Firefox, Safari, etc.).

## Uso Local (Opcional)

Si deseas ejecutar la aplicación localmente, puedes seguir estos pasos:

1. Clona este repositorio en tu ordenador.
2. Asegúrate de tener Python instalado y las bibliotecas necesarias.
3. Abre el archivo .ipynb en un entorno Jupyter Notebook.
4. Ejecuta las celdas para cargar y guardar el modelo.
5. Ejecuta el archivo app.py y ve al terminal.
5. Inicia el servidor local y accede a la aplicación a través de tu navegador.

## Notas

- Este proyecto tiene fines informativos y/o educativos. Los resultados de las recomendaciones pueden variar y no deben utilizarse como base única para tomar decisiones importantes.

## Créditos

- Autor: Fabián García Gómez
- Contacto: datasolu7ion@gmail.com

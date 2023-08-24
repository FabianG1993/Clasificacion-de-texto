'''
Este código es la base de una aplicación web que toma un archivo CSV con comentarios, 
los analiza y los clasifica utilizando un modelo previamente entrenado. Luego, muestra 
los resultados a través de una interfaz web, presentando el archivo subido y un gráfico 
de pastel que ilustra las categorías en las que se clasifican los comentarios.
'''
import os
import base64
from io import BytesIO
import pickle
from flask import Flask, render_template, request, redirect
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

'''
La función perform_prediction utiliza la biblioteca pickle para
cargar un modelo de aprendizaje automático y un vectorizador TF-IDF 
desde archivos pickle.
'''
def perform_prediction(data):
    # Cargar el modelo y la matriz de vectores desde archivos pickle
    with open('modelo.pickle', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pickle', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    # Matriz de características TF-IDF  
    matrix_v = vectorizer.transform(data["comment"])
    predicted_values = model.predict(matrix_v)
    data['label'] = predicted_values
    return data
'''
 La función index de Python utiliza la biblioteca Flask para crear
 una aplicación web que permite a los usuarios cargar un archivo CSV y 
 realizar clasificaciones. Además de abrir el interfaz y de generar 
 una grafica informativa. 
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'restart' in request.form:  # Verifica si se presionó el botón de reinicio
            return redirect('/') 
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join('static', 'uploads', file.filename)
            file.save(file_path)
            # Leer el archivo CSV
            my_data = pd.read_csv(file_path)
            # Realizar clasificación
            clasifications = perform_prediction(my_data)
            # Generar el pie chart
            labels = "Positivo", "Negativo", "Neutral"
            sizes = clasifications['label'].value_counts()
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
            # Guardar el gráfico en memoria
            img_stream = BytesIO()
            plt.savefig(img_stream, format='png')
            plt.close()  # Cerrar la figura para liberar recursos
            # Convertir la imagen a base64
            img_base64 = base64.b64encode(img_stream.getvalue()).decode('utf-8')

            return render_template('index.html', file_path=file_path, pie_chart=img_base64)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

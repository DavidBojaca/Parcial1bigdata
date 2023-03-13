import boto3
from datetime import datetime
from bs4 import BeautifulSoup



def f():
    
    # tener el nombre del archivo anterior
    nombre = str(datetime.today().strftime('%Y-%m-%d'))
    s3 = boto3.resource('s3')

    # traer el objeto html del primer bucket
    bucket = s3.Bucket('lecturadatoscasas')
    obj = bucket.Object(str(nombre + ".html"))
    body = obj.get()['Body'].read()
    
    #cambiar el formato para la captura de los datos
    html = BeautifulSoup(body, 'html.parser')
    
    #Establecer etiquetas con información del html
    data_casa = html.find_all('div', class_='listing listing-card')
    data_titulo = html.find_all('div', class_='listing-card__title')
    data_precio = html.find_all('div', class_='price')
    fecha_actual = datetime.today().strftime('%Y-%m-%d')
    
    #text sirve de encabezado de los valores que se van a extraer del html
    text = "FechaDescarga, Info, Valor, NumHabitaciones, NumBanos, mts2\n"
    
    #se itera en for para la extracion en oreden de lso datosd ecada casa presente en el html
    for i in range(len(data_casa)):
        datos = data_casa[i].find_all('div', class_='listing-card__properties')[0]
        text = text + fecha_actual + "," + \
            str(data_titulo[i].text) + "," + \
            str(data_precio[i].text) + "," + \
            str(data_casa[i]['data-rooms']) + "," + \
            str(datos.find_all('span')[1].text[:1]) + "," + \
            str(datos.find_all('span')[2].text) + \
            "\n"
            
    #se suve en formato csv al segundo bucket
    boto3.client('s3').put_object(Body=text,Bucket='capturadatoscasas',
                                  Key=str(nombre+".csv"))

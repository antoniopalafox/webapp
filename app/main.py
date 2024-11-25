
#!/usr/bin/env python

#  Programa: main.py
# Propósito: Creación aplicación web Flask
#     Autor: Óscar García
#     Fecha: 09/12/2019 

import flask
import datetime
import os

# Crear el objeto que representa la aplicacion web
APP = flask.Flask(__name__)
nombre=os.environ['NAME']
contador=0

@APP.route('/hola')
def index():
    """ Muestra la página inicial asociada al recurso `/`
        y que estará contenida en el archivo index.html
    """
    return "Hola Mundo"

@APP.route('/adios')
def index2():
    """ Muestra la página inicial asociada al recurso `/`
        y que estará contenida en el archivo index.html
    """
    return "Adios Mundo"

@APP.route('/')
def index3():
    """ Muestra la página inicial asociada al recurso `/`
        y que estará contenida en el archivo index.html
    """
    global contador
    contador = contador + 1
    return flask.render_template('index.html', contador=contador, nombre=nombre, timestamp=datetime.datetime.now())


if __name__ == '__main__':
    APP.debug = True
    APP.run(host='0.0.0.0', port=os.environ['PORT'])

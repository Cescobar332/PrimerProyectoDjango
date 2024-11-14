from django.http import HttpResponse
import datetime
from django.template import loader
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):

    p1 = Persona("Carlos", "Escobar")

    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora = datetime.datetime.now()

    #doc_externo = loader.get_template('miplantilla.html')

    #documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas})

    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas})

def cursoC(request):

    fecha_actual = datetime.datetime.now()

    return render(request, "CursoC.html", {"dameFecha":fecha_actual})

def cursoCss(request):

    fecha_actual = datetime.datetime.now()

    return render(request, "cursoCss.html", {"dameFecha":fecha_actual})

def despedida(request):
    return HttpResponse("Hasta luego gente de Django")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    periodo = agno - 2024
    edadFutura = edad + periodo
    documento2 = "<html><body><h2>En el año %s tendrás %s años</h2></body></html>" %(agno, edadFutura)

    return HttpResponse(documento2)
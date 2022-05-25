from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
from django.template import Context
from django.template import loader
import datetime
from AppCoder.models import Curso

# Create your views here.
def prueba_curso(self):
    curso = Curso(nombre = "desarrollo web" , camada = 19500)
    curso.save()
    documentodetexto = f"--->Curso: {curso.nombre}, Camada {curso.camada}"
    return HttpResponse(documentodetexto)

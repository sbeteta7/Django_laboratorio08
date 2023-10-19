from django.contrib import admin
from .models import Matricula,Estudiante,Curso,Docente

# Register your models here.
admin.site.register([Estudiante,Curso,Docente,Matricula])
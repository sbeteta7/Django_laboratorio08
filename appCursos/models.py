import datetime
from django.db import models

class Estudiante(models.Model):
    CodEstudiante = models.AutoField(primary_key=True)
    AnioIngreso = models.IntegerField()
    Apellido = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=15)

    
    def __str__(self):
        return f'{self.Apellido}, {self.Nombre}'

class Curso(models.Model):
    CodCurso = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Credito = models.PositiveIntegerField()

    def __str__(self):
        return self.Nombre

class Docente(models.Model):
    CodDocente = models.AutoField(primary_key=True)
    Apellido = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Apellido}, {self.Nombre}'

class Matricula(models.Model):
    matricula_id = models.AutoField(primary_key=True, default=None)
    AnioAcademico = models.IntegerField()
    Ciclo = models.CharField(max_length=10)
    Fecha = models.DateField()
    CodigoEstudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    CodigoCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    CodigoDocente = models.ForeignKey(Docente, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.AnioAcademico} - {self.Ciclo} - {self.CodigoEstudiante} - {self.CodigoCurso} - {self.CodigoDocente}'

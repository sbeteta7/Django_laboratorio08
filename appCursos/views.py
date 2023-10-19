from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404
import logging

logger = logging.getLogger(__name__)


from appCursos.forms import MatriculaForm,MatriculaUpdateForm,MatriculaSearchForm
from .models import Matricula,Estudiante,Curso,Docente
# Create your views here.


def listMatricula(request):
    formSearch = MatriculaSearchForm(request.GET)
    matriculas= Matricula.objects.all()
    estudiantes = Estudiante.objects.all()
    cursos = Curso.objects.all()
    docentes = Docente.objects.all()
    formCreateMatricula = MatriculaForm()

    if formSearch.is_valid():
        matricula_id = formSearch.cleaned_data.get('matricula_id')
        if matricula_id:
            matriculas = matriculas.filter(matricula_id=matricula_id)
        AnioAcademico = formSearch.cleaned_data.get('AnioAcademico')
        if AnioAcademico:
            matriculas = matriculas.filter(AnioAcademico=AnioAcademico)

        Ciclo = formSearch.cleaned_data.get('Ciclo')
        if Ciclo:
            matriculas = matriculas.filter(Ciclo=Ciclo)

        CodigoEstudiante = formSearch.cleaned_data.get('CodigoEstudiante')
        if CodigoEstudiante:
            matriculas = matriculas.filter(CodigoEstudiante=CodigoEstudiante)

        CodigoCurso = formSearch.cleaned_data.get('CodigoCurso')
        if CodigoCurso:
            matriculas = matriculas.filter(CodigoCurso=CodigoCurso)

        CodigoDocente = formSearch.cleaned_data.get('CodigoDocente')
        if CodigoDocente:
            matriculas = matriculas.filter(CodigoDocente=CodigoDocente)

    context = {
        'matriculas':matriculas,
        'estudiantes': estudiantes,
        'cursos': cursos,
        'docentes': docentes,
        'formCreateMatricula':formCreateMatricula,
        
        'formSearch':formSearch
    }
    return render(request,'matricula.html',context)


def createMatricula(request):
    if request.method == "POST":
        formCreateMatricula = MatriculaForm(request.POST)
        if formCreateMatricula.is_valid():
            newMatricula=formCreateMatricula.save()
    
            newMatricula.save()

        return redirect('appCursos:matricula')
    else:
        return redirect('appCursos:matricula')
    
def deleteMatricula(request):
    if request.method == "POST":
        try:    
            id = request.POST.get('matricula_id')
            matricula = Matricula.objects.get(matricula_id=id)
            matricula.delete()
            messages.success(request, 'Matricula eliminado correctamente')
        except ObjectDoesNotExist:   
            messages.error(request, 'Matricula no encontrado')
        except Exception as e:
            logger.error(f'Error al eliminar la matrícula: {e}')
            messages.error(request, 'Error al eliminar el alumno')
        
        return redirect('appCursos:matricula')
    else:
        return redirect('appCursos:matricula')
    

def updateMatricula(request, matricula_id):
    matricula = get_object_or_404(Matricula, pk=matricula_id)

    if request.method == "POST":
        form = MatriculaUpdateForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            # Puedes agregar un mensaje de éxito si lo deseas
            return redirect('appCursos:matricula')
    else:
        form = MatriculaUpdateForm(instance=matricula)

    return render(request, 'matricula.html', {'form': form, 'matricula': matricula})
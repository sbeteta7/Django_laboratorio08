from .models import Matricula, Estudiante, Curso, Docente
from django import forms


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date'}),
            'CodigoEstudiante': forms.Select(attrs={'class': 'form-control'}),
            'CodigoCurso': forms.Select(attrs={'class': 'form-control'}),
            'CodigoDocente': forms.Select(attrs={'class': 'form-control'}),
        }

class MatriculaUpdateForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date'}),
            'CodigoEstudiante': forms.Select(attrs={'class': 'form-control'}),
            'CodigoCurso': forms.Select(attrs={'class': 'form-control'}),
            'CodigoDocente': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(MatriculaUpdateForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['AnioAcademico'].initial = instance.AnioAcademico
            self.fields['Ciclo'].initial = instance.Ciclo
            self.fields['Fecha'].initial = instance.Fecha
            self.fields['CodigoEstudiante'].initial = instance.CodigoEstudiante
            self.fields['CodigoCurso'].initial = instance.CodigoCurso
            self.fields['CodigoDocente'].initial = instance.CodigoDocente



class MatriculaSearchForm(forms.Form):
    CAMPO_CHOICES = [
        ('matricula_id', 'Código de Matrícula'),
        ('AnioAcademico', 'Año Académico'),
        ('Ciclo', 'Ciclo'),
        ('CodigoEstudiante', 'Estudiante'),
        ('CodigoCurso', 'Curso'),
        ('CodigoDocente', 'Docente'),
    ]

    campo = forms.ChoiceField(
        choices=CAMPO_CHOICES,
        required=True,
        widget=forms.RadioSelect,
        
    )
    valor = forms.CharField(required=False, label='Valor de Búsqueda', widget=forms.TextInput(attrs={'class': 'form-control'}))

    matricula_id = forms.IntegerField(
        required=False,
        label='Código de Matrícula',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    AnioAcademico = forms.IntegerField(
        required=False,
        label='Año Académico',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    Ciclo = forms.CharField(
        max_length=10,
        required=False,
        label='Ciclo',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    CodigoEstudiante = forms.ModelChoiceField(
        queryset=Estudiante.objects.all(),
        required=False,
        label='Código del Estudiante',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    CodigoCurso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        required=False,
        label='Código del Curso',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    CodigoDocente = forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        required=False,
        label='Código del Docente',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )


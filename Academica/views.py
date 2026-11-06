from django.shortcuts import render
from Academica.models import Faculty, Department

# Create your views here.

def listaFacultades(request):
    facultades = Faculty.objects.all()
    return render(request, 'general/faculty_list.html',
                 {'facultades': facultades})

def listaDepartamentos(request):
    departamentos = Department.objects.select_related('faculty')
    return render(request, 'departamentos/department_list.html',
                     {'departamentos': departamentos })

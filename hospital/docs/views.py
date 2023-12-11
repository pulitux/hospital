from django.shortcuts import render
from docs.models import Doctor


def index(request):
    doctor = Doctor()
    if len(request.POST['hospitales']):
        hospitales = ','.join(h for h in request.POST['hospitales'])
        cursor = doctor.por_hospital(request)
    else:
        hospitales = ''
    contexto = {
        'lista_doctores':cursor,
        'hospitales':hospitales
    }
    return render(request, 'index.html', contexto)
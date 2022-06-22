

from django.http import HttpResponse
from datetime import datetime

from django.template import Context, Template, loader

from primermvt.models import Abuelo, Hermano, Madre

def inicio(request):
    return HttpResponse ('Bienvenidos a la Base de Datos')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha : {fecha_actual}')

def mi_template(request):
    
    template1 = loader.get_template('mvt.html')
    
    abuelo= Abuelo(nombre='Angel Pintor', edad=83)
    abuelo.save()
    
    madre= Madre(nombre='Marisa Pintor', edad=53)
    madre.save()
    
    hermano= Hermano(nombre='Emmanuel Cruz Pintor', edad=24)
    hermano.save()
    
    render1 = template1.render(
        {'abuelo':abuelo, 'madre':madre, 'hermano':hermano})
    
    return HttpResponse (render1)
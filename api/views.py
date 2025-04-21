from django.shortcuts import render

# views.py
from django.shortcuts import render
from .redis_client import agregar_lugar, lugares_cercanos, distancia
from scripts.precargar import precargar

def home(request):
    if request.method == 'POST':
        grupo = request.POST['grupo']
        nombre = request.POST['nombre']
        lat = float(request.POST['lat'])
        lon = float(request.POST['lon'])
        agregar_lugar(grupo, nombre, lat, lon)
    return render(request, 'home.html')

def buscar_cercanos(request):
    lugares = []
    if request.method == 'POST':
        grupo = request.POST['grupo']
        lat = float(request.POST['lat'])
        lon = float(request.POST['lon'])
        lugares = lugares_cercanos(grupo, lat, lon)
    return render(request, 'cercanos.html', {'lugares': lugares})

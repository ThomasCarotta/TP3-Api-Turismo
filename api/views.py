from django.shortcuts import render, redirect
from django.contrib import messages
from .redis_client import agregar_lugar, lugares_cercanos, GRUPOS, redis_client

def index(request):
    lugares = []
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    
    if lat and lon:
        try:
            lat = float(lat)
            lon = float(lon)
            for tipo in GRUPOS.keys():
                cercanos = lugares_cercanos(tipo, lat, lon, radio_km=5)
                for lugar in cercanos:
                    lugares.append({
                        'nombre': lugar[0],
                        'tipo': tipo,
                        'distancia': round(float(lugar[1]), 2),
                        'mostrar_distancia': True
                    })
        except (ValueError, TypeError):
            messages.error(request, 'Las coordenadas deben ser números válidos')
    else:
        for tipo, key in GRUPOS.items():
            lugares_grupo = redis_client.zrange(key, 0, -1)
            for nombre in lugares_grupo:
                lugares.append({
                    'nombre': nombre,
                    'tipo': tipo,
                    'distancia': None,
                    'mostrar_distancia': False
                })
    
    lugares.sort(key=lambda x: (x['tipo'], x['nombre']))
    
    return render(request, 'api/index.html', {
        'lugares': lugares,
        'coordenadas_ingresadas': bool(lat and lon)
    })

def agregar_lugar_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        
        if nombre and tipo and lat and lon:
            try:
                lat = float(lat)
                lon = float(lon)
                resultado = agregar_lugar(tipo, nombre, lat, lon)
                if resultado == 1:
                    messages.success(request, f'"{nombre}" fue agregado exitosamente como {tipo}')
                else:
                    messages.warning(request, f'"{nombre}" ya existe en {tipo}')
                return redirect('index')
            except ValueError as e:
                messages.error(request, str(e))
            except (TypeError, ValueError):
                messages.error(request, 'Las coordenadas deben ser números válidos')
    
    tipos = [
        ('cervecerias', 'Cervecería'),
        ('universidades', 'Universidad'),
        ('farmacias', 'Farmacia'),
        ('emergencias', 'Emergencia'),
        ('supermercados', 'Supermercado')
    ]
    
    return render(request, 'api/agregar_lugar.html', {'tipos': tipos})
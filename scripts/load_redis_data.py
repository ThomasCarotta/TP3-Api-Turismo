from api.redis_client import redis_client, GRUPOS, agregar_lugar
import json

# Datos iniciales de lugares
lugares_iniciales = [
    {'grupo': 'cervecerias', 'nombre': 'Träctor', 'lat': -41.1335, 'lon': -71.3103},
    {'grupo': 'cervecerias', 'nombre': 'Drakkar', 'lat': -41.1339, 'lon': -71.3105},
    {'grupo': 'universidades', 'nombre': 'UADER', 'lat': -41.1320, 'lon': -71.3090},
    {'grupo': 'universidades', 'nombre': 'UTN', 'lat': -41.1345, 'lon': -71.3087},
    {'grupo': 'farmacias', 'nombre': 'Farmacia Alberdi', 'lat': -41.1351, 'lon': -71.3072},
    {'grupo': 'farmacias', 'nombre': 'Farmacia del Pueblo', 'lat': -41.1351, 'lon': -71.3072},
    {'grupo': 'emergencias', 'nombre': 'Hospital JJ Urquiza', 'lat': -41.1281, 'lon': -71.2659},
    {'grupo': 'supermercados', 'nombre': 'Gran Rex', 'lat': -41.1344, 'lon': -71.3085}
]

def cargar_datos_iniciales():
    # Verificar si ya hay datos en Redis
    for grupo in GRUPOS.values():
        if redis_client.exists(grupo) and redis_client.zcard(grupo) > 0:
            print(f"El grupo {grupo} ya tiene datos. No se cargarán nuevamente.")
            return False

    # Cargar datos si no existen
    print("Cargando datos iniciales en Redis...")
    for lugar in lugares_iniciales:
        try:
            agregar_lugar(lugar['grupo'], lugar['nombre'], lugar['lat'], lugar['lon'])
            print(f"✓ Añadido: {lugar['nombre']} ({lugar['grupo']})")
        except Exception as e:
            print(f"✗ Error al añadir {lugar['nombre']}: {str(e)}")
    
    print("Carga de datos completada!")
    return True

if __name__ == "__main__":
    cargar_datos_iniciales()
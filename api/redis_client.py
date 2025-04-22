import redis
import os

# Configuración de la conexión Redis
redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=6379,
    decode_responses=True
)

# Definición de grupos
GRUPOS = {
    'cervecerias': 'grupo:cervecerias',
    'universidades': 'grupo:universidades',
    'farmacias': 'grupo:farmacias',
    'emergencias': 'grupo:emergencias',
    'supermercados': 'grupo:supermercados'
}

def agregar_lugar(grupo, nombre, lat, lon):
    """Agrega un lugar a un grupo específico en Redis"""
    if grupo not in GRUPOS:
        raise ValueError(f"Grupo no válido: {grupo}")
    
    key = GRUPOS[grupo]
    # Verificar si el lugar ya existe
    if redis_client.zscore(key, nombre) is None:
        return redis_client.geoadd(key, (lon, lat, nombre))
    return 0  # Retorna 0 si el lugar ya existía

def lugares_cercanos(grupo, lat, lon, radio_km=5):
    """Busca lugares cercanos a unas coordenadas dadas"""
    if grupo not in GRUPOS:
        raise ValueError(f"Grupo no válido: {grupo}")
    
    key = GRUPOS[grupo]
    return redis_client.geosearch(
        name=key,
        longitude=lon,
        latitude=lat,
        radius=radio_km,
        unit='km',
        withdist=True
    )

def distancia(grupo, nombre, lat, lon):
    """Calcula la distancia entre un lugar y unas coordenadas"""
    if grupo not in GRUPOS:
        raise ValueError(f"Grupo no válido: {grupo}")
    
    key = GRUPOS[grupo]
    return redis_client.geodist(key, nombre, (lon, lat), unit='km')
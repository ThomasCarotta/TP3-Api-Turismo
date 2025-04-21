import redis

r = redis.Redis(host='redis', port=6379, decode_responses=True)

GRUPOS = {
    'cervecerias': 'grupo:cervecerias',
    'universidades': 'grupo:universidades',
    'farmacias': 'grupo:farmacias',
    'emergencias': 'grupo:emergencias',
    'supermercados': 'grupo:supermercados'
}

def agregar_lugar(grupo, nombre, lat, lon):
    key = GRUPOS[grupo]
    r.geoadd(key, (lon, lat, nombre))

def lugares_cercanos(grupo, lat, lon, radio_km=5):
    key = GRUPOS[grupo]
    return r.georadius(key, lon, lat, radio_km, unit='km', withdist=True)

def distancia(grupo, nombre, lat, lon):
    key = GRUPOS[grupo]
    return r.geodist(key, nombre, (lon, lat), unit='km')

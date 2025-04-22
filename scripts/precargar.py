from api.redis_client import agregar_lugar

def precargar():
    agregar_lugar('cervecerias', 'Träctor', -41.1335, -71.3103)
    agregar_lugar('cervecerias', 'Drakkar', -41.1339, -71.3105)
    agregar_lugar('universidades', 'UADER', -41.1320, -71.3090)
    agregar_lugar('universidades', 'UTN', -41.1345, -71.3087)
    agregar_lugar('farmacias', 'Farmacia Alberdi', -41.1351, -71.3072)
    agregar_lugar('farmacias', 'Farmacia del Pueblo', -41.1351, -71.3072)
    agregar_lugar('emergencias', 'Hospital JJ Urquiza', -41.1281, -71.2659)
    agregar_lugar('supermercados', 'Gran Rex', -41.1344, -71.3085)

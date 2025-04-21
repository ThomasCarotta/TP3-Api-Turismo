from api.redis_client import agregar_lugar

def precargar():
    agregar_lugar('cervecerias', 'Träctor', -41.1335, -71.3103)
    agregar_lugar('cervecerias', 'Drakkar', -41.1339, -71.3105)
    agregar_lugar('universidades', 'UADER', -41.1320, -71.3090)
    agregar_lugar('universidades', 'UTN', -41.1345, -71.3087)
    agregar_lugar('farmacias', 'Farmacia Alberdi', -41.1551, -61.3072)
    agregar_lugar('farmacias', 'Farmacia del pueblo', -51.1351, -21.3072)
    agregar_lugar('emergencias', 'Hospital Justo Jose de Urquiza', -43.1281, -62.2659)
    agregar_lugar('supermercados', 'Supermercado Gran Rex', -52.1354, -64.3242)
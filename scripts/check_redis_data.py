from api.redis_client import redis_client, GRUPOS
import sys

def verificar_datos():
    """Verifica si hay datos en Redis"""
    for grupo in GRUPOS.values():
        if redis_client.exists(grupo) and redis_client.zcard(grupo) > 0:
            print(f"Datos encontrados en {grupo}")
            return True
    
    print("No se encontraron datos en Redis")
    return False

if __name__ == "__main__":
    if verificar_datos():
        sys.exit(0)  # Código de éxito (hay datos)
    else:
        sys.exit(1)  # Código de fallo (no hay datos)
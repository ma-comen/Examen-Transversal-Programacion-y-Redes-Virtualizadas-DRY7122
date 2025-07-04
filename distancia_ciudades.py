from geopy.distance import geodesic
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="viajes_app")

def obtener_coordenadas(ciudad):
    location = geolocator.geocode(ciudad)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

while True:
    print("\n--- Calculadora de distancia entre ciudades ---")
    origen = input("Ingrese ciudad de origen (o 's' para salir): ")
    if origen.lower() == 's':
        print("Programa finalizado.")
        break

    destino = input("Ingrese ciudad de destino (o 's' para salir): ")
    if destino.lower() == 's':
        print("Programa finalizado.")
        break

    transporte = input("Medio de transporte (auto, avión, caminando, etc.): ")

    coord_origen = obtener_coordenadas(origen)
    coord_destino = obtener_coordenadas(destino)

    if not coord_origen or not coord_destino:
        print("No se pudieron obtener las coordenadas de alguna ciudad.")
        continue

    distancia_km = geodesic(coord_origen, coord_destino).kilometers
    distancia_millas = geodesic(coord_origen, coord_destino).miles

    # Estimación de duración según transporte (puedes ajustar los promedios)
    if transporte.lower() == "auto":
        duracion_horas = distancia_km / 80  # 80 km/h promedio
    elif transporte.lower() == "avión":
        duracion_horas = distancia_km / 800  # 800 km/h promedio
    elif transporte.lower() == "caminando":
        duracion_horas = distancia_km / 5  # 5 km/h promedio
    else:
        duracion_horas = distancia_km / 60  # promedio general

    print(f"\nDesde {origen.title()} hasta {destino.title()}:")
    print(f"Distancia: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
    print(f"Duración estimada en {transporte}: {duracion_horas:.2f} horas")
    print(f"Narrativa: El viaje desde {origen.title()} hasta {destino.title()} en {transporte} cubre aproximadamente {distancia_km:.2f} kilómetros.")
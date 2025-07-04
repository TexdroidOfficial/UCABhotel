from enum import Enum
import pickle

class categoria_habitacion(Enum):
    SENCILLA = "mono"
    DOBLE = "duo"
    SUITE = "deluxe"
    PRESIDENCIAL = "royal"
    
class status_habitacion(Enum):
    OCUPADA = "locked"
    LIBRE = "free"
    RESERVADA = "saved"
    INVALIDO = "error"

matriz_habitaciones = [
    [201, categoria_habitacion.SUITE.value, status_habitacion.LIBRE.value, "", "", "", ""],
    [202, categoria_habitacion.SUITE.value, status_habitacion.LIBRE.value, "", "", "", ""],
    [203, categoria_habitacion.SUITE.value, status_habitacion.OCUPADA.value, "20250127", "20250128", "V-12345678", "Ana Ramirez"],
    [204, categoria_habitacion.SUITE.value, status_habitacion.OCUPADA.value, "20250221", "20250302", "V-18901234", "Luis Rodriguez"],
    [205, categoria_habitacion.SUITE.value, status_habitacion.RESERVADA.value, "20250314", "20250316", "V-20123456", "Maria Perez"],
    [211, categoria_habitacion.DOBLE.value, status_habitacion.LIBRE.value, "", "", "", ""],
    [212, categoria_habitacion.DOBLE.value, status_habitacion.LIBRE.value, "", "", "", ""],
    [213, categoria_habitacion.DOBLE.value, status_habitacion.OCUPADA.value, "20250423", "20250430", "V-12345678", "Pedro Martinez"],
    [214, categoria_habitacion.DOBLE.value, status_habitacion.OCUPADA.value, "20250501", "20250511", "V-17654321", "Carla Soto"],
    [215, categoria_habitacion.DOBLE.value, status_habitacion.RESERVADA.value, "20250512", "20250523", "V-21987654", "Diego Torres"],
    [221, categoria_habitacion.SENCILLA.value, status_habitacion.LIBRE.value, "", "", "", ""],  
    [222, categoria_habitacion.SENCILLA.value, status_habitacion.LIBRE.value, "", "", "", ""],  
    [223, categoria_habitacion.SENCILLA.value, status_habitacion.OCUPADA.value, "20250601", "20250602", "V-13456789", "Elena Gomez"],
    [224, categoria_habitacion.SENCILLA.value, status_habitacion.OCUPADA.value, "20250607", "20250611", "V-19876543", "Francisco Diaz"],  
    [225, categoria_habitacion.SENCILLA.value, status_habitacion.RESERVADA.value, "20250622", "20250630", "V-22345678", "Freddy Vega"],
    [231, categoria_habitacion.PRESIDENCIAL.value, status_habitacion.LIBRE.value, "", "", "", ""],
    [232, categoria_habitacion.PRESIDENCIAL.value, status_habitacion.LIBRE.value, "", "", "", ""],
    [233, categoria_habitacion.PRESIDENCIAL.value, status_habitacion.OCUPADA.value, "20250727", "20250729", "V-14567890", "Humberto Rojas"],
    [234, categoria_habitacion.PRESIDENCIAL.value, status_habitacion.OCUPADA.value, "20250807", "20250809", "V-16789012", "Isabel Castro"],
    [235, categoria_habitacion.PRESIDENCIAL.value, status_habitacion.RESERVADA.value, "20250811", "20250813", "V-23456789", "Javier Vargas"]
]
    
with open ("hotelData.bin", "wb") as file:
    pickle.dump(matriz_habitaciones, file)
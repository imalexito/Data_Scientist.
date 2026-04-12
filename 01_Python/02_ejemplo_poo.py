"""
class ArchivoCSV:
    def __init__(self,ruta,separador):
        self.ruta = ruta
        self.separador = separador
        self.esta_abierto = False

    def abrir(self):
        self.esta_abierto = True
        print(f"Abrinedo archivo en {self.ruta} con separador {self.separador}")



mi_data = ArchivoCSV("datos.csv", ",")
print(mi_data.ruta)
mi_data.abrir()
"""

class SensorTemperatura:
    def __init__(self,ubicacion):
        self.ubucacion = ubicacion
        self.lectura_actual = 25.0 #vlaor por defecto

    #'self' es obligatorio, 'limite ' es el parameto extra que u elegiste
    def es_alesrta(self,limite):
        if self.lectura_actual > limite:
            return True
        else:
            return False

#uso 
mi_sensor = SensorTemperatura("almacen")
#aqui le pasamos el 30.00 al parameto "limite"
print(mi_sensor.es_alesrta(30.00))
print(mi_sensor.es_alesrta(20.00))


class SensorTemperatura:
    def __init__(self,ubicacion):
        self.ubiacion = ubicacion
        self.lecturas = []

    def agregar_lecturas(self, valor):
        self.lecturas.append(float(valor))

    def ver_promedio(self,unidad):
        promedio = sum(self.lecturas) / len(self.lecturas)
        if unidad.upper() == "F":
            promedio = (promedio * 1.8) + 32
            return promedio
        elif unidad.upper() == "C":
            return promedio
        else:
            return "Unidad no reconocida"


sendor_servidores = SensorTemperatura("Data Center Norte")
sendor_servidores.agregar_lecturas(22.5)
sendor_servidores.agregar_lecturas("23.8")
sendor_servidores.agregar_lecturas(25)
sendor_servidores.agregar_lecturas("21.2")
sendor_servidores.agregar_lecturas(24.5)
print(sendor_servidores.ver_promedio("C"))
print(sendor_servidores.ver_promedio("f"))


    

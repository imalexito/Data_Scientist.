ventas = [100, 250, 300, 50, 400]
total_ventas = sum(ventas)
print(f"Total de ventas: {total_ventas}")


cleinte = {"nombre": "juan",
           "edad": 23,
            "gasto_total":400}


if cleinte["gasto_total"] > 200:
    print("cleinteVIP")
else:
    print("Cleinte regular")



ventas_mes = [120,450,80,600,210,90,500]

ventas_altas = []

for ventas in ventas_mes:
	if ventas > 300:
		ventas_altas.append(ventas)
print(f"ventas_altas: {ventas_altas}") 

#Karen Cabrera 28-02-2024

import math

p= float (input("Ingrese el precio de  suscripción: "))
u= float (input("Ingrese el número de  usuarios: "))
gt= float (input("Ingrese los gastos totales: "))
utilidades_ano_anterior= float (input("Ingrese las utilidades del año anterior: "))
razon_utilidades=(((p*u)-gt)/utilidades_ano_anterior)
decimal=round(razon_utilidades,2)

utilidades = print(f"la razón de las utilidades de este periodo y el año anterior es: {decimal}" )
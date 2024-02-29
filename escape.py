#Karen Cabrera 28-02-2024
import math

gravitacional_constante = float (input("Ingrese la constante gravitacional: "))
radio_planeta = float (input ("Ingrese el radio en Kilómetros: "))

velocidad_escape = math.sqrt(2 * gravitacional_constante * radio_planeta*1000)

print(f"La velocidad de Escape es: {velocidad_escape:1f} [m/s]")
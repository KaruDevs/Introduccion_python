#Karen Cabrera 28-02-2024

p= float (input("Ingrese el precio de  suscripción: "))
unormal= float (input("Ingrese el número de  usuarios: "))
upremium= float (input("Ingrese el número de  usuarios premium: "))
gt= float (input("Ingrese los gastos totales: "))
total_normal=p*unormal
precio_premium=(p*1.5)
total_premium=precio_premium*upremium
utilidades = print(f"las utilidades son: {total_normal+total_premium-gt}" )
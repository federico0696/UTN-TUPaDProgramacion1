# Calculadora de propinas en un restaurante

# 1. Pedir al usuario el monto total de la cuenta
monto = float(input("Ingrese el monto de la cuenta: "))

# 2. Calcular la propina sugerida al 10%
propina_10 = monto * 0.10
total_10 = monto + propina_10

# 3. Calcular la propina sugerida al 15%
propina_15 = monto * 0.15
total_15 = monto + propina_15

# 4. Mostrar resultados en pantalla
print(f"\nPropina sugerida (10%): {propina_10}")
print(f"Total a pagar (10%): {total_10}")
print(f"Propina sugerida (15%): {propina_15}")
print(f"Total a pagar (15%): {total_15}")

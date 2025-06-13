def verificar_valor(valor):
    if valor is None:
     print("El valor no está asignado (es None).")
    else:
     print(f"El valor es: {valor}")

# Prueba con None
verificar_valor(None)

# Prueba con otro valor
verificar_valor(10)
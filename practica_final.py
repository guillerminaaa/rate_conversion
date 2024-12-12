# Solicitar al usuario que seleccione la conversion que realizara (pesos mexicanos -->usd o euros)


eur_to_mxn_rate = 23.70
usd_to_mxn_rate = 20.75

# 2. Ingrese el monto que quiere convertir
coin_type = input(
    "Por favor ingrese a que moneda convetira el monto ingresado (EUR/USD): ")
coin_type = coin_type.upper()

# 3. Realizar la conversion al peso selccionado
amount_to_covert = float(input("Ingrese el monto a convertir: "))

# 4. mostrar el resultado de la conversion al usuario
if coin_type == "EUR":
    result = amount_to_covert * eur_to_mxn_rate
    print("El resultado de la conversion de EUR a MXN es: ", result)
elif coin_type == "USD":
    result = amount_to_covert * usd_to_mxn_rate 
    print("El resultado de la conversion de USD a MXN es : ", result)
else:
    print("No esta disonible este tipo de conversion actualmente")

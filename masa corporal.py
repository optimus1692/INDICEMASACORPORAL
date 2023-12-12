def calcular_imc(peso, altura):
    # Fórmula del IMC: peso / (altura ** 2)
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Pedir al usuario que ingrese información personal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
segundo_apellido = input("Ingrese su segundo apellido: ")
edad = int(input("Ingrese su edad: "))

# Pedir al usuario que ingrese peso y altura
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
mi_imc = calcular_imc(peso, altura)

# Clasificar el IMC
clasificacion = clasificar_imc(mi_imc)

# Mostrar resultados
print(f"\nInformación personal:")
print(f"Nombre: {nombre}")
print(f"Apellido: {apellido}")
print(f"Segundo Apellido: {segundo_apellido}")
print(f"Edad: {edad} años")

print(f"\nSu IMC es: {mi_imc:.2f}")
print(f"Clasificación: {clasificacion}")
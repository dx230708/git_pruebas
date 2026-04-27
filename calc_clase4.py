def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return num1 / num2

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor ingresá un número.")

def calcular(num1, num2, operacion):
    operaciones = {
        '+': sumar,
        '-': restar,
        '*': multiplicar,
        '/': dividir
    }
    if operacion not in operaciones:
        raise ValueError(f"Operación '{operacion}' no reconocida. Usá +, -, * o /.")
    return operaciones[operacion](num1, num2)

def main():
    num1 = obtener_numero("Introduce el primer número: ")
    num2 = obtener_numero("Introduce el segundo número: ")
    operacion = input("Introduce la operación (+, -, *, /): ")

    try:
        resultado = calcular(num1, num2, operacion)
        print(f"El resultado es: {resultado}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

# ESTO ES LO IMPORTANTE:
if __name__ == "__main__":

    main()  # <--- Esta línea DEBE tener sangría (4 espacios)
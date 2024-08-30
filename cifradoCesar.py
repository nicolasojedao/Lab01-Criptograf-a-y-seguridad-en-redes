import sys

def cifrado_cesar(texto, desplazamiento):
    resultado = []

    for char in texto:
        if char.islower():  # Si el carácter es una letra minúscula
            # Realiza el desplazamiento dentro del rango 'a-z'
            resultado.append(chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a')))
        elif char.isupper():  # Si el carácter es una letra mayúscula
            # Realiza el desplazamiento dentro del rango 'A-Z'
            resultado.append(chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A')))
        elif char.isdigit():  # Si el carácter es un número
            # Realiza el desplazamiento dentro del rango '0-9'
            resultado.append(chr((ord(char) - ord('0') + desplazamiento) % 10 + ord('0')))
        else:
            # Si no es una letra ni un número, se deja intacto (espacios, puntuación, etc.)
            resultado.append(char)
    
    return ''.join(resultado)

def main():
    # Obtener argumentos desde la línea de comandos
    if len(sys.argv) != 3:
        print("Uso: python3 cifrado_cesar.py '<oracion>' <desplazamiento>")
        sys.exit(1)
    
    texto = sys.argv[1]
    try:
        desplazamiento = int(sys.argv[2])
    except ValueError:
        print("El desplazamiento debe ser un número entero.")
        sys.exit(1)

    # Llamar a la función de cifrado y mostrar el resultado
    resultado = cifrado_cesar(texto, desplazamiento)
    print(resultado)

if __name__ == "__main__":
    main()

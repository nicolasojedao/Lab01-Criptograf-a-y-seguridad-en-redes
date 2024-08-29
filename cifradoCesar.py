import sys

def cifrado_cesar(texto, desplazamiento):
    resultado = []

    for caracter in texto:
        if caracter.islower():  
            
            indice = ord(caracter) - ord('a')
            
            nuevo_indice = (indice + desplazamiento) % 26
        
            nuevo_caracter = chr(nuevo_indice + ord('a'))
            resultado.append(nuevo_caracter)

        elif caracter.isupper():  
            
            indice = ord(caracter) - ord('A')
            
            nuevo_indice = (indice + desplazamiento) % 26
            
            nuevo_caracter = chr(nuevo_indice + ord('A'))
            resultado.append(nuevo_caracter)

        elif caracter.isdigit():  
            
            indice = ord(caracter) - ord('0')
            
            nuevo_indice = (indice + desplazamiento) % 10
            
            nuevo_caracter = chr(nuevo_indice + ord('0'))
            resultado.append(nuevo_caracter)
        elif caracter == " ":
            resultado.append(caracter)

    return ''.join(resultado)




if len(sys.argv) < 3:
    print("Uso: python3 script.py <input_string> <input_int>")
    sys.exit(1)
    
input_string = sys.argv[1]
input_entero = int(sys.argv[2])

texto_cifrado = cifrado_cesar(input_string, input_entero)
print("Texto original:", input_string)
print("Texto cifrado:", texto_cifrado)
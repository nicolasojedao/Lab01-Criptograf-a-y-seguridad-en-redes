from scapy.all import *
import sys

def extraer_ultimo_caracter_icmp(pcap_file):
    """
    Extrae el último carácter de la carga útil de cada paquete ICMP Echo Request en un archivo .pcapng.
    """
    caracteres = []
    # Cargar los paquetes del archivo .pcapng
    paquetes = rdpcap(pcap_file)

    # Filtrar solo los paquetes ICMP Echo Request
    for paquete in paquetes:
        if ICMP in paquete and paquete[ICMP].type == 8:  # Type 8 es Echo Request
            # Obtener la carga útil (data) del paquete ICMP
            data = bytes(paquete[Raw].load) if Raw in paquete else None
            if data:
                # Agregar el último carácter de la carga útil a la lista
                caracteres.append(chr(data[0]))

    return ''.join(caracteres)

def descifrado_cesar(texto, desplazamiento):
    """
    Aplica un descifrado César a un texto con un desplazamiento dado, manejando mayúsculas, minúsculas y números.
    """
    resultado = []
    
    for char in texto:
        if char.islower():  # Manejar letras minúsculas
            resultado.append(chr((ord(char) - ord('a') - desplazamiento) % 26 + ord('a')))
        elif char.isupper():  # Manejar letras mayúsculas
            resultado.append(chr((ord(char) - ord('A') - desplazamiento) % 26 + ord('A')))
        elif char.isdigit():  # Manejar números
            resultado.append(chr((ord(char) - ord('0') - desplazamiento) % 10 + ord('0')))
        else:
            resultado.append(char)  # Dejar los espacios y otros caracteres intactos

    return ''.join(resultado)

def main(pcap_file):
    # Extraer los caracteres de los paquetes ICMP
    oracion_cifrada = extraer_ultimo_caracter_icmp(pcap_file)
    print(f"Oración cifrada extraída: {oracion_cifrada}")

    # Aplicar y mostrar el descifrado César para desplazamientos del 1 al 25
    print("\nDescifrados posibles (1-25):")
    for desplazamiento in range(1, 26):
        texto_descifrado = descifrado_cesar(oracion_cifrada, desplazamiento)
        print(f"Desplazamiento {desplazamiento}: {texto_descifrado}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 script.py <archivo.pcapng>")
        sys.exit(1)
    
    # Leer el nombre del archivo .pcapng de la consola
    archivo_pcap = sys.argv[1]
    main(archivo_pcap)

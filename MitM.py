from scapy.all import *
import sys

def extraer_primer_caracter_icmp(pcap_file):
    caracteres = []
    paquetes = rdpcap(pcap_file)
    for paquete in paquetes:
        if ICMP in paquete and paquete[ICMP].type == 8 and len(paquete) == 92:
            data = bytes(paquete[Raw].load) if Raw in paquete else None
            if data:
                caracteres.append(chr(data[0]))
    return ''.join(caracteres)

def descifrado_cesar(texto, desplazamiento):
    resultado = []
    for char in texto:
        if char.islower():
            resultado.append(chr((ord(char) - ord('a') - desplazamiento) % 26 + ord('a')))
        elif char.isupper():
            resultado.append(chr((ord(char) - ord('A') - desplazamiento) % 26 + ord('A')))
        elif char.isdigit():
            resultado.append(chr((ord(char) - ord('0') - desplazamiento) % 10 + ord('0')))
        else:
            resultado.append(char)
    return ''.join(resultado)

def main(pcap_file):
    oracion_cifrada = extraer_primer_caracter_icmp(pcap_file)
    print(f"Oración cifrada extraída: {oracion_cifrada}")
    print("\nDescifrados posibles (1-25):")
    for desplazamiento in range(1, 26):
        texto_descifrado = descifrado_cesar(oracion_cifrada, desplazamiento)
        print(f"Desplazamiento {desplazamiento}: {texto_descifrado}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 script.py <archivo.pcapng>")
        sys.exit(1)
    archivo_pcap = sys.argv[1]
    main(archivo_pcap)

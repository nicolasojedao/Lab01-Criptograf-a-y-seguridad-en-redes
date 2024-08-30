import sys
import os
import time
from scapy.all import IP, ICMP, send, Raw

def enviar_ping_real(destino):
    print("Enviando 4 pings reales a 8.8.8.8...")
    os.system(f"ping -c 4 -s 64 {destino}")

def enviar_paquete_icmp(destino, id, seq, ttl, carga):
    relleno_ping_ubuntu = bytes.fromhex(
        '10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f'
        '20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f'
        '30 31 32 33 34 35 36 37 38 39 3a 3b 3c 3d 3e 3f'
    )
    datos = carga.encode() + relleno_ping_ubuntu[len(carga):]
    paquete = IP(dst=destino, ttl=ttl) / ICMP(id=id, seq=seq) / Raw(load=datos)
    send(paquete, verbose=False)

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 programa.py '<oracion>'")
        sys.exit(1)
    
    oracion = sys.argv[1]
    destino = "8.8.8.8"
    id = 1
    ttl = 64

    enviar_ping_real(destino)

    print("Enviando paquetes ICMP con caracteres de la oración ingresada...")
    for seq, char in enumerate(oracion, start=1):
        print(".")
        enviar_paquete_icmp(destino, id, seq, ttl, char)
        time.sleep(1)
        print(f"Sent 1 packets with seq={seq}.")

    enviar_ping_real(destino)

if __name__ == "__main__":
    main()

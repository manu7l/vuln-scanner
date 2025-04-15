#!/usr/bin/env python3

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Lista de puertos comunes (puedes expandir o importar desde archivo)

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP",
}

def scan_port(ip, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout (timeout)
            s.connect((ip, port))
            return port, True
    except:
        return port, False

def main():
    parser = argparse.ArgumentParser(description="🛡️ Simple Port Scanner - Python3")
    parser.add_argument("target", help="Ip o dominio a escanear")
    parser.add_argument( "-t", "--threads", type=int, default=50, help="Numero de hilos (default=50)")
    parser.add_argument("-to", "--timeout", type=int, default=1, help="Timeout de conexion en segundos")
    args = parser.parse_args()

    print(f"\n🔍 Escaneando \033[95m{args.target}\033[0m...\n")
    print(f"󰞌 Usando {args.threads} hilos - Timeout {args.timeout}s\n")
    start_time = datetime.now()

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [executor.submit(scan_port, args.target, port, args.timeout) for port in common_ports]
        for future in futures:
            port, is_open = future.result()
            if is_open:
                service = common_ports.get(port, "Desconocido\n")
                print(f"\033[92m✅\033[0m Puerto \033[93m{port}\033[0m ({service}) abierto")

    duration = datetime.now() - start_time
    print(f"\n\033[91m⏱️ Escaneo completado en {duration.total_seconds():.2f} segundos.\033[0m")


if __name__ == "__main__":
    main()


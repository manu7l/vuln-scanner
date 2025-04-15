# 🛡️ Vuln Scanner

Un escáner simple pero potente de puertos y servicios hecho en Python3. Ideal para prácticas de ciberseguridad, análisis de red o como base para un escáner más avanzado.

## 🚀 Características

- Escanea puertos comunes
- Multithreading rápido
- Muestra resultados con colores y emojis 😎
- Totalmente personalizable

## 🖥️ Requisitos

- Python 3.x
- Sistema Linux o Mac (aunque funciona en Windows con terminal compatible)

## ⚙️ Opciones

Opción | Descripción        | Default


-t     | Nº de hilos        | 50

-to    | Timeout por puerto | 1


## 🚨 Uso de las opciones 
python3 vuln_scanner.py scanme.nmap.org -t 100 -to 2


## 🌐 Modo de empleo
python3 vuln_scanner.py <IP o dominio> [opciones]



Manu – @manu7l


## 📦 Instalación

```bash
git clone https://github.com/manu7l/vuln-scanner.git
cd vuln-scanner
chmod +x vuln_scanner.py








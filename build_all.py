import os
import subprocess
import shutil
import sys

# Configuration
DIST_DIR = "bin"
WORK_DIR = "build_temp"
SPEC_DIR = "spec_files"

# List of tools to build
TOOLS = [
    # Network
    {"path": "network/port_scanner.py", "name": "port_scanner"},
    {"path": "network/network_scanner.py", "name": "network_scanner"},
    {"path": "network/ssh_bruteforce.py", "name": "ssh_bruteforce"},
    
    # Web
    {"path": "web/subdomain_enumeration.py", "name": "subdomain_enum"},
    {"path": "web/directory_enumeration.py", "name": "dir_enum"},
    {"path": "web/js_crawler.py", "name": "js_crawler"},
    {"path": "web/file_downloader.py", "name": "downloader"},
    
    # Spyware
    {"path": "spyware/keylogger.py", "name": "keylogger"},
    {"path": "spyware/keylogger_server.py", "name": "keylogger_server"},
    
    # Crypto
    {"path": "crypto/hash_cracker.py", "name": "hash_cracker"},
    
    # Backdoors
    # {"path": "backdoors/reverse_shell.py", "name": "reverse_shell"}, # Uncomment when implemented
    # {"path": "backdoors/listener.py", "name": "listener"}, # Uncomment when implemented
]

def clean_dirs():
    """Create or clean directories"""
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR)
    
    if not os.path.exists(SPEC_DIR):
        os.makedirs(SPEC_DIR)

def build_tool(tool):
    """Build a single tool using PyInstaller"""
    print(f"[*] Building {tool['name']}...")
    
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--distpath", DIST_DIR,
        "--workpath", WORK_DIR,
        "--specpath", SPEC_DIR,
        "--name", tool['name'],
        "--clean",
        # Hidden imports often needed for these libraries
        "--hidden-import", "scapy",
        "--hidden-import", "requests",
        "--hidden-import", "paramiko",
        "--hidden-import", "keyboard",
        "--hidden-import", "pyfiglet",
        "--collect-all", "pyfiglet",
        tool['path']
    ]
    
    try:
        subprocess.check_call(cmd)
        print(f"[+] Successfully built {tool['name']}")
    except subprocess.CalledProcessError:
        print(f"[!] Failed to build {tool['name']}")

def main():
    print("=======================================")
    print("   PenTools Compiler (PyInstaller)")
    print("=======================================")
    
    clean_dirs()
    
    for tool in TOOLS:
        if os.path.exists(tool['path']):
            build_tool(tool)
        else:
            print(f"[!] File not found: {tool['path']}")

    # Cleanup temp build dir
    if os.path.exists(WORK_DIR):
        try:
            shutil.rmtree(WORK_DIR)
            print("[*] Cleaned up temporary build files.")
        except Exception as e:
            print(f"[!] Could not clean up {WORK_DIR}: {e}")

    print("\n[+] Build process complete. Check the 'bin/' folder.")

if __name__ == "__main__":
    main()

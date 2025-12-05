import requests
import pyfiglet
import sys
import argparse
import concurrent.futures

def check_directory(url, timeout):
    try:
        r = requests.get(url, timeout=timeout)
        if r.status_code != 404:
            print(f"[+] Found: {url} | Code: {r.status_code}")
            return True
    except requests.RequestException:
        pass
    return False

def main():
    ascii_banner = pyfiglet.figlet_format("PenTools \n Dir Enumeration")
    print(ascii_banner)

    parser = argparse.ArgumentParser(description='Threaded Directory Enumeration Tool')
    parser.add_argument('ip', help='Target IP Address')
    parser.add_argument('-w', '--wordlist', default="directories.txt", help='Path to wordlist (default: directories.txt)')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of threads (default: 10)')
    parser.add_argument('--timeout', type=int, default=2, help='Request timeout in seconds')

    args = parser.parse_args()
    
    # Construct base URL
    base_url = f"http://{args.ip}"
    print(f"[*] Scanning directories on {base_url}...")
    print(f"[*] Wordlist: {args.wordlist}")
    print(f"[*] Threads: {args.threads}")

    try:
        with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
             # Strip newlines and spaces
            directories = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Error: Wordlist not found at {args.wordlist}")
        sys.exit(1)

    print(f"[*] Loaded {len(directories)} valid directory names.")
    print("[*] Starting Scan...\n")

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = []
        for directory in directories:
            # Check logic: normally valid directories don't need .html extension enforced unless specified
            # The original script enforced .html: f"http://{sys.argv[1]}/{dir}.html"
            # I will preserve this behavior but it might be limiting. 
            # Better approach: check exactly what is in wordlist + extension.
            # For now, respecting original logic:
            url = f"{base_url}/{directory}.html" 
            futures.append(executor.submit(check_directory, url, args.timeout))
            
        concurrent.futures.wait(futures)

    print("\n[*] Scan completed.")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except SystemExit:
        pass
    except Exception as e:
        print(f"Error: {e}")
    input("\nPress Enter to exit...")
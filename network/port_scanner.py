# Import sys for system interaction (arguments, output)
import sys
# Import socket to create network connections
import socket
# Import argparse to handle command line arguments easily
import argparse
# Import concurrent.futures to handle threads efficiently
import concurrent.futures
# Import threading to use locks and prevent printing issues
import threading

# Create a lock so prints don't mix when multiple threads try to write at once
print_lock = threading.Lock()

# Function to grab the "banner" (welcome message) of a service on a port
def grab_banner(ip, port):
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout of 2 seconds
        s.settimeout(2)
        # Try to connect to the IP and port
        s.connect((ip, port))
        
        # Try to receive data (the banner)
        try:
            # Some services wait for input first, but for simple banners we just read.
            # Read 1024 bytes, decode to text and strip extra spaces.
            banner = s.recv(1024).decode().strip()
            if not banner:
                banner = "No banner"
            
        except:
            # If reading fails (timeout or empty), assume no banner
            banner = "No banner (timeout/empty)"
            
        # Close the connection
        s.close()
        return banner
    except:
        # If initial connection fails, return None
        return None

# Main function to scan a specific port
def scan_port(ip, port):
    try:
        # Create a socket for scanning
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Short timeout (1s) for scanning to be fast
        sock.settimeout(1)
        # connect_ex returns 0 if connection is successful (port open), or an error code if not
        result = sock.connect_ex((ip, port))
        
        # If result is 0, the port is open
        if result == 0:
            sock.close()
            # Try to grab the service banner
            banner = grab_banner(ip, port)
            # Use the lock to print in an orderly fashion
            with print_lock:
                if banner and banner != "No banner":
                     print(f"[+] Port {port:<5} OPEN | Banner: {banner}")
                else:
                     print(f"[+] Port {port:<5} OPEN")
            # Return the open port
            return port
        # Close the socket if it wasn't open
        sock.close()
    except Exception:
        pass
    return None

# Main program function
def main():
    # Configure the arguments acceptable by the program
    parser = argparse.ArgumentParser(description='Threaded Port Scanner with Banner Grabbing')
    parser.add_argument('target', help='Target IP Address')
    parser.add_argument('-p', '--ports', default="1-1000", help='Port range (e.g. 1-1000) or single port')
    parser.add_argument('-t', '--threads', type=int, default=100, help='Number of threads')
    
    # Process received arguments
    args = parser.parse_args()
    
    # Process port range
    try:
        if '-' in args.ports:
            # If there is a hyphen, separate start and end
            start, end = map(int, args.ports.split('-'))
            ports = range(start, end + 1)
        else:
            # Otherwise, it's a single port
            ports = [int(args.ports)]
    except ValueError:
        print("[!] Invalid port format. Use start-end (e.g. 1-100) or single port.")
        sys.exit(1)
        
    print(f"\n[*] Scanning {args.target}...")
    print(f"[*] Port Range: {args.ports}")
    print(f"[*] Threads: {args.threads}\n")
    
    open_ports = []
    
    try:
        # Use ThreadPoolExecutor to handle multiple scans in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
            # Launch a scan task for each port and save the "futures"
            futures = {executor.submit(scan_port, args.target, port): port for port in ports}
            
            # As threads finish (as_completed), process results
            for future in concurrent.futures.as_completed(futures):
                port = futures[future]
                if future.result():
                    open_ports.append(port)
                    
    except KeyboardInterrupt:
        # If user presses Ctrl+C, exit cleanly
        print("\n[!] Scan aborted by user.")
        sys.exit(0)

    # Final summary
    if not open_ports:
        print("\n[-] No open ports found.")
    else:
        print(f"\n[*] Scan complete. Found {len(open_ports)} open ports.")

# Script entry point
if __name__ == '__main__':
    main()

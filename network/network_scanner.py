# Import everything from scapy to manipulate network packets
from scapy.all import *
import sys

# Script to scan local network looking for connected devices
# Usage: python Network_scanner.py [IP_Range]
# Example: python Network_scanner.py 10.80.181.0/24

# Check if user specified an IP range, otherwise use default
if len(sys.argv) > 1:
    target_ip = sys.argv[1]
else:
    target_ip = "10.80.181.0/24"

# Warn that we are scanning
print(f"[*] Scanning network: {target_ip}...")

# Create ARP packet asking "Who has this IP?"
arp = ARP(pdst=target_ip)
# Create Ethernet frame destined for Broadcast (all devices)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# Combine Ethernet frame and ARP packet
packet = ether/arp

try:
    # Send packet and wait for responses (srp = send and receive packet)
    # verbose=0 so it doesn't print internal scapy messages
    result = srp(packet, timeout=3, verbose=0)[0]

    # Print result table header
    print("\nAvailable devices in the network:")
    print("IP" + " "*18+"MAC")
    print("-" * 35)
    
    clients = []
    # Iterate over received responses (sent, received)
    for sent, received in result:
        # Save client data
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        # Print IP and MAC of found device
        print(f"{received.psrc:20}    {received.hwsrc}")

except Exception as e:
    # Error handling
    print(f"[!] Error: {e}")
    print("[!] Ensure you have Npcap installed (required for Scapy on Windows).")
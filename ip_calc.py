import ipaddress

def compute_ip_planning():
    ip = input("Enter the IP address with CIDR (e.g., 192.168.1.0/24): ")
    try:
        network = ipaddress.IPv4Network(ip, strict=False)
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Netmask: {network.netmask}")
        print(f"Available Hosts: {list(network.hosts())}")
    except ValueError:
        print("Invalid IP address!")

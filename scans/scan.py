from scapy.all import ICMP, IP, sr1, conf
import ipaddress

def scan_subnet(subnet):
    conf.verb = 0  # Disable verbose in Scapy
    active_hosts = []

    for ip in ipaddress.IPv4Network(subnet):
        packet = IP(dst=str(ip))/ICMP()
        reply = sr1(packet, timeout=1)
        if reply:
            active_hosts.append(str(ip))

    return active_hosts

# Example Usage
subnet = "192.168.0.0/24"  # Replace with your subnet
active_hosts = scan_subnet(subnet)
print(f"Active hosts on the subnet {subnet}:")
for host in active_hosts:
    print(host)


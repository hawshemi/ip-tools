import re
from collections import Counter
import ipaddress

# Function to validate an IP address
def is_valid_ip(ip):
    try:
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    except ValueError:
        return False

# Function to check if an IP address is local
def is_local_ip(ip):
    try:
        ip_obj = ipaddress.IPv4Address(ip)
        local_ip_ranges = [
            ipaddress.IPv4Network('10.0.0.0/8'),
            ipaddress.IPv4Network('172.16.0.0/12'),
            ipaddress.IPv4Network('192.168.0.0/16'),
            ipaddress.IPv4Network('100.64.0.0/10')
        ]
        return any(ip_obj in local_range for local_range in local_ip_ranges)
    except ipaddress.AddressValueError:
        return False

# Read IP addresses from the input file
with open("input.txt", "r") as f:
    ip_addresses = f.read().splitlines()

# Validate and filter IP addresses
valid_ip_addresses = [ip for ip in ip_addresses if is_valid_ip(ip) and not is_local_ip(ip)]

# Count the IP addresses
ip_counter = Counter(valid_ip_addresses)

# Write the counted IP addresses to a file sorted by count
with open("counted_ips.txt", "w") as f:
    for ip, count in ip_counter.most_common():
        f.write(f"{count} {ip}\n")

# Write unique IP addresses to a separate file
unique_ips = set(valid_ip_addresses)
with open("unique_ips.txt", "w") as f:
    for ip in unique_ips:
        f.write(f"{ip}\n")

import re
from collections import Counter

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

# Function to filter out local IP addresses
def is_local_ip(ip):
    return ip.startswith("10.") or ip.startswith("192.168.") or ip == "127.0.0.1"

# Read IP addresses from the input file
with open("ip.txt", "r") as f:
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

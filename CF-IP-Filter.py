import ipaddress

# List of Cloudflare IP address ranges
cloudflare_ranges = [
    "173.245.48.0/20",
    "103.21.244.0/22",
    "103.22.200.0/22",
    "103.31.4.0/22",
    "141.101.64.0/18",
    "108.162.192.0/18",
    "190.93.240.0/20",
    "188.114.96.0/20",
    "197.234.240.0/22",
    "198.41.128.0/17",
    "162.158.0.0/15",
    "104.16.0.0/13",
    "104.24.0.0/14",
    "172.64.0.0/13",
    "131.0.72.0/22"
]

# Function to check if an IP address is in Cloudflare ranges
def is_cloudflare_ip(ip):
    for range_str in cloudflare_ranges:
        if ipaddress.ip_address(ip) in ipaddress.ip_network(range_str):
            return True
    return False

# Read the input file and omit Cloudflare IP addresses
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

filtered_ips = [line.strip() for line in lines if not is_cloudflare_ip(line.strip())]

# Write the filtered IPs to a new file
with open('output.txt', 'w') as output_file:
    for ip in filtered_ips:
        output_file.write(ip + '\n')

print("Filtered IP addresses saved to 'output.txt'")

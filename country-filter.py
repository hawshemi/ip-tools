import requests
import json

# Replace with your input and output file paths
input_file_path = 'input.txt'
output_file_path = 'output.txt'

# List of countries to filter
filtered_countries = ['IR', 'CN', 'RU']

# Function to get the country code of an IP address
def get_country_code(ip):
    url = f"https://ipinfo.io/{ip}/country"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return None

# Read IP addresses from the input file
with open(input_file_path, 'r') as input_file:
    ip_addresses = input_file.readlines()

# Filter IP addresses by country and print before writing to the output file
filtered_ips = []
for ip in ip_addresses:
    country_code = get_country_code(ip.strip())
    if country_code:
        print(f"IP: {ip.strip()}, Country Code: {country_code}")
        if country_code not in filtered_countries:
            filtered_ips.append(ip)

# Write filtered IP addresses to the output file
with open(output_file_path, 'w') as output_file:
    output_file.writelines(filtered_ips)

print(f"Filtered IP addresses written to {output_file_path}")

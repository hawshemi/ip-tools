import requests
import re

IPINFO_API_URL = "https://ipinfo.io/{ip}/json"

def read_ip_addresses_from_file(filename):
    # Read IP addresses from a file and return them as a list.
    with open(filename, 'r', encoding="utf8") as file:
        return [line.strip() for line in file]

def get_ip_info(ip):
    # Get information about an IP address using the ipinfo.io API.
    try:
        response = requests.get(IPINFO_API_URL.format(ip=ip))
        response.raise_for_status()
        data = response.json()

        country = data.get("country")
        isp = data.get("org")
        city = data.get("city")
        region = data.get("region")

        as_match = re.search(r'AS\d+', isp) if isp else None
        as_number = as_match.group(0) if as_match else 'N/A'

        return country, isp, as_number, city, region
    except requests.exceptions.RequestException as e:
        return None, None, None, None, None

def is_datacenter(ip):
    # Check if an IP address belongs to a datacenter.
    try:
        response = requests.get(IPINFO_API_URL.format(ip=ip))
        response.raise_for_status()
        org = response.json().get("org", "").lower()

        keywords = ["data center", "hosting", "cloud", "server", "backbone", "back-bone", "google", "cloudflare"]
        return any(keyword in org for keyword in keywords)
    except requests.exceptions.RequestException as e:
        return False

def main():
    filename = "ip.txt"
    ip_addresses = read_ip_addresses_from_file(filename)

    with open("output.txt", "w", encoding="utf8") as output_file:
        for ip in ip_addresses:
            country, isp, as_number, city, region = get_ip_info(ip)
            formatted_isp = isp.replace(as_number, '').strip() if as_number else isp.strip()
            
            output_str = f"IP: {ip} / Country: {country} / ISP: {formatted_isp} / AS Number: {as_number} / City: {city} / Region: {region}"
            print(output_str)
            output_file.write(output_str)
            
            datacenter_info = "likely a datacenter IP.\n" if is_datacenter(ip) else "not a datacenter IP.\n"
            print((datacenter_info))
            output_file.write(datacenter_info)

if __name__ == "__main__":
    main()

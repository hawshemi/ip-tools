import requests
from bs4 import BeautifulSoup

# Function to scrape the "Usage Type" from browserleaks.com
def scrape_usage_type(ip_address):
    url = f"https://browserleaks.com/ip/{ip_address}"
    print(f"Scraping Usage Type for IP: {ip_address}")
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        usage_type_element = soup.find("td", text="Usage Type")
        
        if usage_type_element:
            usage_type = usage_type_element.find_next_sibling("td").text.strip()
            return usage_type
        else:
            return "Usage Type not found"
    else:
        return "Error fetching data"

# Function to get organization (org) from ipinfo.io
def get_org(ip_address):
    url = f"https://ipinfo.io/{ip_address}/org?token=XXX"
    print(f"Fetching Org for IP: {ip_address}")
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Org not found"

# Keywords to exclude
exclude_keywords = ["Cellular", "Residential"]

# Read IP addresses from ip.txt and process each one
with open("input.txt", "r") as file:
    ip_addresses = file.read().splitlines()

for ip_address in ip_addresses:
    usage_type = scrape_usage_type(ip_address)
    org = get_org(ip_address)

    # Exclude IPs with usage type containing the keywords
    if not any(keyword in usage_type for keyword in exclude_keywords):
        # Combine and write the result to a file
        result = f"IP: {ip_address}\nUsage Type: {usage_type}\nOrg: {org}\n\n"
        with open("output.txt", "a") as output_file:
            output_file.write(result)

    print(f"Completed processing IP: {ip_address}")

import re

# Regular expression pattern to match the timestamp and IP address
pattern = r'\[(.*?)\]\s(\d+\.\d+\.\d+\.\d+)\s'

# Open the log file for reading
with open('access6.log', 'r') as file:
    # Create an output file for writing
    with open('ip6.txt', 'w') as output_file:
        # Iterate through each line in the file
        for line in file:
            # Use regular expression to find matches
            matches = re.findall(pattern, line)
            if matches:
                # Extract and write the IP address to the output file
                timestamp, ip_address = matches[0]
                output_file.write(ip_address + '\n')

print("IP addresses have been written to 'output.txt'")

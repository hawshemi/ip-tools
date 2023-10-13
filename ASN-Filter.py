import re

# Read data from input.txt
with open("filtered-scanned.txt", "r") as input_file:
    data = input_file.read()

# Split data into blocks using double newline as a separator
blocks = data.strip().split("\n\n")

# Initialize a list to store the filtered data
filtered_data = []

# Define a regular expression pattern to match the keyword "AS16322"
pattern = re.compile(r"AS43754")

# Loop through each block and filter the data
for block in blocks:
    # Check if the pattern "AS16322" is found in the block
    if not pattern.search(block):
        # Add a newline before the "IP" line
        block_with_newline = re.sub(r"IP:", "\nIP:", block)
        # Append the modified block to the filtered_data list
        filtered_data.append(block_with_newline)

# Write the filtered data to output.txt
with open("output.txt", "w") as output_file:
    for block in filtered_data:
        output_file.write(block + "\n")

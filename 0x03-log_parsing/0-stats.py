#!/usr/bin/env python3

# Import the sys module to access stdin
import sys

# Import the defaultdict class from the collections module to create a dictionary with default values
from collections import defaultdict

# Initialize the total file size to 0
total_size = 0

# Create a dictionary to count the number of lines for each status code
line_counter = defaultdict(int)

# Initialize a counter for the current number of lines
current_lines = 0

# Define a function to print the counters
def print_counters():
    # Use the global keyword to access the global current_lines variable
    global current_lines
    # Print the total file size
    print(f'Total file size: File size: {total_size}')
    # Print the number of lines for each status code in sorted order
    for status_code in sorted(line_counter.keys()):
        print(f'{status_code}: {line_counter[status_code]}')
    # Reset the current_lines counter
    current_lines = 0
    # Print a blank line for readability
    print()

# Iterate over each line in stdin
for line in sys.stdin:
    # Increment the current_lines counter
    current_lines += 1
    # Split the line into parts using spaces as separators
    parts = line.strip().split(' ')
    # If the line does not have exactly 6 parts, skip it
    if len(parts)!= 6:
        continue
    
    # Extract the IP address, date, method, status code, and file size from the parts
    ip, date, method, status_code, file_size = parts
    # Convert the file size to an integer
    file_size = int(file_size)
    # Add the file size to the total size
    total_size += file_size
    # Increment the count for the status code
    line_counter[status_code] += 1

    # If the current_lines counter is a multiple of 10 or equal to 10000, print the counters
    if current_lines % 10 == 0 or current_lines == 10000:
        print_counters()

# Print the final counters
print_counters()

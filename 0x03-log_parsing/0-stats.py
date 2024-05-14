#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import sys

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """
    Print the statistics: total file size and number of lines per status code.
    """
    print("File size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) != 7 or parts[2] != '"GET' or parts[3] != '/projects/260' or parts[4] != 'HTTP/1.1"' or not parts[5].isdigit() or not parts[6].isdigit():
            continue

        status_code = int(parts[5])
        file_size = int(parts[6])

        total_file_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:

    print_statistics()
    raise

print_statistics()

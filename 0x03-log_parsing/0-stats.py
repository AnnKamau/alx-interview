#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys

def print_stats(total_size, status_codes):
    """
    Prints the statistics
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        ip = parts[0]
        status_code = parts[-2]
        file_size = parts[-1]
        
        try:
            total_size += int(file_size)
        except ValueError:
            continue

        try:
            if int(status_code) in status_codes:
                status_codes[int(status_code)] += 1
        except ValueError:
            continue

        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

print_stats(total_size, status_codes)

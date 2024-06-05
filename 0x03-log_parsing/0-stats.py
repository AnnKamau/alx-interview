#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import sys
import signal

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """
    Print the statistics: total file size and number of lines per status code.
    """
    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
    print()

def signal_handler(sig, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).
    """
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        
        # Skip lines that do not match the expected format
        if len(parts) != 9:
            continue

        ip_address = parts[0]
        date = parts[3][1:-1]
        method = parts[5][1:]
        path = parts[6]
        protocol = parts[7][:-1]
        status_code_str = parts[8]
        file_size_str = parts[9]

        if method != "GET" or path != "/projects/260" or protocol != "HTTP/1.1":
            continue
        if not status_code_str.isdigit() or not file_size_str.isdigit():
            continue

        status_code = int(status_code_str)
        file_size = int(file_size_str)

        total_file_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_statistics()

except (EOFError, KeyboardInterrupt):
    print_statistics()
    sys.exit(0)

print_statistics()

#!/usr/bin/env python3

import sys
from collections import defaultdict

total_size = 0
line_counter = defaultdict(int)
current_lines = 0

def print_counters():
    global current_lines
    print(f'Total file size: File size: {total_size}')
    for status_code in sorted(line_counter.keys()):
        print(f'{status_code}: {line_counter[status_code]}')
    current_lines = 0
    print()

for line in sys.stdin:
    current_lines += 1
    parts = line.strip().split(' ')
    if len(parts) != 6:
        continue
    
    ip, date, method, status_code, file_size = parts
    file_size = int(file_size)
    total_size += file_size
    line_counter[status_code] += 1

    if current_lines % 10 == 0 or current_lines == 10000:
        print_counters()

print_counters()

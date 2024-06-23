#!/usr/bin/python3
"""
log parsing
"""

import sys
import signal

# Initialize metrics
total_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_metrics():
    """" print """
    global total_size, status_code_count
    print(f"File size: {total_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def handle_interrupt(signum, frame):
    """ handle """
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        
        ip_address = parts[0]
        date = parts[3]
        request = ' '.join(parts[4:7])
        status_code = parts[-2]
        file_size = parts[-1]

        # Validate the format
        if not date.startswith('[') or not date.endswith(']'):
            continue
        if not request.startswith('"GET /projects/260 HTTP/1.1"'):
            continue
        if not status_code.isdigit() or not file_size.isdigit():
            continue

        status_code = int(status_code)
        file_size = int(file_size)
        
        # Update metrics
        total_size += file_size
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        
        line_count += 1
        
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    sys.exit(0)

print_metrics()


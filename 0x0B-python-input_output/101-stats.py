#!/usr/bin/python3
"""a script that reads stdin
line by line and computes metrics:"""
import sys


def compute_metrics():
    total_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split(" ")
            if len(parts) >= 9:
                status_code = int(parts[7])
                file_size = int(parts[8])
                total_size += file_size
                status_code_counts[status_code] += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_code_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, status_code_counts)

def print_metrics(total_size, status_code_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

if __name__ == "__main__":
    compute_metrics()
import sys
import re

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read input line by line
    for line in sys.stdin:
        # Parse the line using a regular expression
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match:
            ip, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            # Update total file size
            total_size += file_size

            # Update status code counts
            if status_code in status_counts:
                status_counts[status_code] += 1

            # Increment line count
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code, count in sorted(status_counts.items()):
                    if count > 0:
                        print(f"{code}: {count}")

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")

# Final statistics
print(f"File size: {total_size}")
for code, count in sorted(status_counts.items()):
    if count > 0:
        print(f"{code}: {count}")

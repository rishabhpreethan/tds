import gzip
import re
from datetime import datetime
from collections import defaultdict

def parse_log_line(line):
    pattern = (
        r'(\S+) (\S+) (\S+) \[(.*?)\] "([^"]*)" (\d{3}) (\d+) "([^"]*)" "([^"]*)" (\S+) (\S+)'
    )
    match = re.match(pattern, line)
    if match:
        return match.groups()
    return None

def main():
    log_file_path = 'tds\\week3\\s-anand.net-May-2024.gz'
    target_path = '/tamilmp3/'
    target_date = '29/May/2024'
    ip_size_totals = defaultdict(int)

    with gzip.open(log_file_path, 'rt') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            if not parsed_line:
                continue
            
            ip, rlogname, ruser, time_str, request, status, size, referer, user_agent, vhost, server = parsed_line
            log_date = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S %z").strftime("%d/%b/%Y")

            if target_path in request and log_date == target_date:
                ip_size_totals[ip] += int(size)
    
    # Find the IP address that downloaded the most bytes
    top_ip = max(ip_size_totals, key=ip_size_totals.get)
    top_ip_size = ip_size_totals[top_ip]

    print(f"Top IP address: {top_ip}, Bytes downloaded: {top_ip_size}")

if __name__ == '__main__':
    main()

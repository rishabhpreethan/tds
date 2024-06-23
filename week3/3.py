import gzip
import re
from datetime import datetime
from collections import defaultdict

def parse_log_line(line):
    pattern = (
        r'(\S+) (\S+) (\S+) \[(.*?)\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+) "([^"]*)" "([^"]*)" (\S+) (\S+)'
    )
    match = re.match(pattern, line)
    if match:
        return match.groups()
    return None

def main():
    log_file_path = 'tds\\week3\\s-anand.net-May-2024.gz'
    target_path = '/wp-content/'
    hourly_ip_counts = defaultdict(set)

    with gzip.open(log_file_path, 'rt') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            if not parsed_line:
                continue
            
            ip, rlogname, ruser, time_str, method, url, protocol, status, size, referer, user_agent, vhost, server = parsed_line
            log_datetime = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S %z")
            log_hour = log_datetime.strftime("%Y-%m-%d %H:00:00")
            log_day_of_week = log_datetime.weekday()

            if target_path in url and log_day_of_week == 5:  # 5 corresponds to Saturday
                hourly_ip_counts[log_hour].add(ip)
    
    # Find the hour with the most unique IP addresses
    peak_hour = max(hourly_ip_counts, key=lambda hour: len(hourly_ip_counts[hour]))
    peak_hour_unique_ips = len(hourly_ip_counts[peak_hour])

    print(f"Peak hour: {peak_hour}, Unique IPs: {peak_hour_unique_ips}")

if __name__ == '__main__':
    main()

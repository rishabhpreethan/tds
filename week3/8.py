import gzip
import re
from collections import defaultdict
from datetime import datetime

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
    target_date = '16/May/2024'
    chrome_version_pattern = re.compile(r'Chrome/(\d+)\.')

    version_counts = defaultdict(int)

    with gzip.open(log_file_path, 'rt') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            if not parsed_line:
                continue
            
            ip, rlogname, ruser, time_str, request, status, size, referer, user_agent, vhost, server = parsed_line
            log_date = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S %z").strftime("%d/%b/%Y")

            if log_date == target_date:
                match = chrome_version_pattern.search(user_agent)
                if match:
                    major_version = match.group(1)
                    version_counts[major_version] += 1
    
    # Find the most common major version
    most_common_version = max(version_counts, key=version_counts.get)
    count_most_common_version = version_counts[most_common_version]

    print(f"The most common major Chrome version {most_common_version} accessed the site {count_most_common_version} times on {target_date}.")

if __name__ == '__main__':
    main()

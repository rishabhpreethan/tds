import gzip
import re
from datetime import datetime

def parse_log_line(line):
    pattern = (
        r'(\S+) (\S+) (\S+) \[(.*?)\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+) "([^"]*)" "([^"]*)" (\S+) (\S+)'
    )
    match = re.match(pattern, line)
    if match:
        return match.groups()
    return None

def is_successful(status):
    return 200 <= int(status) < 300

def main():
    log_file_path = 'tds\\week3\\s-anand.net-May-2024.gz'
    target_path = '/tamil/'
    start_time = datetime.strptime("07:00", "%H:%M").time()
    end_time = datetime.strptime("09:00", "%H:%M").time()
    count = 0

    with gzip.open(log_file_path, 'rt') as f:
        for line in f:
            parsed_line = parse_log_line(line)
            if not parsed_line:
                continue
            
            ip, rlogname, ruser, time_str, method, url, protocol, status, size, referer, user_agent, vhost, server = parsed_line
            log_time = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S %z").time()
            log_date = datetime.strptime(time_str, "%d/%b/%Y:%H:%M:%S %z").date()

            if method == 'GET' and target_path in url and start_time <= log_time <= end_time and log_date.weekday() == 3 and is_successful(status):
                count += 1

    print(count)

if __name__ == '__main__':
    main()

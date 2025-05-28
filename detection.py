import re

FAILED_LOGIN_PATTERN = re.compile(r"Failed password for (invalid user )?(\w+|\w+@|\S+) from (\d+\.\d+\.\d+\.\d+)")

def detect_log(line):
    match = FAILED_LOGIN_PATTERN.search(line)
    if match:
        invalid = match.group(1) is not None
        username = match.group(2)
        ip = match.group(3)
        return {
            'username' : username,
            'ip': ip,
            'invalid_user' : invalid,
            'raw' : line
        }
    return None
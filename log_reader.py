import time

def follow_log(filepath):
    with open(filepath, 'r') as file:
        file.seek(0,2)

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.2)
                continue
            yield line.strip()
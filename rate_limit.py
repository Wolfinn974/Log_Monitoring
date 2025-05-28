from collections import defaultdict
import time

class RateLimiter:
    def __init__(self, max_attempts=5, window_seconds=60):
        self.attempts_ip = defaultdict(list)
        self.max_attempts = max_attempts
        self.window_seconds = window_seconds
    
    def cleanup_old_attempt(self, ip, current_time):
        window_start= current_time - self.window_seconds
        self.attempts_ip[ip] = [t for t in self.attempts_ip[ip] if t >= window_start]

    def register_attempt(self, ip):
        now = time.time()
        self.cleanup_old_attempt(ip, now)
        self.attempts_ip[ip].append(now)
        return self.ip_blocked(ip)
    
    def ip_blocked(self,ip):
        return len(self.attempts_ip[ip]) >= self.max_attempts

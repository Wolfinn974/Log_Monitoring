from log_reader import follow_log
from detection import detect_log
from rate_limit import RateLimiter
from alerter import log_alert
from autoban import ban_ip
from notifier import send_telegram_alert

LOG_FILE =  "/var/log/auth.log"

ascii_banner = r"""
██╗      ██████╗  ██████╗     ███╗   ███╗ ██████╗ ███╗   ██╗██╗████████╗ ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
██║     ██╔═══██╗██╔════╝     ████╗ ████║██╔═══██╗████╗  ██║██║╚══██╔══╝██╔═══██╗██╔══██╗██║████╗  ██║██╔════╝ 
██║     ██║   ██║██║  ███╗    ██╔████╔██║██║   ██║██╔██╗ ██║██║   ██║   ██║   ██║██████╔╝██║██╔██╗ ██║██║  ███╗
██║     ██║   ██║██║   ██║    ██║╚██╔╝██║██║   ██║██║╚██╗██║██║   ██║   ██║   ██║██╔══██╗██║██║╚██╗██║██║   ██║
███████╗╚██████╔╝╚██████╔╝    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║   ██║   ╚██████╔╝██║  ██║██║██║ ╚████║╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                               
                                   🔒 SIEMlike | Log Monitoring System 🔍
"""

print(ascii_banner)

if __name__ == "__main__":
    print("[***]Log Monitoring...")
    limiter = RateLimiter(max_attempts=3, window_seconds=30)
    for line in follow_log(LOG_FILE):
        result = detect_log(line)
        if result:
            ip = result['ip']
            username = result['username']
            if limiter.register_attempt(ip):
                message = f"[MAX ALERT] SUSPICIOUS: {ip} went over attempts limits"
                log_alert(ip, username, message)
                ban_ip(ip)
                send_telegram_alert(message)
            else :
                print(f"[!]Failed log attempt: IP={result['ip']} | Username={result['username']} | Line={result['raw']}")


import subprocess

WHITELIST = ["127.0.0.1", "localhost"]

def is_whitelisted(ip):
    return ip in WHITELIST

def ban_ip(ip):
    if is_whitelisted(ip):
        print(f"[i] IP {ip} is whitelisted")
        return
    
    try:
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
        print(f"[**]IP Banned: {ip}")
    except subprocess.CalledProcessError as e:
        print(f"[X] Banning Error: {ip} : {e}")
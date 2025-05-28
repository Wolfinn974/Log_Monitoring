import json
import time
import os
import stat

ALERT_FILE = "alerts.json"

# Vérifie si le fichier existe
if os.path.exists(ALERT_FILE):
    file_permissions = os.stat(ALERT_FILE).st_mode
    desired_permissions = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH
    if (file_permissions & 0o777) != desired_permissions:
        os.chmod(ALERT_FILE, desired_permissions)

def log_alert(ip, username, message):
    alert = {
        "timestamp": time.strftime("%Y-%m-%d %H-%M-%S"),
        "ip": ip,
        "username": username,
        "alert": message
    }

    with open(ALERT_FILE, "a") as f:
        f.write(json.dumps(alert) + "\n")
    
    print(f"[***]Alert registered: {alert}")
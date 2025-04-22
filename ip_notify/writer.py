import os
import sys
from pathlib import Path

def write_ip_if_changed(ip: str) -> bool:
    path = Path(os.getenv("LAST_IP_FILE"))
    old = path.read_text().strip() if path.exists() else None
    if ip != old:
        path.parent.mkdir(exist_ok=True, parents=True)
        path.write_text(ip + "\n")
        return True
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: ip‑writer <IP>")
        sys.exit(1)
    ip = sys.argv[1]
    if write_ip_if_changed(ip):
        print(f"IP changed to {ip} and written.")
    else:
        print(f"No change: {ip} == existing IP.")
    sys.exit(0)
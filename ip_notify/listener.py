#!/usr/bin/env python3
from pyroute2 import IPRoute
from .writer import write_ip_if_changed
from .notifier import send_telegram

def do_notify(new_ip):
    if write_ip_if_changed(new_ip):
        send_telegram(new_ip)

def main():
    ipr = IPRoute()
    ipr.bind()
    for msg in ipr.get():
        if msg.get("event") == "RTM_NEWADDR":
            addr = msg.get("attrs", [])
            for k, v in addr:
                if k == "IFA_ADDRESS":
                    do_notify(v)
#!/usr/bin/env python3

from pyroute2 import IPRoute

print(">>> Starting raw netlink listener")

ipr = IPRoute()
ipr.bind()

try:
    for msg in ipr.get():
        print("📡 Netlink message:", msg)
except Exception as e:
    print("🔥 Crash:", e)

# ⚙️ IP Notifier

A minimalist, Python-based daemon that watches for IP address changes on a specific interface (e.g., wlp0s20f3) and sends a notification via Telegram when it detects one. Optionally logs the IP to a file to avoid duplicates.
Designed for headless Debian machines (like my cursed server Wraith) with dynamic IPs.

## Project Structure

ip-notifier/</br>
├──ip_nofifier/</br>
|....└──__init__.py</br>
|....└──listerner.py        # Main loop, listens for IP changes</br>
|....└──writer.py           # Handles writing IP to file</br>
|....└──notifier.py         # Sends Telegram notifications</br>
├──.env.ip_notify      # Contains BOT_TOKEN, CHAT_ID, and LAST_IP_FILE</br>

## How It Works

- Uses pyroute2.IPRoute to bind to Netlink events from the kernel.
- Listens specifically for RTM_NEWADDR events on interface wlp0s20f3.
- On valid change:
  - Writes the new IP to a specified file.
  - Sends a Telegram message using a bot token and chat ID.
  - Avoids repeat notifications by caching the last IP sent.

```.env.ip_notify Format
BOT_TOKEN=123456789:ABCDEFyourtelegrambottoken
CHAT_ID=123456789
LAST_IP_FILE=/path/to/last_ip.txt
```

- Example Telegram Message `👻 wraith 🌐 10.160.14.169`

## Key Notes

- Only reacts to changes in IPv4 addresses on `wlp0s20f3` .
- Works silently in the background with no cron jobs or polling.
  - Adding a systemd config file is necessary
- Modular: easily replace the notifier or writer with other backends.
- Works great for dynamic Wi-Fi setups, travel kits, or server resurrection rituals.

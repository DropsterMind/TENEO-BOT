import asyncio
import json
import os
from datetime import datetime
import pytz
from aiohttp import ClientSession, ClientTimeout, WSMsgType
from aiohttp_socks import ProxyConnector
from colorama import init, Fore, Style
from fake_useragent import UserAgent

init(autoreset=True)
wib = pytz.timezone("Asia/Jakarta")

class DropsterMindBot:
    def __init__(self):
        self.WS_URL = "wss://secure.ws.teneo.pro/websocket"
        self.tokens = self.load_tokens()
        self.proxies = self.load_proxies()
        self.rotate_proxy = False
        self.use_proxy = False
        self.logfile = self.setup_log_file()

    def setup_log_file(self):
        date = datetime.now(wib).strftime("%Y-%m-%d")
        filename = f"logs_{date}.txt"
        open(filename, 'w').close()
        return filename

    def log(self, message: str):
        timestamp = datetime.now(wib).strftime("%d/%m/%y %H:%M:%S WIB")
        log_line = f"[🕒 {timestamp}] {message}"
        print(log_line)
        with open(self.logfile, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")

    def welcome(self):
        logo = r"""
 ____                        _             __  __ _           _ 
|  _ \ _ __ ___  _   _ _ __ | |_ ___ _ __ |  \/  (_)_ __   __| |
| | | | '__/ _ \| | | | '_ \| __/ _ \ '__|| |\/| | | '_ \ / _` |
| |_| | | | (_) | |_| | | | | ||  __/ |   | |  | | | | | | (_| |
|____/|_|  \___/ \__,_|_| |_|\__\___|_|   |_|  |_|_|_| |_|\__,_|
                        By DropsterMind 🧠
"""
        print(Fore.GREEN + logo)

    def load_tokens(self):
        try:
            with open("tokens.json", "r") as f:
                return json.load(f)
        except:
            self.log("❌ File tokens.json Not Found.")
            return []

    def load_proxies(self):
        proxies = []
        if os.path.exists("proxy.txt"):
            with open("proxy.txt") as f:
                proxies = [line.strip() for line in f if line.strip()]
        return proxies

    def mask_email(self, email):
        local, domain = email.split("@")
        return f"{local[:3]}***@{domain}"

    def get_next_proxy(self, idx):
        if not self.proxies:
            return None
        return self.proxies[idx % len(self.proxies)]

    async def send_ping(self, ws, email, access_token):
        while True:
            await asyncio.sleep(15)
            await ws.send_json({"type": "PING"})
            self.log(f"🟢 [{self.mask_email(email)}] Ping sent 💓")

    async def handle_ws(self, email, access_token, proxy=None):
        headers = {
            "User-Agent": UserAgent().random,
            "Origin": "chrome-extension://emcclcoaglgcpoognfiggmhnhgabppkm"
        }
        params = f"?accessToken={access_token}&version=v0.2"
        connector = ProxyConnector.from_url(proxy) if proxy else None

        try:
            async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                async with session.ws_connect(self.WS_URL + params, headers=headers) as ws:
                    self.log(f"✅ [{self.mask_email(email)}] Connected 🌐 {'with proxy' if proxy else 'without proxy'}")

                    asyncio.create_task(self.send_ping(ws, email, access_token))

                    async for msg in ws:
                        if msg.type == WSMsgType.TEXT:
                            data = msg.json()
                            if "message" in data:
                                if data["message"] == "Connected successfully" or data["message"] == "Pulse from server":
                                    points_today = data.get("pointsToday", 0)
                                    points_total = data.get("pointsTotal", 0)
                                    heartbeats = data.get("heartbeats", 0)
                                    self.log(
                                        f"🏆 [{self.mask_email(email)}] Points: {points_today} 🎯 | Total: {points_total} 💰 | HB: {heartbeats} ❤️"
                                    )
                        elif msg.type == WSMsgType.ERROR:
                            self.log(f"❌ [{self.mask_email(email)}] Error: {msg.data}")
                            break

        except Exception as e:
            self.log(f"⚠️ [{self.mask_email(email)}] Connection failed: {e}")

    async def run(self):
        self.clear_console()
        self.welcome()

        if not self.tokens:
            self.log("❌ No accounts loaded.")
            return

        print("🔧 Proxy Mode:")
        print("1. Free Proxy from proxy.txt")
        print("2. Private Proxy from proxy.txt")
        print("3. Without Proxy")
        mode = input("Choose [1/2/3]: ").strip()

        if mode in ["1", "2"]:
            self.use_proxy = True
            rotate = input("🔁 Rotate invalid proxy? [y/n]: ").strip().lower()
            self.rotate_proxy = rotate == "y"

        self.log(f"👥 Running {len(self.tokens)} accounts {'with proxy' if self.use_proxy else 'without proxy'}.\n")

        tasks = []
        for idx, item in enumerate(self.tokens):
            email = item.get("Email")
            token = item.get("accessToken")
            if not email or not token:
                continue
            proxy = self.get_next_proxy(idx) if self.use_proxy else None
            tasks.append(self.handle_ws(email, token, proxy))

        await asyncio.gather(*tasks)

    def clear_console(self):
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    try:
        bot = DropsterMindBot()
        asyncio.run(bot.run())
    except KeyboardInterrupt:
        print("\n👋 Exit by user. Goodbye!")

import requests as r

import uuid, colorama
from concurrent.futures import ThreadPoolExecutor


class elaina:
    def __init__(self):
        self.api = r.Session()

    def e(self, uid):
        data = {"partnerUserId": uid}
        headers = {
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0",
            "Origin": "https://www.opera.com",
            "Referer": "https://www.opera.com/",
        }
        while True:
            try:
                return self.api.post(
                    "https://api.discord.gx.games/v1/direct-fulfillment",
                    json=data,
                    headers=headers,
                )
            except Exception as e:
                print(f"Hata alındı: {e}")

    def ilue(self, uid):
        boost = elaina().e(uid)
        try:
            with open("promos.txt", "a") as f:
                f.write(
                    f"https://discord.com/billing/partner-promotions/1180231712274387115/{boost.json()['token']}\n\n"
                )
                return True
        except Exception as e:
            return False


worker_sayisi = int(input("How many threads would you like to use?(recommended: 10): "))
print(
    """
made with love ...
YUPPPPIEEEEE
\n"""
)


success = 0
fail = 0
total = 0

with ThreadPoolExecutor(max_workers=worker_sayisi) as executor:
    while True:
        uid = str(uuid.uuid4())
        if executor.submit(elaina().ilue, uid).result():
            success += 1
            total += 1
        else:
            fail += 1
            total += 1
        print(
            colorama.Fore.GREEN
            + f"\rSuccess: {success}"
            + colorama.Fore.RESET
            + " / "
            + colorama.Fore.RED
            + f"Fail: {fail}"
            + colorama.Fore.RESET
            + " / "
            + colorama.Fore.YELLOW
            + f"Total: {total}"
            + colorama.Fore.RESET,
            end="",
        )

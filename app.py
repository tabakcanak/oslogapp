import os
import time
from datetime import datetime

import requests


SLACK_API_URL = os.environ["SLACK_API_URL"]
APP_NAME = os.environ["APP_NAME"]
FOOTER_NAME = os.environ["FOOTER_NAME"]
INTERVAL_SECONDS = int(os.environ.get("INTERVAL_SECONDS", "60"))


def send_message():
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    payload = {
        "attachments": [
            {
                "color": "good",
                "text": "OK",
                "title": f"{APP_NAME} - ok",
                "footer": f"{FOOTER_NAME} | {now}",
            }
        ]
    }

    try:
        response = requests.post(
            SLACK_API_URL,
            json=payload,
            timeout=10,
        )

        if response.status_code == 200:
            print(f"[{now}] OK - {APP_NAME}", flush=True)
        else:
            print(
                f"[{now}] ERROR - HTTP {response.status_code}: {response.text}",
                flush=True,
            )

    except requests.RequestException as e:
        print(f"[{now}] ERROR - {e}", flush=True)


def main():
    print(f"App: {APP_NAME}", flush=True)
    print(f"Footer: {FOOTER_NAME}", flush=True)
    print(f"Interval: {INTERVAL_SECONDS} seconds", flush=True)

    while True:
        send_message()
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()

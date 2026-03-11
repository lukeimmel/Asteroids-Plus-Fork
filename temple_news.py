import requests
from bs4 import BeautifulSoup

def get_temple_alerts():
    url = "https://safety.temple.edu/tusafe/tualert"

    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text("\n", strip=True)

        lines = []
        for line in text.split("\n"):
            line = line.strip()
            if len(line) > 25:
                lines.append(line)
            if len(lines) == 3:
                break

        if not lines:
            return ["Temple alerts unavailable."]
        return lines

    except Exception:
        return [
            "Temple Alerts",
            "Check TUalert page",
            "Source unavailable"
        ]

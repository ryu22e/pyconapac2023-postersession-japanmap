from collections.abc import Iterator

import requests
from bs4 import BeautifulSoup

URL = "https://www.pycon.jp/support/bootcamp.html"
USER_AGENT = "pyconapac2023-postersession-japanmap/0.1.0"


def get_prefs() -> Iterator[str]:
    r = requests.get(URL, headers={"User-Agent": USER_AGENT})
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.select_one("table.docutils,.align-default")
    tbody = table.tbody if table else None
    strong_tags = tbody.find_all("strong") if tbody else []
    for strong_tag in strong_tags:
        yield strong_tag.text

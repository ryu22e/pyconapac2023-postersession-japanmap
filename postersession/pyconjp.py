from collections.abc import Iterator

import requests
from bs4 import BeautifulSoup
from requests_cache import CachedSession

URL = "https://www.pycon.jp/support/bootcamp.html"
USER_AGENT = "pyconapac2023-postersession-japanmap/0.1.0"


def _get_session(
    cache_directory: str | None,
) -> requests.Session | CachedSession:
    session: requests.Session | CachedSession
    if cache_directory:
        session = CachedSession(
            cache_directory, backend="filesystem", serializer="json"
        )
    else:
        session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    return session


def get_prefs(cache_directory: str | None = None) -> Iterator[str]:
    session = _get_session(cache_directory)
    r = session.get(URL)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.select_one("table.docutils,.align-default")
    tbody = table.tbody if table else None
    strong_tags = tbody.find_all("strong") if tbody else []
    for strong_tag in strong_tags:
        yield strong_tag.text

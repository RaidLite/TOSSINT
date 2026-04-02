from maigret.maigret import maigret as maigret_search
from maigret.result import MaigretCheckStatus
from maigret.sites import MaigretDatabase
from json import load
from logging import getLogger, CRITICAL
from os import path
import maigret
from typing import Any
from sherlock_project.result import QueryStatus
from sherlock_project.sherlock import sherlock, QueryNotifyPrint
from sherlock_project.sites import SitesInformation
from tools.utils.utils import get_now

def run_sherlock(username: str) -> dict[str, Any]:
    try:
        sites = SitesInformation()
        site_data = {s.name: s.information for s in sites}
        notify = QueryNotifyPrint(result=None, verbose=False, print_all=False, browse=False)
        results = sherlock(username, site_data, notify, timeout=10)
        found = {s: r['url_user'] for s, r in results.items() if
                 r.get("status") and r["status"].status == QueryStatus.CLAIMED}
        return {"tool": "sherlock", "username": username, "timestamp": get_now(),
                "data": {"found_count": len(found), "accounts": found}}
    except Exception as e:
        return {"tool": "sherlock", "username": username, "error": str(e)}

async def check_username(username: str, top: int = 500) -> str:
    db = MaigretDatabase()
    base_path = path.dirname(maigret.__file__)
    db_path = path.join(base_path, "resources/data.json")
    with open(db_path, "r", encoding="utf-8") as f: db.load_from_json(load(f))
    sites = db.ranked_sites_dict(top=top)
    logger = getLogger("maigret")
    logger.setLevel(CRITICAL)

    try:
        results = await maigret_search(username=username, site_dict=sites, timeout=10, logger=logger)
        urls = [
            data["url_user"]
            for data in results.values()
            if data.get("status") and data["status"].status == MaigretCheckStatus.CLAIMED
        ]

    except Exception: urls = []
    if not urls: return f"[username] {username}\n  no accounts found"
    lines = "\n".join(f"  · {url}" for url in urls)
    return f"[username] {username}\n{lines}"


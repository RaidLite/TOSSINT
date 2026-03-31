from json import load
from logging import getLogger, CRITICAL
from os import path
import maigret
from maigret.maigret import maigret as maigret_search
from maigret.result import MaigretCheckStatus
from maigret.sites import MaigretDatabase

async def check_username(username: str, top: int = 500) -> str:
    db = MaigretDatabase()
    base_path = path.dirname(maigret.__file__)
    db_path = path.join(base_path, "resources/data.json")
    with open(db_path, "r", encoding="utf-8") as f: db.load_from_json(load(f))
    sites = db.ranked_sites_dict(top=top)
    logger = getLogger("maigret")
    logger.setLevel(CRITICAL)

    try:
        results = await maigret_search(username=username, site_dict=sites, timeout=10, logger=logger,)
        urls = [
            data["url_user"]
            for data in results.values()
            if data.get("status") and data["status"].status == MaigretCheckStatus.CLAIMED
        ]
    except Exception: urls = []

    if not urls: return f"[username] {username}\n  no accounts found"
    lines = "\n".join(f"  · {url}" for url in urls)
    return f"[username] {username}\n{lines}"
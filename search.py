import maigret
from asyncio import run, gather
from datetime import datetime
from json import load
from logging import getLogger, CRITICAL
from os import path
from typing import Any
from holehe.core import import_submodules, get_functions, launch_module
from httpx import AsyncClient
from maigret.maigret import maigret as maigret_search
from maigret.result import MaigretCheckStatus
from maigret.sites import MaigretDatabase
from sherlock_project.result import QueryStatus
from sherlock_project.sherlock import sherlock, QueryNotifyPrint
from sherlock_project.sites import SitesInformation

def get_now(): return datetime.now().isoformat()
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

def run_holehe(email: str) -> dict[str, Any]:
    async def _exec():
        async with AsyncClient(timeout=10) as client:
            output = []
            modules = import_submodules("holehe.modules")
            websites = get_functions(modules)
            tasks = [launch_module(m, email, client, output) for m in websites]
            await gather(*tasks, return_exceptions=True)
            return output

    try:
        raw = run(_exec())
        found = [{"service": r.get("name"), "recovery": r.get("emailrecovery"), "phone": r.get("phoneNumber")} for r in
                 raw if isinstance(r, dict) and r.get("exists")]
        return {"tool": "holehe", "email": email, "timestamp": get_now(),
                "data": {"found_count": len(found), "found": found,
                         "rate_limited": [r.get("name") for r in raw if isinstance(r, dict) and r.get("rateLimit")]}}
    except Exception as e:
        return {"tool": "holehe", "email": email, "error": str(e)}


async def check_username(username: str, top: int = 500) -> str:
    db = MaigretDatabase()
    base_path = path.dirname(maigret.__file__)
    db_path = path.join(base_path, "resources/data.json")
    with open(db_path, "r", encoding="utf-8") as f:
        db.load_from_json(load(f))
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
    except Exception:
        urls = []

    if not urls: return f"[username] {username}\n  no accounts found"
    lines = "\n".join(f"  · {url}" for url in urls)
    return f"[username] {username}\n{lines}"

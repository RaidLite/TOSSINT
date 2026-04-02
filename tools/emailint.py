from asyncio import run, gather
from typing import Any
from tools.utils.utils import get_now
from holehe.core import import_submodules, get_functions, launch_module
from httpx import AsyncClient

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
        found = [
            {"service": r.get("name"), "recovery": r.get("emailrecovery"),
             "phone": r.get("phoneNumber")} for r in
                 raw if isinstance(r, dict) and r.get("exists")]
        return {"tool": "holehe", "email": email, "timestamp": get_now(),
                "data": {"found_count": len(found), "found": found,
                         "rate_limited": [r.get("name") for r in raw if isinstance(r, dict) and r.get("rateLimit")]}}
    except Exception as e:
        return {"tool": "holehe", "email": email, "error": str(e)}
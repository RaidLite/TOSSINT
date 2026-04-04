import aiofiles

from datetime import datetime
from json import dumps
from os import system, name
from pystyle import Colorate, Colors

def get_now():
    return datetime.now().isoformat()

def cls():
    system('cls' if name == 'nt' else 'clear')

def print_gradient(text):
    print(Colorate.Vertical(Colors.red_to_yellow, text))

async def save(path, data):
    async with aiofiles.open(path, "w", encoding="utf-8") as f:
        await f.write(dumps(data, ensure_ascii=False, indent=4))
from datetime import datetime
from json import dump
from os import system, name
from pystyle import Colorate, Colors

def get_now(): return datetime.now().isoformat()
def cls(): system('cls' if name == 'nt' else 'clear')
def print_gradient(text): print(Colorate.Vertical(Colors.blue_to_cyan, text))
async def save(path, data):
    with open(path, "w", encoding="utf-8") as f: dump(data, f, ensure_ascii=False, indent=4)
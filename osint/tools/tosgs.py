from asyncio import sleep
from json import dump, load
from os import listdir, makedirs
from re import findall
from httpx import AsyncClient
from qrcode import QRCode
from telethon import (
    types,
    functions,
    TelegramClient,
    errors
)
from tqdm.asyncio import tqdm
from osint.tools.settings import session_name, tosgs_menu, tosgs_title, url, api_id, api_hash, path_json, path_nft_json, nft_ids, folder_json
from osint.tools.utils import cls, print_gradient, save

def get_sessions(): return sorted([f.replace('session_', '').replace('.session', '') for f in listdir('TOSGS') if f.startswith('session_') and f.endswith('.session')])
async def get_invoice(peer, g_id): return types.InputInvoiceStarGift(hide_name=False, include_upgrade=False, peer=peer, gift_id=g_id, message=types.TextWithEntities(text="", entities=[]))
async def get_all_gifts_not_hidden(client): return await client(functions.payments.GetStarGiftsRequest(hash=0))
async def get_client_not_started(S_NAME): return TelegramClient(session=f'session_{S_NAME}', api_id=api_id, api_hash=api_hash, device_model="iPhone 5s", system_version="12.5.8")
async def payment_request(invoice, client): return await client(functions.payments.GetPaymentFormRequest(invoice=invoice, theme_params=None))

async def get_all_gifts_ids():
    async with AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200: return []
        html_content = response.text
        gifts_ids = findall(r'<span class="name">([^<]+)</span>', html_content)
        gifts_ids = [gift_id.strip().rstrip('/') for gift_id in gifts_ids]
    return gifts_ids


def get_gifts_all_id_array():
    try:
        with open("ids/all_gifts.json", "r", encoding="utf-8") as f:
            data = load(f)
            return [int(g_id) for g_id in data.get("ids", [])]
    except (FileNotFoundError, ValueError, KeyError): return []

async def get_client(s_name):
    client = await get_client_not_started(s_name)
    await client.start()
    return client

def format_gift(g):
    return {
        "id": g.id,
        "title": getattr(g, 'title', None),
        "stars": getattr(g, 'stars', 0),
        "convert_stars": getattr(g, 'convert_stars', 0),
        "limited": getattr(g, 'limited', False),
        "sold_out": getattr(g, 'sold_out', False),
        "availability_remains": getattr(g, 'availability_remains', None),
        "availability_total": getattr(g, 'availability_total', None),
        "first_sale_date": str(g.first_sale_date) if getattr(g, 'first_sale_date', None) else None,
        "last_sale_date": str(g.last_sale_date) if getattr(g, 'last_sale_date', None) else None,
        "upgrade_stars": getattr(g, 'upgrade_stars', None),
        "birthday": getattr(g, 'birthday', False),
        "require_premium": getattr(g, 'require_premium', False),
        "per_user_remains": getattr(g, 'per_user_remains', None)
    }


async def register(sid):
    print('РЕГИСТРАЦИЯ НОВОГО АККАУНТА')
    tg = await get_client_not_started(sid)
    try:
        await tg.connect()
        if not await tg.is_user_authorized():
            qr = await tg.qr_login()
            print("\nОтсканируйте этот QR-код в приложении Telegram:")
            qr_gen = QRCode()
            qr_gen.add_data(qr.url)
            qr_gen.make(fit=True)
            qr_gen.print_ascii(invert=True)
            try:
                await qr.wait()
            except errors.SessionPasswordNeededError:
                print('\n[!] На аккаунте включен облачный пароль (2FA).')
                pw = input('Введите ваш пароль: ')
                await tg.sign_in(password=pw)
            print("Вход выполнен!")
        print('Аккаунт успешно сохранен!')
        input('Нажмите клавишу Enter чтобы вернуться в меню...')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        input('Нажмите клавишу Enter чтобы вернуться в меню...')
    finally:
        await tg.disconnect()

async def nftparse():
    client = await get_client(session_name)
    gifts = await get_all_gifts_not_hidden(client)
    gifts_dict = {g.id: g for g in gifts.gifts}

    async for g_id in tqdm(get_gifts_all_id_array(), desc="Checking Gifts"):
        gift_obj = gifts_dict.get(g_id)
        if gift_obj is None: continue
        title = getattr(gift_obj, 'title', None)
        is_limited = getattr(gift_obj, 'limited', False)
        if title and is_limited: nft_ids.append(g_id)

    await save(path_nft_json, nft_ids)
    await sleep(0.1)
    await client.disconnect()


async def send_gift():
    client = await get_client(session_name)
    your_gift_id = int(input("Введи айди гифта для отправки: "))
    target_username = input("Кому отправить? (введи юзернейм или ID): ")
    try: count = int(input("Сколько штук отправить? "))
    except ValueError:
        print("❌ Ошибка: введите число.")
        return

    if target_username.isdigit(): target_username = int(target_username)

    try:
        print(f"Готовим отправку {count} шт...")
        peer = await client.get_input_entity(target_username)
        invoice = types.InputInvoiceStarGift(hide_name=False, include_upgrade=False, peer=peer, gift_id=your_gift_id, message=types.TextWithEntities(text="", entities=[]))
        for i in range(1, count + 1):
            try:
                form = await payment_request(invoice, client)
                await client(functions.payments.SendStarsFormRequest(form_id=form.form_id, invoice=invoice))
                print(f"✅ [{i}/{count}] Подарок успешно отправлен")
                if i < count: await sleep(1)

            except Exception as e:
                print(f"❌ Ошибка на шаге {i}: {e}")
                break

        await client.disconnect()

    except ValueError: print(f"❌ Ошибка, не получилось найти пользователя {target_username}.")
    except Exception as e: print(f"❌ Появилась ошибка при подготовке: {e}")


async def info_gifts():
    makedirs(folder_json, exist_ok=True)
    available_ids = []
    client = await get_client(session_name)
    peer = await client.get_input_entity('me')
    all_gifts = await get_all_gifts_not_hidden(client)
    gifts_dict = {g.id: g for g in all_gifts.gifts}
    async for g_id in tqdm(get_gifts_all_id_array(), desc="Checking Gifts"):
        gift_obj = gifts_dict.get(g_id)
        if not gift_obj:
            try:
                await payment_request(await get_invoice(peer, g_id), client)
                available_ids.append(g_id)
            except Exception: pass
            finally: await sleep(0.1)
            continue

        stars = getattr(gift_obj, 'stars')
        if stars >= 0: continue
        sold_out = getattr(gift_obj, 'sold_out', False)
        if not sold_out: available_ids.append(g_id)
        await sleep(0.1)

    with open(path_json, "w", encoding="utf-8") as f: dump(available_ids, f, indent=4)
    await client.disconnect()

async def runly():
    client = await get_client(session_name)
    result = await get_all_gifts_not_hidden(client)
    result2 = await get_all_gifts_ids()
    makedirs("ids", exist_ok=True)
    gifts_data = [format_gift(g) for g in result.gifts]
    data_to_save = {"ids": result2}
    await save("ids/api_gifts.json", gifts_data)
    await save("ids/all_gifts.json", data_to_save)
    await client.disconnect()


async def tosgs():
    while True:
        cls()
        print_gradient(tosgs_title)
        print_gradient(tosgs_menu)

        match input(">>> "):
            case "1": await info_gifts()
            case "2": await send_gift()
            case "3": await runly()
            case "4": await nftparse()
            case "5": await register(session_name)
            case "0": break
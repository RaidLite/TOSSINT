from os import system, name
from random import uniform, randint, choices, choice
from string import ascii_lowercase, ascii_letters, punctuation, digits, ascii_uppercase
from faker import Faker
from pystyle import Colors, Colorate, Center
from qrcode import QRCode
from qrcode import constants

fake = Faker()
title = """
 ███████████  █████████     ███████      █████████  █████ ██████████ ███████████ █████ █████
▒▒███▒▒▒▒▒▒█ ███▒▒▒▒▒███  ███▒▒▒▒▒███   ███▒▒▒▒▒███▒▒███ ▒▒███▒▒▒▒▒█▒█▒▒▒███▒▒▒█▒▒███ ▒▒███ 
 ▒███   █ ▒ ▒███    ▒▒▒  ███     ▒▒███ ███     ▒▒▒  ▒███  ▒███  █ ▒ ▒   ▒███  ▒  ▒▒███ ███  
 ▒███████   ▒▒█████████ ▒███      ▒███▒███          ▒███  ▒██████       ▒███      ▒▒█████   
 ▒███▒▒▒█    ▒▒▒▒▒▒▒▒███▒███      ▒███▒███          ▒███  ▒███▒▒█       ▒███       ▒▒███    
 ▒███  ▒     ███    ▒███▒▒███     ███ ▒▒███     ███ ▒███  ▒███ ▒   █    ▒███        ▒███    
 █████      ▒▒█████████  ▒▒▒███████▒   ▒▒█████████  █████ ██████████    █████       █████   
▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒       ▒▒▒▒▒    

                                                                                            """
menu = """
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  1. Password Generation          15. Job Title Generation                         ║
║  2. Number Generation            16. License Number Generation                    ║
║  3. Persona Generation           17. SSN Generation                               ║
║  4. Mullvad Key Generation       18. QR Code Generation                           ║
║  5. Discord Token Generation     19. Coordinates Generation                       ║
║  6. Bank Card Generation         20. Fake News Generation                         ║
║  7. Email Generation             21. Color Palette Generation                     ║
║  8. Date of Birth Generation     22. Custom Password Generation                   ║
║  9. UUID Generation              23. Bitcoin Address Generation                   ║
║ 10. MAC Address Generation       24. Bitcoin Key Generation                       ║
║ 11. Address Generation           25. Stock Generation                             ║
║ 12. Username Generation          26. Medical Portfolio Generation                 ║
║ 13. Quote Generation             27. Passport Data Generation                     ║
║ 14. Company Generation           28. Exit                                         ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
"""

headlines = [
    "Ученые обнаружили новый вид насекомых в Амазонке",
    "Известный актер объявил о своем участии в новом проекте",
    "Исследование показало, что шоколад полезен для здоровья",
    "Новая технология обещает революцию в медицине",
    "Археологи нашли древний артефакт в Египте"
]
bodies = [
    "Сегодня утром команда исследователей сообщила о своем открытии.",
    "Событие вызвало бурную реакцию в социальных сетях.",
    "Эксперты предсказывают значительное влияние на индустрию.",
    "Местные жители выражают свою поддержку.",
    "Новость распространилась с невероятной скоростью."
]

def generate_custom_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = ascii_lowercase
    if use_uppercase: characters += ascii_uppercase
    if use_digits: characters += digits
    if use_symbols: characters += punctuation
    if not characters: raise ValueError("Невозможно создать пароль: не выбраны символы для использования.")
    return ''.join(choice(characters) for _ in range(length))

def prompt_password_criteria(): return generate_custom_password(
    int(input("Введите длину пароля: ")),
    input("Использовать заглавные буквы? (y/n): ").lower() == 'y',
    input("Использовать цифры? (y/n): ").lower() == 'y',
    input("Использовать символы? (y/n): ").lower() == 'y'
)

def generate_password(length=12): return ''.join(choice(ascii_letters + digits + punctuation) for _ in range(length))
def generate_number(country_code): return f"+{country_code} {fake.phone_number()}"
def generate_bitcoin_address(): return fake.cryptocurrency_address()
def print_gradient_text(text): print(Colorate.Vertical(Colors.blue_to_cyan, text))
def generate_bitcoin_private_key(): return ''.join(choice(ascii_letters + digits) for _ in range(64))
def generate_identity(): return fake.name()
def generate_mullvad_key(): return ''.join(choice(ascii_uppercase + digits) for _ in range(16))
def generate_discord_token(): return ''.join(choice(ascii_letters + digits) for _ in range(59))
def generate_credit_card(): return fake.credit_card_number(card_type=None)
def generate_email(): return fake.email()
def generate_birthdate(): return fake.date_of_birth()
def generate_uuid(): return fake.uuid4()
def generate_mac(): return fake.mac_address()
def generate_address(): return fake.address()
def generate_username(): return fake.user_name()
def generate_quote(): return fake.sentence()
def generate_company(): return fake.company()
def generate_job(): return fake.job()
def generate_license_plate(): return fake.license_plate()
def generate_ssn(): return fake.ssn()
def generate_fake_news(): return f"Headline: {choice(headlines)}\nBody: {choice(bodies)}"
def random_color(): return "#{:06x}".format(randint(0, 0xFFFFFF))
def generate_coordinates(): return f"Latitude: {round(uniform(-90.0, 90.0), 6)}, Longitude: {round(uniform(-180.0, 180.0), 6)}"
def generate_color_palette(): return [random_color() for _ in range(5)]

def generate_qr(data):
    qr = QRCode(version=1, error_correction=constants.ERROR_CORRECT_L, box_size=10, border=4, )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img_path = "qrcode.png"
    img.save(img_path)
    return img_path

def generate_stock_profile(): return {
        "company": fake.company(),
        "symbol": ''.join(choices(ascii_uppercase, k=4)),
        "price": round(uniform(10, 1000), 2),
        "volume": randint(1000, 1000000)
}

def generate_medical_profile(): return {
        "name": fake.name(),
        "age": randint(0, 100),
        "blood_type": choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]),
        "conditions": [fake.word() for _ in range(randint(0, 5))]
}

def generate_passport_details(): return {
        "passport_number": ''.join(choices(ascii_uppercase + digits, k=9)),
        "name": fake.name(),
        "nationality": fake.country(),
        "birthdate": fake.date_of_birth(),
        "expiry_date": fake.date_between(start_date="today", end_date="+10y")
}

def print_menu():
    system('cls' if name == 'nt' else 'clear')
    print_gradient_text(Center.XCenter(title))
    print_gradient_text(Center.XCenter(menu))


def gg():
    while True:
        print_menu()
        option = input("Выберите опцию: ")

        match option:
            case '1': print("Сгенерированный пароль:", generate_password())
            case '2':
                country_code = input("Введите код страны: ")
                print("Сгенерированный номер телефона:", generate_number(country_code))
            case '3': print("Сгенерированная личность:", generate_identity())
            case '4': print("Сгенерированный ключ Mullvad:", generate_mullvad_key())
            case '5': print("Сгенерированный токен Discord:", generate_discord_token())
            case '6': print("Сгенерированный номер банковской карты:", generate_credit_card())
            case '7': print("Сгенерированный email:", generate_email())
            case '8': print("Сгенерированная дата рождения:", generate_birthdate())
            case '9': print("Сгенерированный UUID:", generate_uuid())
            case '10': print("Сгенерированный MAC-адрес:", generate_mac())
            case '11': print("Сгенерированный адрес:", generate_address())
            case '12': print("Сгенерированное имя пользователя:", generate_username())
            case '13': print("Сгенерированная цитата:", generate_quote())
            case '14': print("Сгенерированная компания:", generate_company())
            case '15': print("Сгенерированная должность:", generate_job())
            case '16': print("Сгенерированный номер лицензии:", generate_license_plate())
            case '17': print("Сгенерированный SSN:", generate_ssn())
            case '18':
                data = input("Введите данные для QR-кода: ")
                qr_path = generate_qr(data)
                print(f"QR-код сохранен как {qr_path}")
            case '19': print("Сгенерированные координаты:", generate_coordinates())
            case '20': print("Сгенерированные фальшивые новости:", generate_fake_news())
            case '21': print("Сгенерированная цветовая палитра:", generate_color_palette())
            case '22': print("Сгенерированный пользовательский пароль:", prompt_password_criteria())
            case '23': print("Сгенерированный Bitcoin-адрес:", generate_bitcoin_address())
            case '24': print("Сгенерированный Bitcoin-ключ:", generate_bitcoin_private_key())
            case '25': print("Сгенерированный профиль акции:", generate_stock_profile())
            case '26': print("Сгенерированное медицинское портфолио:", generate_medical_profile())
            case '27': print("Сгенерированные паспортные данные:", generate_passport_details())
            case '28':
                print("Выход")
                break
            case _: print("Неверная опция. Пожалуйста, выберите снова.")

        input("Нажмите Enter для продолжения...")
from random import uniform, randint, choices, choice
from string import ascii_lowercase, ascii_letters, punctuation, digits, ascii_uppercase
from faker import Faker
from pystyle import Center
from qrcode import QRCode
from qrcode import constants
from o.t.settings import title, headlines, bodies, menu
from o.t.utils import cls
from o.t.utils import print_gradient as print_gradient_text

fake = Faker()

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

get_characters = lambda s: (ascii_letters + digits) + ("!@#$%^&*()qwertyuiopasdfghjklzxcvbnm,./;[]йцукенгшщзхъфывапролдячсмить" if s == "medium" else punctuation if s == "high" else "")
def gen_pass(n, s): return ''.join(choice(get_characters(s)) for _ in range(n))
def generate_password(length=12): return ''.join(choice(ascii_letters + digits + punctuation) for _ in range(length))
def generate_number(country_code): return f"+{country_code} {fake.phone_number()}"
def generate_bitcoin_address(): return fake.cryptocurrency_address()
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
    cls()
    print_gradient_text(Center.XCenter(title))
    print_gradient_text(Center.XCenter(menu))

def generate_random_person(gender=None):
    fake = Faker(locale="ru_RU")
    if gender is None:
        gender = choice(["М", "Ж"])
    if gender == "М":
        first_name = fake.first_name_male()
        middle_name = fake.middle_name_male()
    else:
        first_name = fake.first_name_female()
        middle_name = fake.middle_name_female()
    last_name = fake.last_name()
    full_name = f"{last_name} {first_name} {middle_name}"
    birthdate = fake.date_of_birth()
    age = fake.random_int(min=18, max=80)
    street_address = fake.street_address()
    city = fake.city()
    region = fake.region()
    postcode = fake.postcode()
    address = f"{street_address}, {city}, {region} {postcode}"
    email = fake.email()
    phone_number = fake.phone_number()
    inn = str(fake.random_number(digits=12, fix_len=True))
    snils = str(fake.random_number(digits=11, fix_len=True))
    passport_num = str(fake.random_number(digits=10, fix_len=True))
    passport_series = fake.random_int(min=1000, max=9999)
    return {
        "ФИО": full_name,
        "Пол": gender,
        "Дата рождения": birthdate.strftime('%d %B %Y'),
        "Возраст": age,
        "Адрес": address,
        "Email": email,
        "Телефон": phone_number,
        "ИНН": inn,
        "СНИЛС": snils,
        "Паспорт": f"{passport_series} {passport_num}"
    }


def generate_checksum(n):
    d = list(map(int, n))
    s = sum(d[-2::-2]) + sum(sum(divmod(x*2, 10)) for x in d[-1::-2])
    return (10 - s % 10) % 10


def generate_card_number():
    n = "4" + ''.join(str(randint(0,9)) for _ in range(14))
    return n + str(generate_checksum(n))


def generate_card(country="Россия"):
    m, y = randint(1,12), randint(24,30)
    return {
        "Страна": country,
        "Номер карты": generate_card_number(),
        "Срок действия": f"{m:02d}/{y:02d}",
        "CVV": ''.join(str(randint(0,9)) for _ in range(3))
    }


def generate_phone_number(c):
    return {
        "1": f"+1 {randint(200,999)}-{randint(200,999)}-{randint(1000,9999)}",
        "2": f"+7 {randint(900,999)} {randint(100,999)}-{randint(10,99)}-{randint(10,99)}",
        "3": f"+7 {randint(700,709)} {randint(100,999)}-{randint(10,99)}-{randint(10,99)}",
        "4": f"+375 {randint(25,33)} {randint(100,999)}-{randint(100,999)}",
        "5": f"+234 {randint(700,799)} {randint(100,999)}-{randint(1000,9999)}"
    }.get(c)

def generate_qr_code():
    data = input("Enter the data to encode in the QR code: ")
    qr = QRCode(version=1, error_correction=constants.ERROR_CORRECT_L, box_size=10, border=4,)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    file_path = "qrcode.png"
    img.save(file_path)
    print(f"QR code saved as {file_path}")
    input("Press Enter to return to the menu...")



def gg():
    while True:
        print_menu()
        match input("---> "):
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
            case '28': break
            case _: print("Неверная опция. Пожалуйста, выберите снова.")

        input("Нажмите Enter для продолжения...")
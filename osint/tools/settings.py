api_id = 21341528
api_hash = "bf654fd64259c65b85c8899ff081a437"
session_name = 'tosgs'
folder_json = 'found'
path_json = f'{folder_json}/ids.json'
path_nft_json = f'{folder_json}/nft_ids.json'
url = 'https://cdn.changes.tg/gifts/originals/'
nft_ids = []
tosgs_menu = """
1. Parser
2. Send Gift
3. Utility
4. NFT Parsing
5. Register
0. Leave

"""
links = {
    "raw.githubusercontent.com/srusahi/femoz/e44adac46e8a2f4d38c974cee092671700844f82/Base/God_eye_basedata.txt",
    "raw.githubusercontent.com/Karen-HUB-git/STRANGER_PRIVATE2/2af0f86f29037bf9abbe3b130a5c988d8ebe3f70/PAS1k.txt",
    "github.com/shikso81/honkai/raw/eb2fe07682823684c200ac14acf3384175dcb840/NatHack/database/QiWi.csv",
    "github.com/shikso81/honkai/raw/eb2fe07682823684c200ac14acf3384175dcb840/NatHack/database/russol.info.csv",
    "drive.google.com/drive/folders/1YZYHUV3f8sgW6PQOqjCWmNWvKIxC5u0D"
}

translit_dict = {
    "а": "@", "б": "Б", "в": "B", "г": "г", "д": "д", "е": "е", "ё": "ё", "ж": "ж", "з": "3", "и": "u",
    "й": "й", "к": "K", "л": "л", "м": "M", "н": "H", "о": "0", "п": "п", "р": "P", "с": "c", "т": "T",
    "у": "y", "ф": "ф", "х": "X", "ц": "ц", "ч": "4", "ш": "ш", "щ": "щ", "ъ": "ъ", "ы": "ы", "ь": "ь",
    "э": "э", "ю": "ю", "я": "я", "А": "A", "Б": "6", "В": "V", "Г": "r", "Д": "D", "Е": "E", "Ё": "Ё",
    "Ж": "Ж", "З": "2", "И": "I", "Й": "Й", "К": "K", "Л": "Л", "М": "M", "Н": "H", "О": "O", "П": "П",
    "Р": "P", "С": "C", "Т": "T", "У": "Y", "Ф": "Ф", "Х": "X", "Ц": "Ц", "Ч": "Ч", "Ш": "Ш", "Щ": "Щ",
    "Ъ": "Ъ", "Ы": "bl", "Ь": "b", "Э": "Э", "Ю": "9Y", "Я": "9A",
}

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

tosgs_title = title
fsociety_title = title

variants = """
╔══════════════════════════════════════════════════════════════════════════════════════╗
║ 1. DNS Lookup             12. GitHub parsing          24. Generate phone             ║
║ 3. IP Lookup              13. Download video YT       25. Get Databases              ║
║ 4. Image Metadata         14. Generated QR            26. Phone Full Info            ║
║ 5. Data Breach Lookup     15. Internet speedtest      27. Phone Validator            ║
║ 6. Port Scan              16. Generate password       28. Phone Formatter            ║
║ 7. URL Avail. Check       17. Transform text          29. Phone Geo/Carrier          ║
║ 8. SSL Cert Check         18. Scan single port        30. Extract Phones             ║
║ 9. HTTP Headers           19. Get proxy list          31. Phone Examples             ║
║ 10. Response Time         20. MAC lookup              32. Supported Regions          ║
║ 11. HTML Parsing          21. Crawl website           33. Generator Tool             ║
║ 36. Search by nickname    22. Generate person         34. Telegram Gift Parser       ║
║ 37. Search by mail        23. Generate card           35. Search by nickname v2      ║
║══════════════════════════════════════════════════════════════════════════════════════║
║                                 0. Leave                                             ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
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
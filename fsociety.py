import asyncio
import sys
from itertools import zip_longest
from os import name, system
from fakegen import gg
from logic import *
from numb import *
from search import check_username
from tosgs import tosgs

color = Colors.blue_to_cyan
fsociety_title = """
 ███████████  █████████     ███████      █████████  █████ ██████████ ███████████ █████ █████
▒▒███▒▒▒▒▒▒█ ███▒▒▒▒▒███  ███▒▒▒▒▒███   ███▒▒▒▒▒███▒▒███ ▒▒███▒▒▒▒▒█▒█▒▒▒███▒▒▒█▒▒███ ▒▒███ 
 ▒███   █ ▒ ▒███    ▒▒▒  ███     ▒▒███ ███     ▒▒▒  ▒███  ▒███  █ ▒ ▒   ▒███  ▒  ▒▒███ ███  
 ▒███████   ▒▒█████████ ▒███      ▒███▒███          ▒███  ▒██████       ▒███      ▒▒█████   
 ▒███▒▒▒█    ▒▒▒▒▒▒▒▒███▒███      ▒███▒███          ▒███  ▒███▒▒█       ▒███       ▒▒███    
 ▒███  ▒     ███    ▒███▒▒███     ███ ▒▒███     ███ ▒███  ▒███ ▒   █    ▒███        ▒███    
 █████      ▒▒█████████  ▒▒▒███████▒   ▒▒█████████  █████ ██████████    █████       █████   
▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒       ▒▒▒▒▒    
                                                                                            
                                                                                            """
dnint = [
    "--- DNINT",
    "1. DNS Lookup",
    "3. IP Lookup",
    "6. Port Scan",
    "18. Scan single port",
    "19. Get proxy list",
    "20. MAC lookup",
]

web = ["--- Web analytics",
       "7. URL Availability Check",
       "8. SSL Certificate Check",
       "9. HTTP Headers Extraction",
       "10. Server Response Time Check",
       "11. HTML Parsing",
       "21. Crawl website"]

telint = [
    "--- TELINT",
    "26. Phone Full Info",
    "27. Phone Validator",
    "28. Phone Formatter",
    "29. Phone Geo/Carrier",
    "30. Extract Phones from Text"
]

data_breaches = [
    "--- Data Breaches",
    "4. Image Metadata",
    "5. Data Breach Lookup",
    "25. Get Databases"
]

socmint = ["--- SOCMINT",
           "12. GitHub repository parsing",
           "13. Download video Youtube"
]

other = ["--- OTHER",
         "q. Leave",
         "14. Generated QR",
         "15. Internet speedtest",
         "16. Generate password",
         "17. Transform text",
         "22. Generate person",
         "23. Generate card",
         "24. Generate phone",
         "31. Phone Examples",
         "32. Supported Regions",
         "33. Generator Tool",
         "34. Telegram Gift Parser",
         "35. Search by nickname"
]


def print_table(*columns):
    widths = [max(len(str(item)) for item in col) for col in columns]
    for row_data in zip_longest(*columns, fillvalue=""):
        formatted_row = []
        for i, item in enumerate(row_data):
            cell = str(item).ljust(widths[i])
            formatted_row.append(cell)

        text = f" {f' |  '.join(formatted_row) + ' '} "
        print(Colorate.Horizontal(color, text))


def main():
    system('cls' if name == 'nt' else 'clear')
    print(Colorate.Vertical(color, fsociety_title))
    print()
    print_table(
        dnint,
        web,
        telint,
        data_breaches,
        socmint,
        other
    )
    print()
    match input("Enter your choice: ").strip():
        case 'q': print("Exiting the program."); sys.exit(0)
        case '1': dns_lookup(input("Enter domain for DNS lookup: "))
        case '3': ip_lookup(input("Enter IP for IP lookup: "))
        case '4': image_metadata(input("Enter path to image for metadata extraction: "))
        case '5': data_breach_lookup(input("Enter email for data breach lookup: "))
        case '6': port_scan(input("Enter IP for port scan: "))
        case '7': url_availability_check(input("Enter URL for availability check: "))
        case '8': ssl_certificate_check(input("Enter URL for SSL certificate check: "))
        case '9': http_headers_extraction(input("Enter URL for HTTP headers extraction: "))
        case '10': server_response_time_check(input("Enter URL for server response time check: "))
        case '11': html_parser(input("Enter URL for HTML parsing: "))
        case '12': github_repo_parser(input("Enter GitHub repository URL: "))
        case '13': download_youtube_video(input("Enter YouTube video URL: "))
        case '14': generate_qr_code()
        case '15': check_internet_speed()
        case '16': print(generate_password(int(input("Password length: ")), input("Strength (low/medium/high): ")))
        case '17': print(transform_text(input("Enter text: ")))
        case '18': print("Open" if s_port(input("Enter port: "), input("Enter host (default 127.0.0.1): ") or "127.0.0.1") else "Closed")
        case '25': getdb()
        case '33': gg()
        case '34': asyncio.run(tosgs())
        case '20': print(mac_lookup(input("Enter MAC address: ")))
        case '21': print("\n".join(crawl_website(input("Enter start URL: "))[:20]))
        case '35':
            result = asyncio.run(check_username(input("Username --> "), 500))
            print(Colorate.Horizontal(color, result))

        case '19':
            proxies = get_proxy_list()
            print("\n".join(proxies[:10]) if isinstance(proxies, list) else proxies)

        case '22':
            gender = input("Gender (М/Ж or empty): ") or None
            person = generate_random_person(gender)
            for k, v in person.items(): print(f"{k}: {v}")

        case '23':
            for k, v in generate_card().items(): print(f"{k}: {v}")

        case '24': print(generate_phone_number(input("Country code (1-5): ")))
        case '26':
            num = input("Number: ")
            p = parse_safe(num)
            if p: print(info(p))

        case '27':
            num = input("Number: ")
            reg = input("Region: ") or None
            p = parse_safe(num, reg)
            if p:
                print(f"Valid: {is_valid(p)}")
                print(f"Possible: {is_possible(p)}")
                print(f"Emergency: {is_emergency(num, reg or 'US')}")

        case '28':
            num = input("Number: ")
            p = parse_safe(num)
            if p:
                print(f"E164: {format_e164(p)}")
                print(f"Int: {format_international(p)}")
                print(f"Nat: {format_national(p)}")
                print(f"RFC: {format_rfc3966(p)}")

        case '29':
            num = input("Number: ")
            p = parse_safe(num)
            if p:
                print(f"Region: {get_region(p)}")
                print(f"Type: {type_name(p)}")
                print(f"Geo: {is_geographical(p)}")
                print(f"Carrier: {is_carrier_specific(p)}")

        case '30':
            text = input("Text: ")
            reg = input("Default Region: ")
            print(find_numbers_e164(text, reg))

        case '31':
            reg = input("Region: ")
            ex = get_example_number(reg)
            if ex: print(format_international(ex))

        case '32':
            print(f"Regions: {get_supported_regions()}")
            print(f"Codes: {get_supported_calling_codes()}")

        case _: print("Invalid choice. Please select a valid option.")

    input("Press Enter to continue...")


if __name__ == "__main__":
    while True: main()
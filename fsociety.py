import asyncio
import sys
from itertools import zip_longest

import tosu
from fakegen import gg
from logic import *
from numb import *
from tosgs import tosgs

color = Colors.blue_to_cyan

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
           "13. Download video Youtube"]

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
         "35. Telegram UserBot"
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(color, """
 ███████████  █████████     ███████      █████████  █████ ██████████ ███████████ █████ █████
▒▒███▒▒▒▒▒▒█ ███▒▒▒▒▒███  ███▒▒▒▒▒███   ███▒▒▒▒▒███▒▒███ ▒▒███▒▒▒▒▒█▒█▒▒▒███▒▒▒█▒▒███ ▒▒███ 
 ▒███   █ ▒ ▒███    ▒▒▒  ███     ▒▒███ ███     ▒▒▒  ▒███  ▒███  █ ▒ ▒   ▒███  ▒  ▒▒███ ███  
 ▒███████   ▒▒█████████ ▒███      ▒███▒███          ▒███  ▒██████       ▒███      ▒▒█████   
 ▒███▒▒▒█    ▒▒▒▒▒▒▒▒███▒███      ▒███▒███          ▒███  ▒███▒▒█       ▒███       ▒▒███    
 ▒███  ▒     ███    ▒███▒▒███     ███ ▒▒███     ███ ▒███  ▒███ ▒   █    ▒███        ▒███    
 █████      ▒▒█████████  ▒▒▒███████▒   ▒▒█████████  █████ ██████████    █████       █████   
▒▒▒▒▒        ▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒       ▒▒▒▒▒    
                                                                                            
                                                                                            """))
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
    choice = input("Enter your choice: ").strip()

    match choice:
        case 'q':
            print("Exiting the program.")
            sys.exit(0)

        case '1':
            domain = input("Enter domain for DNS lookup: ")
            dns_lookup(domain)

        case '3':
            ip = input("Enter IP for IP lookup: ")
            ip_lookup(ip)

        case '4':
            image_path = input("Enter path to image for metadata extraction: ")
            image_metadata(image_path)

        case '5':
            email = input("Enter email for data breach lookup: ")
            data_breach_lookup(email)

        case '6':
            ip = input("Enter IP for port scan: ")
            port_scan(ip)

        case '7':
            url = input("Enter URL for availability check: ")
            url_availability_check(url)

        case '8':
            url = input("Enter URL for SSL certificate check: ")
            ssl_certificate_check(url)

        case '9':
            url = input("Enter URL for HTTP headers extraction: ")
            http_headers_extraction(url)

        case '10':
            url = input("Enter URL for server response time check: ")
            server_response_time_check(url)

        case '11':
            url = input("Enter URL for HTML parsing: ")
            html_parser(url)

        case '12':
            repo_url = input("Enter GitHub repository URL: ")
            github_repo_parser(repo_url)

        case '13':
            url = input("Enter YouTube video URL: ")
            download_youtube_video(url)

        case '14':
            generate_qr_code()
        case '15':
            check_internet_speed()
        case '16':
            length = int(input("Password length: "))
            strength = input("Strength (low/medium/high): ")
            print(generate_password(length, strength))

        case '17':
            text = input("Enter text: ")
            print(transform_text(text))

        case '18':
            host = input("Enter host (default 127.0.0.1): ") or "127.0.0.1"
            port = input("Enter port: ")
            print("Open" if scan_port(port, host) else "Closed")

        case '19':
            proxies = get_proxy_list()
            print("\n".join(proxies[:10]) if isinstance(proxies, list) else proxies)

        case '20':
            mac = input("Enter MAC address: ")
            print(mac_lookup(mac))

        case '21':
            url = input("Enter start URL: ")
            results = crawl_website(url)
            print("\n".join(results[:20]))

        case '22':
            gender = input("Gender (М/Ж or empty): ") or None
            person = generate_random_person(gender)
            for k, v in person.items():
                print(f"{k}: {v}")

        case '23':
            card = generate_card()
            for k, v in card.items():
                print(f"{k}: {v}")

        case '24':
            code = input("Country code (1-5): ")
            print(generate_phone_number(code))
        case '25':
            getdb()
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

        case '33':
            gg()

        case '34':
            asyncio.run(tosgs())

        case '35':
            asyncio.run(tosu.userbot())

        case _:
            print("Invalid choice. Please select a valid option.")

    input("Press Enter to continue...")


if __name__ == "__main__":
    while True:
        main()

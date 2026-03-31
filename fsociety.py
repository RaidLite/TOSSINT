import asyncio
import sys
from os import name, system

from pystyle import Center

from fakegen import gg, print_gradient_text
from logic import *
from numb import *
from search import check_username, run_sherlock, run_holehe
from tosgs import tosgs

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
dnint = """
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

def main():
    system('cls' if name == 'nt' else 'clear')
    print_gradient_text(Center.XCenter(fsociety_title))
    print_gradient_text(Center.XCenter(dnint))
    print()
    match input("---> ").strip():
        case '0': print("Exiting the program."); sys.exit(0)
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
            print(Colorate.Horizontal(Colors.blue_to_cyan, result))

        case '36':
            nickname = input("Nickname: ")
            data = run_sherlock(nickname)

            if "error" in data:
                result = f"[-] Error for {nickname}: {data['error']}"
            else:
                found_count = data["data"]["found_count"]
                accounts = data["data"]["accounts"]

                if found_count > 0:
                    header = f"[*] Results for '{nickname}' ({found_count} found):\n"
                    links = "\n".join([f" > {site}: {url}" for site, url in accounts.items()])
                    result = header + links
                else:
                    result = f"[-] No accounts found for '{nickname}'."

            print(Colorate.Horizontal(Colors.blue_to_cyan, result))

        case '37':
            email = input("Email: ")
            data = run_holehe(email)

            if "error" in data:
                result = f"[-] Error: {data['error']}"
            else:
                found = data["data"]["found"]
                limited = data["data"]["rate_limited"]

                if found:
                    res_list = [f" > {i['service']}" +
                                (f" ({i['recovery'] or i['phone']})" if i['recovery'] or i['phone'] else "")
                                for i in found]
                    result = f"[*] Found {len(found)} accounts for {email}:\n" + "\n".join(res_list)
                    if limited:
                        result += f"\n[!] Rate Limit: {', '.join(limited)}"
                else:
                    result = f"[-] No data for {email}."

            print(Colorate.Horizontal(Colors.blue_to_cyan, result))


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
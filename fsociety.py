from asyncio import run
from sys import exit

from pystyle import Center, Colorate, Colors

from tools.dnint import dns_lookup, ip_lookup, image_metadata, data_breach_lookup, port_scan, url_availability_check, \
    ssl_certificate_check, http_headers_extraction, server_response_time_check, html_parser, github_repo_parser, \
    download_youtube_video, transform_text, check_internet_speed, getdb, s_port, mac_lookup, crawl_website, \
    get_proxy_list
from tools.emailint import run_holehe
from tools.humint import humint_manual
from tools.socmint import check_username, run_sherlock
from tools.utils.gen import generate_qr_code, gen_pass, generate_random_person, generate_card, generate_phone_number
from tools.utils.gen import gg, print_gradient_text
from tools.utils.manuals import manual
from tools.utils.numbers import parse_safe, get_example_number, is_possible, type_name, get_supported_regions, \
    is_geographical, is_carrier_specific, format_e164, format_international, format_national, format_rfc3966, \
    find_numbers_e164, info, get_supported_calling_codes, is_valid, is_emergency, get_region
from tools.utils.settings import fsociety_title, variants
from tools.utils.utils import cls

def main():
    cls()
    print_gradient_text(Center.XCenter(fsociety_title))
    print_gradient_text(Center.XCenter(variants))
    print()
    match input("---> ").strip():
        case '0': print("Exiting the program."); exit(0)
        case '1': dns_lookup(input("Enter domain for DNS lookup: "))
        case '2': humint_manual()
        case '3': ip_lookup(input("Enter IP for IP lookup: "))
        case '34': image_metadata(input("Enter path to image for metadata extraction: "))
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
        case '16': print(gen_pass(int(input("Password length: ")), input("Strength (low/medium/high): ")))
        case '17': print(transform_text(input("Enter text: ")))
        case '18': print("Open" if s_port(input("Enter port: "), input("Enter host (default 127.0.0.1): ") or "127.0.0.1") else "Closed")
        case '25': getdb()
        case '33': gg()
        case '20': print(mac_lookup(input("Enter MAC address: ")))
        case '21': print("\n".join(crawl_website(input("Enter start URL: "))[:20]))
        case '35':
            result = run(check_username(input("Username --> "), 500))
            print(Colorate.Horizontal(Colors.red_to_yellow, result))

        case '36':
            nickname = input("Nickname: ")
            data = run_sherlock(nickname)
            if "error" in data: result = f"[-] Error for {nickname}: {data['error']}"
            else:
                found_count = data["data"]["found_count"]
                accounts = data["data"]["accounts"]
                if found_count > 0:
                    header = f"[*] Results for '{nickname}' ({found_count} found):\n"
                    links = "\n".join([f" > {site}: {url}" for site, url in accounts.items()])
                    result = header + links
                else: result = f"[-] No accounts found for '{nickname}'."
            print(Colorate.Horizontal(Colors.red_to_yellow, result))

        case '37':
            email = input("Email: ")
            data = run_holehe(email)
            if "error" in data: result = f"[-] Error: {data['error']}"
            elif not data.get("data", {}).get("found"): result = f"[-] No data for {email}."
            else:
                found = data["data"]["found"]
                limited = data.get("data", {}).get("rate_limited", [])
                lines = [f"[*] Found {len(found)} accounts for {email}:"]
                for i in found:
                    extra = i.get('recovery') or i.get('phone')
                    iii = f" ({extra})" if extra else ""
                    lines.append(f" > {i['service']}{iii}")
                if limited: lines.append(f"\n[!] Rate Limit: {', '.join(limited)}")
                result = "\n".join(lines)
            print(Colorate.Horizontal(Colors.red_to_yellow, result))

        case '19':
            proxies = get_proxy_list()
            print_gradient_text("\n".join(proxies) if isinstance(proxies, list) else proxies)

        case '22':
            gender = input("Gender (М/Ж or empty): ") or None
            person = generate_random_person(gender)
            for k, v in person.items(): print_gradient_text(f"{k}: {v}")

        case '23':
            for k, v in generate_card().items(): print(f"{k}: {v}")

        case '24':
            print(generate_phone_number(input("Country code (1-5): ")))
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

        case '38': run(manual())
        case _: print("Invalid choice. Please select a valid option.")

    input("Press Enter to continue...")

if __name__ == "__main__":
    while True: main()

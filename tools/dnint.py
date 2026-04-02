import socket
from datetime import datetime
from hashlib import md5
from os import path, getcwd, makedirs, listdir
from random import choice
from re import sub
from socket import socket, AF_INET, SOCK_STREAM
from ssl import get_server_certificate
from time import sleep, time
from urllib import parse

from OpenSSL import crypto
from PIL import Image
from PIL.ExifTags import TAGS
from bs4 import BeautifulSoup
from dns.resolver import Resolver, NXDOMAIN
from pystyle import Colors, Colorate
from pytube import YouTube
from requests import head, ConnectionError, RequestException, exceptions, get
from speedtest import Speedtest
from tools.utils.settings import translit_dict, links

def sanitize_filename(filename): return sub(r'[\\/*?:"<>|]', "_", filename)
def transform_text(t): return ''.join(translit_dict.get(c, c) for c in t)
def getdb(): print("Your databases:"); print(*[f"- {l}" for l in links], sep="\n")

def dns_lookup(domain):
    resolver = Resolver(configure=False)
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']
    try:
        result = resolver.resolve(domain, 'A')
        print(f"IP addresses for {domain}:")
        for ipval in result: print(f" - {ipval.to_text()}")
    except NXDOMAIN:
        print(f"Could not resolve {domain}")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to return to the menu...")


def ip_lookup(ip):
    try:
        r = get(f"https://ipinfo.io/{ip}/json")
        if r.status_code == 200:
            d = r.json()
            for k in ("ip","hostname","city","region","country","loc","org","postal","timezone"):
                print(f"{k.capitalize()}: {d.get(k,'N/A')}")
        else:
            print(f"Error: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"IP lookup failed for {ip}: {e}")
    input("Press Enter to return to the menu...")


def image_metadata(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image.getexif()

        if not exif_data:
            print(f"No EXIF metadata found in {image_path}")
            input("Press Enter to return to the menu...")
            return

        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            if isinstance(value, bytes):
                try:
                    value = value.decode()
                except UnicodeDecodeError:
                    value = value.hex()
            print(f"{tag_name}: {value}")

    except Exception as e:
        print(f"Failed to extract metadata from {image_path}: {e}")
    input("Press Enter to return to the menu...")


def data_breach_lookup(email):
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {"hibp-api-key": "YOUR_API_KEY"}
        response = get(url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            if breaches:
                print(f"Breaches found for {email}:")
                for breach in breaches:
                    print(f"Name: {breach['Name']}, Domain: {breach['Domain']}, BreachDate: {breach['BreachDate']}")
            else:
                print(f"No breaches found for {email}.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Data breach lookup failed for {email}: {e}")
    input("Press Enter to return to the menu...")


def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(1)
    try: return s.connect_ex((ip, port)) == 0
    finally: s.close()


def port_scan(ip):
    print(Colorate.Horizontal(Colors.green_to_white,
          f"Scanning {ip} for open ports (expected time ~2 minutes)..."))

    start = datetime.now()
    open_ports = [p for p in range(1, 1025) if s_port(ip, str(p))]
    duration = datetime.now() - start

    print(Colorate.Horizontal(Colors.green_to_white,
          f"\nScan completed in {duration}\n"))

    if open_ports:
        print(Colorate.Horizontal(Colors.green_to_white, "Open ports:"))

        lines = "\n".join(f"Port {p} is open" for p in open_ports)
        print(Colorate.Horizontal(Colors.green_to_white, lines))
    else:
        print(Colorate.Horizontal(Colors.green_to_white, "No open ports found"))

    input(Colorate.Horizontal(Colors.green_to_white, "\nPress Enter to return to the menu..."))

def url_availability_check(url):
    try:
        r = get(url)
        print(f"The URL {url} is reachable." if r.status_code == 200
              else f"The URL {url} is not reachable. Status code: {r.status_code}")
    except ConnectionError: print(f"The URL {url} is not reachable. Failed to establish a connection.")
    input("Press Enter to return to the menu...")


def ssl_certificate_check(url):
    try:
        cert_pem = get_server_certificate((url, 443))
        x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert_pem.encode())

        subject = dict(
            (k.decode(), v.decode())
            for k, v in x509.get_subject().get_components()
        )
        issuer = dict(
            (k.decode(), v.decode())
            for k, v in x509.get_issuer().get_components()
        )

        valid_from = datetime.strptime(
            x509.get_notBefore().decode(), "%Y%m%d%H%M%SZ"
        )
        valid_until = datetime.strptime(
            x509.get_notAfter().decode(), "%Y%m%d%H%M%SZ"
        )

        print(f"Subject: {subject}")
        print(f"Issuer: {issuer}")
        print(f"Valid from: {valid_from}")
        print(f"Valid until: {valid_until}")
        print(f"Expired: {x509.has_expired()}")

    except Exception as e:
        print(f"Failed to retrieve SSL certificate for {url}: {e}")

    input("Press Enter to return to the menu...")


def http_headers_extraction(url):
    try:
        response = head(url)
        print(f"HTTP headers for {url}:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Failed to retrieve HTTP headers for {url}: {e}")
    input("Press Enter to return to the menu...")


def server_response_time_check(url):
    try:
        start_time = time()
        end_time = time()
        response_time = end_time - start_time
        print(f"Server response time for {url}: {response_time} seconds")
    except Exception as e:
        print(f"Failed to measure server response time for {url}: {e}")
    input("Press Enter to return to the menu...")

def html_parser(url):
    max_retries = 3
    retry_delay = 5

    for attempt in range(max_retries):
        try:
            response = get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            file_name = sanitize_filename(
                f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}.html"
            )

            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(soup.prettify())

            print(f"HTML content saved to {file_name}")
            break

        except exceptions.Timeout:
            print(f"Failed to parse HTML for {url}: Request timed out.")

        except exceptions.HTTPError as e:
            status_code = e.response.status_code if e.response else None

            if status_code == 429:
                if attempt < max_retries - 1:
                    print(f"Failed to parse HTML for {url}: {e}. Retrying in {retry_delay} seconds...")
                    sleep(retry_delay)
                else:
                    print(f"Failed to parse HTML for {url}: {e}. Max retries reached.")
            else:
                print(f"Failed to parse HTML for {url}: {e}")
                break

        except exceptions.RequestException as e:
            print(f"Failed to parse HTML for {url}: {e}")
            break

        except OSError as e:
            print(f"Failed to save HTML for {url}: {e}")
            break

    input("Press Enter to return to the menu...")


def github_repo_parser(url):
    try:

        repo_api_url = url.replace("github.com", "api.github.com/repos")
        response = get(repo_api_url, timeout=10)
        response.raise_for_status()
        repo_info = response.json()

        repo_name = repo_info.get('name', 'Unknown')
        repo_owner = repo_info.get('owner', {}).get('login', 'Unknown')
        repo_description = repo_info.get('description', 'No description')
        repo_language = repo_info.get('language', 'No language specified')
        repo_stars = repo_info.get('stargazers_count', 0)
        repo_forks = repo_info.get('forks_count', 0)
        repo_update_date = repo_info.get('updated_at', 'No update date')

        repo_info_content = (
            f"Repository Name: {repo_name}\n"
            f"Owner: {repo_owner}\n"
            f"Description: {repo_description}\n"
            f"Language: {repo_language}\n"
            f"Stars: {repo_stars}\n"
            f"Forks: {repo_forks}\n"
            f"Last Updated: {repo_update_date}\n"
        )

        repo_info_file_name = f"{repo_name}_repo_info.txt"
        with open(repo_info_file_name, 'w', encoding='utf-8') as file:
            file.write(repo_info_content)

        print(f"Repository information saved to {repo_info_file_name}")

        contents_api_url = f"{repo_api_url}/contents"
        response = get(contents_api_url, timeout=10)
        response.raise_for_status()
        contents = response.json()

        local_dir = repo_name
        if not path.exists(local_dir):
            makedirs(local_dir)

        for content in contents:
            if content['type'] == 'file':
                file_url = content['download_url']
                file_path = path.join(local_dir, content['name'])
                file_response = get(file_url, timeout=10)
                with open(file_path, 'wb') as file:
                    file.write(file_response.content)
                print(f"Saved {content['name']} to {file_path}")

    except RequestException as e:
        print(f"Failed to retrieve repository information for {url}: {e}")
    except Exception as e:
        print(f"Failed to parse repository information for {url}: {e}")
    input("Press Enter to return to the menu...")


def get_file_hash(file_path):
    hash_md5 = md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def choose_file_from_directory():
    current_directory = getcwd()
    files = [f for f in listdir(current_directory) if path.isfile(path.join(current_directory, f))]
    if not files:
        print("В текущем каталоге не найдено файлов.")
        return None

    print("Файлы в текущем каталоге:")
    for idx, file in enumerate(files, 1):
        print(f"[{idx}] {file}")

    while True:
        try:
            choice = int(input("Введите номер файла для сканирования: "))
            if 1 <= choice <= len(files):
                return path.join(current_directory, files[choice - 1])
            else:
                print("Неверный выбор. Пожалуйста, введите номер из списка.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите корректное число.")


def check_internet_speed():
    st = Speedtest()
    st.download()
    st.upload()
    st.results.share()
    results = st.results.dict()
    print(f"Download speed: {results['download'] / 1_000_000:.2f} Mbps")
    print(f"Upload speed: {results['upload'] / 1_000_000:.2f} Mbps")
    print(f"Ping: {results['ping']} ms")
    input("Press Enter to return to the menu...")


def download_youtube_video(url):
    try:
        yt = YouTube(url)
        print(f"Downloading: {yt.title}")
        yt.streams.get_highest_resolution().download()
        print("Download completed.")
    except Exception as e: print(f"An error occurred: {e}")


def s_port(p, host="127.0.0.1"):
    s = socket(AF_INET, SOCK_STREAM)
    ok = s.connect_ex((host, int(p))) == 0
    s.close()
    return ok


def get_proxy_list():
    try:
        r = get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
        return r.text.strip().split("\r\n") if r.status_code == 200 else f"Ошибка: {r.status_code}"
    except Exception as e: return f"Ошибка: {e}"


def mac_lookup(mac):
    try:
        r = get(f"https://api.macvendors.com/{mac}")
        return r.text.strip() if r.status_code == 200 else f"Error: {r.status_code}"
    except Exception as e: return f"Error: {e}"


def send_request(url, agents, i):
    try:
        r = get(url, headers={"User-Agent": choice(agents)})
        return f"Request {i} OK: {r.status_code}"
    except Exception as e: return f"Request {i} failed: {e}"


def crawl_website(start_url, max_depth=2):
    visited = set()
    results = []

    def crawl(url, depth=0):
        if depth > max_depth or url in visited:
            return
        parsed = parse.urlparse(url)
        domain = f"{parsed.scheme}://{parsed.netloc}"
        visited.add(url)
        results.append(url)
        try:
            response = get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a"):
                href = link.get("href")
                if not href:
                    continue
                href = href.split("#")[0].rstrip("/")
                if href.startswith("http"):
                    href_parsed = parse.urlparse(href)
                    if href_parsed.netloc != parsed.netloc:
                        continue
                else:
                    href = domain + href
                crawl(href, depth + 1)
        except Exception as e:
            results.append(f"Error with {url}: {e}")

    crawl(start_url)
    return results
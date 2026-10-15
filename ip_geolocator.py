import requests

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

BANNER = r"""
  ________  .__               .___        
 /  _____/  |__|  ____        |   |______  
/   \  ___  |  | /    \  ______ |   |\____ \ 
\    \_\  \ |  ||   |  \/_____/ |   ||  |_> >
 \______  / |__||___|  /        |___||   __/ 
        \/           \/              |__|    
"""

API_URL = "https://ipinfo.io/{}/json"


def search(ip=""):
    """Look up an IP address on ipinfo.io. An empty string looks up your own IP."""
    url = API_URL.format(ip) if ip else "https://ipinfo.io/json"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    if data.get("bogon"):
        raise ValueError("That's a private or reserved address, so it has no public location.")

    return {
        "IP": data.get("ip"),
        "City": data.get("city"),
        "Region or State": data.get("region"),
        "Country": data.get("country"),
        "Coordinates": data.get("loc"),
        "ISP (Internet Service Provider)": data.get("org"),
        "Timezone": data.get("timezone"),
    }


def print_result(result):
    width = max(len(key) for key in result)
    for key, value in result.items():
        print(f"{GREEN}{key:<{width}}{RESET} : {value or 'N/A'}")


def main():
    print(f"{GREEN}{BANNER}{RESET}")
    print("Enter an IP address (blank = your own IP, q = quit)\n")

    while True:
        try:
            ip = input(f"{GREEN}search IP :0 > {RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            break

        if ip.lower() in {"q", "quit", "exit"}:
            break

        try:
            print()
            print_result(search(ip))
        except requests.HTTPError:
            print(f"{RED}Lookup failed. Check that the IP address is valid.{RESET}")
        except requests.RequestException:
            print(f"{RED}Network error. Check your connection and try again.{RESET}")
        except ValueError as err:
            print(f"{RED}{err}{RESET}")

        print()


if __name__ == "__main__":
    main()

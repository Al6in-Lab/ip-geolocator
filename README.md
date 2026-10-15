# ip-geolocator

A small, clean command-line tool that looks up the approximate location and network details of any public IP address.

```
  ________  .__               .___        
 /  _____/  |__|  ____        |   |______  
/   \  ___  |  | /    \  ______ |   |\____ \ 
\    \_\  \ |  ||   |  \/_____/ |   ||  |_> >
 \______  / |__||___|  /        |___||   __/ 
        \/           \/              |__|    
```

## Features

- Look up any public IPv4 or IPv6 address
- Leave the prompt blank to look up your own IP
- Shows city, region, country, coordinates, ISP and timezone
- Handles invalid IPs, private addresses and network errors without crashing
- No API key required

## Requirements

- Python 3.8+
- [`requests`](https://pypi.org/project/requests/)

## Installation

```bash
git clone https://github.com/Al6in-Lab/ip-geolocator.git
cd ip-geolocator
```

Create and activate a virtual environment so the dependencies stay isolated from your system Python:

```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

When you're done, leave the environment with `deactivate`.

## Usage

```bash
python ip_geolocator.py
```

Type an IP address at the prompt and press Enter. Type `q` (or press `Ctrl+C`) to quit.

### Example

```
search IP :0 > 8.8.8.8

IP                              : 8.8.8.8
City                            : Mountain View
Region or State                 : California
Country                         : US
Coordinates                     : 37.4056,-122.0775
ISP (Internet Service Provider) : AS15169 Google LLC
Timezone                        : America/Los_Angeles
```

## How it works

The script sends a request to the free [ipinfo.io](https://ipinfo.io) API and prints the fields it returns. The free tier has rate limits, so very heavy use may be throttled.

## Notes

- IP geolocation is approximate. It usually points to the ISP's regional hub, not an exact street address.
- Private and reserved addresses (like `192.168.x.x`) have no public location and will return a message saying so.
- Please use this tool responsibly.


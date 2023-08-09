
"""
Bitcoin Price Index
https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
"""

import sys
import requests
import json

if len(sys.argv) == 2:
    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
#   print(json.dumps(response, indent = 2))
    rate = response["bpi"]["USD"]["rate_float"]
    amount = rate * bitcoin
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()

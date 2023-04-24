#!/usr/bin/python3
import requests, os

try:
    os.system("clear")
    while True:
        quote_data = requests.get("https://zenquotes.io/api/quotes").json()
        # print(quote_data)
        for quote_list in quote_data:
            quote = quote_list['q']
            print(f"\33[93m{quote}\33[0m")
except KeyboardInterrupt:pass
except Exception as e:print(e)
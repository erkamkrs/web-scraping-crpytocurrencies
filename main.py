import requests
from bs4 import BeautifulSoup
import lxml
import csv
import pandas as pd
import html5lib



headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}

URL = "https://www.coingecko.com/"

response = requests.get(url=URL, headers=headers)

website_html = response.text

soup = BeautifulSoup(website_html, "lxml")

tables = []


soup = BeautifulSoup(response.content, "html.parser")
tables.append(pd.read_html(str(soup))[0])

main_table = pd.concat(tables)
table = main_table.loc[:, main_table.columns[1:-1]]
file_title = "Crypto Currencies Data Table"
table.to_csv(file_title, index=False)


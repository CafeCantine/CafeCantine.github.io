#!/usr/bin/env python3
import json
from urllib.request import urlopen

from bs4 import BeautifulSoup


def fetch_data():
    with urlopen('https://www.papayoux-solidarite.com/fr/collecte/le-cafe-cantine-a-besoin-de-soutien') as response:
        soup = BeautifulSoup(response.read().decode('utf-8', 'ignore'), 'html.parser')
        __update_amount(soup)
        __update_donators(soup)


def __update_amount(soup: BeautifulSoup):
    anchor = soup.find(id="montant")
    amount = anchor.text
    with open("data/amount", "w") as target:
        target.write(amount)


def __update_donators(soup: BeautifulSoup):
    donators = [anchor.text for anchor in soup.find_all("div", {"id": "pseudo"})]
    with open("data/donators.json", "w") as target:
        target.write(json.dumps(donators))


if __name__ == "__main__":
    fetch_data()

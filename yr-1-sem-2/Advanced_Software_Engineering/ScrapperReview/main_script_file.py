import csv
import os.path
import builtwith
import requests
from bs4 import BeautifulSoup


FIELD_TITLE = "Title"
FIELD_LINKS = "Links"


def fetch_html(url, payload):
    """Fetch url and return the HTML content"""
    r = requests.get(url, params=payload)
    print("You're on", r.url)
    return r.content


def parse_and_scrape_data(raw_data):
    soup = BeautifulSoup(raw_data, "html.parser")

    for item in soup.find_all("div", {"class": "g"}):
        title = item.a.text
        links = item.cite.text
        print(links)
        product_details = {
            FIELD_TITLE: title,
            FIELD_LINKS: links,
        }
        write_on_csv(product_details)


def write_on_csv(product_details, filename="googleresults.csv"):
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile, fieldnames=(FIELD_TITLE, FIELD_LINKS))

        if not file_exists:
            writer.writeheader()

        writer.writerow(product_details)
        print("wrote on to the file")


if __name__ == "__main__":
    print("Running as a progam")
    # TODO: Do something useful


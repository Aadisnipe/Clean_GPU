# #give name of the gpu and it will return the price of the gpu from various site
# from scrappper.md_scraper import MdScraper
# print(MdScraper().scrape("NVIDIA GeForce RTX 3080"))

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class MDComputersScraper:

    BASE_URL = "https://mdcomputers.in/"

    def __init__(self):
        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/130.0.0.0 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,"
                "application/xml;q=0.9,*/*;q=0.8"
            ),
            "Accept-Language": "en-IN,en;q=0.9",
        })

    def search(self, product_name):

        params = {
            "route": "product/search",
            "search": product_name
        }

        response = self.session.get(
            self.BASE_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        products = []

        for item in soup.select(".product-grid-item"):

            title_element = item.select_one(
                ".product-entities-title a"
            )

            if not title_element:
                continue

            price_element = item.select_one(
                ".price .ins"
            )

            if not price_element:
                price_element = item.select_one(".price")

            image_element = item.select_one(
                ".product-image-link img"
            )

            product = {
                "name": title_element.get_text(
                    " ", strip=True
                ),
                "price": (
                    price_element.get_text(" ", strip=True)
                    if price_element else None
                ),
                "url": urljoin(
                    self.BASE_URL,
                    title_element.get("href", "")
                ),
                "image": (
                    urljoin(
                        self.BASE_URL,
                        image_element.get("src", "")
                    )
                    if image_element else None
                )
            }

            products.append(product)

        return products


if __name__ == "__main__":

    scraper = MDComputersScraper()

    product_name = input("Enter product name: ")

    products = scraper.search(product_name)

    print(f"\nFound {len(products)} products\n")

    for index, product in enumerate(products, start=1):

        print(f"Product {index}")
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("URL:", product["url"])
        print("Image:", product["image"])
        print("-" * 60)

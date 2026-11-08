from wsgiref import headers

from ..scrapper import Scraper
import os
import requests
from urllib.parse import urlencode
#Things I have Noticed:
'''
    Only mention name here not metion the word
    Graphics card in the name
    Not metion the Memory type like GDDR6 etc
'''
class MdScraper(Scraper):
    def scrape(self, gpu_name):
        headers = {
                 # Browser identification
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/131.0.0.0 Safari/537.36"
            ),
        
            # Accepted response formats
            "Accept": (
                "text/html,application/xhtml+xml,"
                "application/xml;q=0.9,image/avif,"
                "image/webp,image/apng,*/*;q=0.8"
            ),
        
            # Language preferences
            "Accept-Language": "en-US,en;q=0.9",
        
            # Compression
            "Accept-Encoding": "gzip, deflate, br",
        
            # Connection
            "Connection": "keep-alive",
        
            # Browser navigation context
            "Upgrade-Insecure-Requests": "1",
        
            # Fetch metadata
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
        
            # Browser client hints
            "sec-ch-ua": (
                '"Chromium";v="131", '
                '"Google Chrome";v="131", '
                '"Not_A Brand";v="24"'
            ),
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            }
        session = requests.Session()
        session.headers.update(headers)
        url = f"https://www.mdcomputers.in/search?}"
        response = session.get(url,timeout=20)
        
        return "Implement the scraping logic for the specific website here"
        # Implement the scraping logic for the specific website here
        # For example, you can use requests and BeautifulSoup to fetch and parse the HTML
        # Return the price of the GPU as a string or a number

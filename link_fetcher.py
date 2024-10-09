# link_fetcher.py

import requests
from bs4 import BeautifulSoup

from color_manager import COLOR_CODES


class LinkFetcher:
    """Fetch links from a given URL."""

    @staticmethod
    def fetch(url):
        if url=="":
            print("Empty URL")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx/5xx responses
            soup = BeautifulSoup(response.content, 'html.parser')
            # Return a set of all unique links from the page
            return {link.get('href') for link in soup.find_all('a') if link.get('href')}
        except requests.RequestException as e:
            print(f"{COLOR_CODES['red']}Error fetching {url}: {e}")  # Print error in red
            return set()

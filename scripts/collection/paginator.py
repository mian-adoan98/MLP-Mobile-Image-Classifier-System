## Pagination: extract website urls from paginised arrays on webpage 

# Import libraries 
import pandas as pd 
import requests 
import os 

# Import selenium dependencies for setting up 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Import selenium depdencies part 2 for extracting content from web
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Implement class Paginator
class Paginator: 
    # Initialise attributes for extracting multiple webpages through paginisation
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.start_path = "/android-os/"

    # Method 1: Extract pages 
    def verify_link(self, website_url: str) -> BeautifulSoup: 
        response = requests.get(website_url)

        if response.status_code == 200:
            webpage_html = response.text
            soup = BeautifulSoup(webpage_html, "lxml")
            print("Extract web content successfully!")
        else:
            print(f"Extract web content not successfully. Status code = {response.status_code}")
        
        return soup
    
    # Method 2: Extract one link page
    def extract_page(self, full_url: str):
        resp = requests.get(full_url)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Extract product detail links—adjust selector if needed
        product_links = [urljoin(self.base_url, a["href"]) 
                        for a in soup.select("a.view-details")]

        # Extract "next" link
        next_link_tag = soup.find("a", string="next")
        next_url = urljoin(self.base_url, next_link_tag["href"]) if next_link_tag else None

        return product_links, next_url
    
    # Method 3: Extract all links
    def extract_all(self):
        current_url = urljoin(self.base_url, self.start_path)
        all_product_links = []

        while current_url:
            print(f"Scraping {current_url}")
            links, next_url = self.extract_page(current_url)
            all_product_links.extend(links)
            all_product_links.append(current_url)
            current_url = next_url

        return all_product_links
    
    # Method 4: Pipeline (NEED MORE UPDATEs)
    def paginator_pipeline(self):
        product_links, next_url = self.extract_all(self)
        product_links = self.extract_all(self)



# Example code 
if __name__ == "__main__":
    pass 
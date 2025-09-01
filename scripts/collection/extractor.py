# Extraction
# Implement abstract dependencies
from abc import ABC, abstractmethod
# Import necessary libraries
import pandas as pd 
import time

# Import selenium dependencies for setting up 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Import selenium depdencies part 2 for extracting content from web
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# Implementing 3 different classes: ImageExtractor, LabelExtractor, Paginisor

# Implement Extractor abstract class
class Extractor(ABC):
    # Abstract method 1: 
    @abstractmethod
    def extract(self, weblink: str) -> list:
        pass

# Implement ImageExtractor class
class ImageExtractor(Extractor):
    # Method 1: Extract images from dynamic webpage  
    def extract(self, weblink: str) -> list:
        # Set up options 
        options = Options()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")

        # Set up driver including options 
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(weblink)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5)

        # Extract images from website 
        product_images = driver.find_elements(By.CSS_SELECTOR, "div.product-module figure img")
        image_urls = [img.get_attribute("data-src") or img.get_attribute("src") for img in product_images]

        # Quit the driver 
        driver.quit()

        return image_urls
    
# Implement LabelExtractor class
class LabelExtractor(Extractor):
    # Extract dataset into a 
    def extract(self, weblink: str) -> list:
        # Set up options 
        options = Options()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")

        # Set up driver including options 
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(weblink)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5)

        # Extract images from website 
        product_titles = driver.find_elements(By.CSS_SELECTOR, "div.product-name h5 a")
        labels = [title.text for title in product_titles]

        # Number of labels
        num_labels = len(labels)
        print(f"Extract {num_labels} labels from {weblink}")
        # Quit the driver 
        driver.quit()

        return labels

# Example code 
if __name__ == "__main__":
    pass 
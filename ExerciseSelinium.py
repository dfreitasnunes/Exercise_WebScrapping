import sys
sys.path.append('Lib')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class ZipLinkScraper:
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.url = url
        self.driver = None

    def start_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
        self.driver = webdriver.Chrome(service=Service(self.driver_path), options=chrome_options)

    def stop_driver(self):
        if self.driver:
            self.driver.quit()

    def extract_zip_links(self):
        self.start_driver()
        self.driver.get(self.url)
        
        time.sleep(3)  # Wait for the page to load

        # Find all anchor elements with .zip in their href attribute
        zip_links = self.driver.find_elements(By.XPATH, "//a[contains(@href, '.zip')]")
        
        # Extract the href attribute (the link)
        zip_link_urls = [link.get_attribute('href') for link in zip_links]

        self.stop_driver()
        return zip_link_urls



def main():
    driver_path = 'chromedriver-win64\chromedriver.exe'  # Update this path
    url = 'https://www.ibge.gov.br/estatisticas/sociais/populacao/22827-censo-demografico-1991.html?=&t=downloads'  # Update this URL

    scraper = ZipLinkScraper(driver_path, url)
    zip_links = scraper.extract_zip_links()

    print("Extracted .zip links:")
    for link in zip_links:
        print(link)

# Example usage
if __name__ == "__main__":
    main()
   
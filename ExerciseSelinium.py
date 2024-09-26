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
        # Run in headless mode (no GUI)
        chrome_options.add_argument("--headless")  
        #Start the chrome driver
        self.driver = webdriver.Chrome(service=Service(self.driver_path), options=chrome_options)

    def stop_driver(self):
        if self.driver:
            self.driver.quit()

    def extract_zip_links(self):
        self.start_driver()
       
        self.stop_driver()
        return 



def main():
    # Path for the Driver
    driver_path = r'C:\Users\diogo.nunes\Desktop\Empresa\python\Exercise\Exercise_WebScrapping\chromedriver-win64\chromedriver.exe'  
     # Url to scrappe
    url = 'https://www.ibge.gov.br/estatisticas/sociais/populacao/22827-censo-demografico-1991.html?=&t=downloads' 

    scraper = ZipLinkScraper(driver_path, url)
    zip_links = scraper.extract_zip_links()

    print("Extracted .zip links:")
    for link in zip_links:
        print(link)

# Example usage
if __name__ == "__main__":
    main()
   
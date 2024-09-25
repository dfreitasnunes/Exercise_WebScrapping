# Exercise.py
import sys
sys.path.append('Lib')


import requests
import zipfile
import os
from bs4 import BeautifulSoup



class WebScraper:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.soup = None

    def fetch_content(self):
        #Fetch the HTML content from the URL
        try:
            self.response = requests.get(self.url)
            # Raise an error for bad status codes
            self.response.raise_for_status()  
            print("Content fetched successfully!")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching content: {e}")

    def parse_content(self):
        #Parse the HTML content using BeautifulSoup
        if self.response is not None:
            # Using html.parser , trouble in using lxml 
            self.soup = BeautifulSoup(self.response.content, 'html.parser') 
            print("Content parsed successfully!")
            print(self.soup)
        else:
            print("No content to parse. Did you fetch the content first?")

    def extract_data(self):
        #Extract specific data from the parsed HTML based on tag and class.
        if self.soup is not None:
            elements = self.soup.find_all('li', {'id' :'Censos/Censo_Demografico_1991/Indice_de_Gini'})
            if not elements:
                return print('falhoupah')
            return self.soup.find_all(tag, class_=class_name)
        else:
            print("No parsed content found. Please parse the content first.")
            return []

    def extract_zip_links(self):
        # Use extract_data to get all anchor tags for <a>
        anchors = self.extract_data('a')
        zip_links = []
        
        # Filter for .zip links
        for anchor in anchors:
            href = anchor.get('href')
            if href and href.endswith('.zip'):
                zip_links.append(href)
        
        return zip_links
   



    def read_zip_contents(self, zip_path):
        # Check if the file exists
        if not os.path.exists(zip_path):
            print(f"The file {zip_path} does not exist.")
            return
        
        # Open the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            print("Contents of the zip file:")
            zip_file.printdir()
            
            # Read and print the contents of each file
            for file_info in zip_file.infolist():
                print(f"\nReading {file_info.filename}:")
                with zip_file.open(file_info) as file:
                    content = file.read()
                    print(content.decode('utf-8', errors='replace'))  # Decode bytes to string



def main():
    # URL to scrape 
    url = "https://www.ibge.gov.br/estatisticas/sociais/populacao/22827-censo-demografico-1991.html?=&t=downloads"
    # Instantiate the scraper with the target URL
    scraper = WebScraper(url)
    # Fetch and parse the content
    scraper.fetch_content()
    scraper.parse_content()
    #print(scraper.extract_data())
    # Extract all the zip links
    #zip_links = scraper.extract_zip_links('Censo_Demografico_1991')
    #print(zip_links)
    
    
    # To hold the combined content from all zip files

    #all_zip_contents = {}

    # Loop through each zip link and read its contents
    #for zip_link in zip_links:
        #print(f"Processing zip link: {zip_link}")
        # Here you might want to download the zip file first, e.g., using requests
        #response = requests.get(zip_link)
        #zip_file_path = zip_link.split('/')[-1]  # Extract filename from URL

        # Save the downloaded zip file
        #with open(zip_file_path, 'wb') as f:
            #f.write(response.content)

        # Read the contents of the downloaded zip file
        #zip_contents = {}
        #with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            #for file_info in zip_file.infolist():
                #with zip_file.open(file_info) as file:
                    #content = file.read()
                    #zip_contents[file_info.filename] = content.decode('utf-8', errors='replace')

        #all_zip_contents[zip_file_path] = zip_contents

        # Delete the zip file after processing
        #os.remove(zip_file_path)

        # Now all_zip_contents holds the data from all processed zip files
        #print("Combined contents from all zip files:")
        #for zip_name, contents in all_zip_contents.items():
            #print(f"\nContents of {zip_name}:")
            #for filename, content in contents.items():
                #print(f"\nFile: {filename}\nContent:\n{content[:100]}...")  # Print the first 100 chars of each file

    # Write all contents to a file
    #output_file_path = 'extracted_contents.txt'
    #with open(output_file_path, 'w', encoding='utf-8') as output_file:
        #for zip_name, contents in all_zip_contents.items():
            #output_file.write(f"Contents of {zip_name}:\n")
            #for filename, content in contents.items():
                #output_file.write(f"\nFile: {filename}\nContent:\n{content}\n")
            #output_file.write("\n" + "="*40 + "\n")  # Separator between zip file contents
    

if __name__ == "__main__":
    main()
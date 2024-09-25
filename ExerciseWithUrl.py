import sys
sys.path.append('Exercise\Exercise_WebScrapping\Lib')

import requests
import tempfile
import os
import zipfile
import xlrd 


class URLExtractorFromIBGE:
    def __init__(self, api_url):
        self.api_url = api_url
        self.urls = []
        self.data_content = ""

    def fetch_data(self):
        """Fetch data from the provided API URL."""
        response = requests.get(self.api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def extract_urls(self, json_data):
        """Extract URLs from the provided JSON data."""
        for item in json_data:
            if 'url' in item:
                self.urls.append(item['url'])

    def get_urls(self):
        """Fetch data from the API and return extracted URLs."""
        json_data = self.fetch_data()
        self.extract_urls(json_data)
        return self.urls
    def download_file(self, url):
        """Download a file from the URL and return the temporary file path."""
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Create a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        with open(temp_file.name, 'wb') as f:
            f.write(response.content)
        return temp_file.name
    def read_file_content(self, file_path):
            extracted_data = ""
            # Open the ZIP file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                print("Contents of the ZIP file:")
                print(zip_ref.namelist())  # List all files in the ZIP
                # Iterate through the contents of the ZIP file
                for file_name in zip_ref.namelist():
                    # Check if the file is an .xlsx file (update this to '.xls' if needed)
                    if file_name.endswith('.XLS'):
                        print(f"Reading file: {file_name}")
                        with zip_ref.open(file_name) as file:
                            # Load the workbook
                            print('ola')
                            workbook = xlrd.open_workbook(file_contents=file.read())
                            print('ole')
                            for sheet_index in range(workbook.nsheets):
                                ws = workbook.sheet_by_index(sheet_index)
                                for row_index in range(ws.nrows):
                                    # Read each row as a tuple
                                    row = ws.row_values(row_index)
                                    # Join the cell values with a tab and append to extracted_data
                                    extracted_data += "\t".join(str(cell) if cell is not None else '' for cell in row) + "\n"
            return extracted_data
    
    def process_files(self):
        #zip_contents = {}
        """Download each file, read its content, and append to data_content."""
        for url in self.urls:
            try:
                if url.endswith('.zip'):
                    print(url)
                    temp_file_path = self.download_file(url)
                    file_content = self.read_file_content(temp_file_path)
                    print(file_content)
                    self.data_content += file_content + "\n"  # Append content with a newline
                    os.remove(temp_file_path)  # Delete the temporary file
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while processing {url}: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
    def get_data_content(self):
        """Return the accumulated data content."""
        return self.data_content

# Example usage
if __name__ == "__main__":
    api_url = "https://servicodados.ibge.gov.br/api/v1/downloads/estatisticas?caminho=Censos/Censo_Demografico_1991/Indice_de_Gini&nivel=1"
    extractor = URLExtractorFromIBGE(api_url)
    
    try:
        urls = extractor.get_urls()
        print("Extracted URLs:")
        print(urls)
        
        extractor.process_files()
        combined_data = extractor.get_data_content()
        
        print("\nCombined Data Content:")
        print(combined_data)
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
Objective: 

Extract data from IBGE (https://www.ibge.gov.br/) and persist it in the DBMS of your choice. This data corresponds to the Demographic Census (Gini index) conducted in 1991 (e.g., Acre.zip, Alagoas.zip, Amapa.zip, etc.).

Requirements:

Use an object-oriented programming (OOP) approach (SOLID principles);
Make the source code available on GitHub (commits should correspond to the changes made);
Containerize the application and the services used (optional). Not Check

Development :

I initially approached the project using BeautifulSoup to scrape .zip links from the static content on the IBGE website. However, I encountered an obstacle when I found that the required .zip files were generated dynamically via JavaScript, making BeautifulSoup unsuitable for this task.

To overcome this, I turned to Selenium, which is better suited for handling JavaScript content. Unfortunately, I faced additional challenges because my work computer has BlackCarbon blocking the ChromeDriver, preventing me from using it effectively.

After researching how the JavaScript was constructing the download links, I discovered that they were accessible through an API endpoint: https://servicodados.ibge.gov.br/api/v1/downloads/estatisticas?caminho=Censos/Censo_Demografico_1991/Indice_de_Gini&nivel=1. I built a class to extract these .zip links, then proceeded to extract .xls information and compile all the data together. This is able to accept any kind of path for the censos.

However, I encountered several problems during the process. Due to BlackCarbon restrictions on my work computer, I was unable to use pip install freely, leading to challenges in correctly installing libraries and their dependencies. For instance, instead of using pandas, I had to rely on xlrd due to issues with the numpy dependency. As a result, my libraries folder has become quite chaotic. 

I also did not start the project from a fresh GitHub repository, which contributed to some confusion with Git commits.
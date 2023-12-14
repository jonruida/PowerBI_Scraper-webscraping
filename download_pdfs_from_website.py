####################
# Author : Kulwinder K.
# Date : 12/06/2023
# This script downloads the pdf files available on the webpages 
# https://www.un.org/techenvoy/global-digital-compact
# https://www.un.org/techenvoy/global-digital-compact/submissions
# and saves them in separate folders
#####################

#importing libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import requests
import time
import os

def download_pdfs():

    chrome_options = Options()

    # Set the executable path for the Chrome WebDriver
    #path to your executable
    chrome_options.add_argument("webdriver.chrome.driver=..\chrome-win64")

    #url of the webpage that needs to be parse
    urls = ['https://www.un.org/techenvoy/global-digital-compact', 'https://www.un.org/techenvoy/global-digital-compact/submissions']

    #create download folder in same directory
    notebook_directory = os.path.abspath('')
    download_subdirectory='data'
    # Create the full path to the download directory
    download_directory = os.path.join(notebook_directory, download_subdirectory)
    download_directory

    # Create the directory if it doesn't exist
    if not os.path.exists(download_directory):
    os.makedirs(download_directory)

    # Create a new instance of the Chrome driver with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    for url in urls:
        # Navigate to the webpage
        driver.get(url)

        # Find all PDF links on the page
        pdf_links = driver.find_elements(By.XPATH, '//a[contains(@href, ".pdf")]')
    
        # Iterate through each PDF link
        for pdf_link in pdf_links:
        
            # Get the direct link to the PDF file
            pdf_file_url = pdf_link.get_attribute('href')
    
            # Use requests to download the PDF file with headers and session
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            session = requests.Session()
            response = session.get(pdf_file_url, headers=headers, stream=True)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Extract the filename from the URL
                filename = pdf_file_url.split("/")[-1]
                # Specify the full path to the file
                folder_name=url.split("/")[-1]
            
                current_download_dir= os.path.join(download_directory, folder_name)
            
                if not os.path.exists(current_download_dir):
                    os.makedirs(current_download_dir)
            
                full_path = current_download_dir + "\\" + filename

                # Save the PDF to a local file
                with open(full_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                print(f"File '{filename}' downloaded successfully.")
            else:
                print(f"Failed to download file. Status code: {response.status_code}")
        
            time.sleep(1)
        

    driver.quit()

if __name__ == "__main__":
    download_pdfs()

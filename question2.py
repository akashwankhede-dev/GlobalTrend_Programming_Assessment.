# 2) Write a Python function that takes a list of URLs, attempts to download their content, and retries up to 3 times if an error occurs. Use appropriate error handling to manage different types of exceptions.

import requests
from time import sleep

def download_content(urls):
    results = {}
    max_retries = 3

    for url in urls:
        success = False
        attempts = 0

        while not success and attempts < max_retries:
            try:
                response = requests.get(url)
                response.raise_for_status()
                results[url] = response.text
                success = True
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err} - {url}")
            except requests.exceptions.ConnectionError as conn_err:
                print(f"Connection error occurred: {conn_err} - {url}")
            except requests.exceptions.Timeout as timeout_err:
                print(f"Timeout error occurred: {timeout_err} - {url}")
            except requests.exceptions.RequestException as req_err:
                print(f"Error occurred: {req_err} - {url}")
            
            if not success:
                attempts += 1
                if attempts < max_retries:
                    print(f"Retrying {url} ({attempts}/{max_retries})...")
                    sleep(1)  # Wait for 1 second before retrying

        if not success:
            results[url] = None
            print(f"Failed to download content from {url} after {max_retries} attempts")

    return results

# Example usage:
urls = [
    "https://www.google.com",
    "https://www.python.org",
]

content = download_content(urls)
for url, data in content.items():
    if data:
        print(f"Content from {url}:\n{data[:100]}...")  # Print first 100 characters
    else:
        print(f"Failed to retrieve content from {url}")

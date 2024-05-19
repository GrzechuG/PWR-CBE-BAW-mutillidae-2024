import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# A5 - Directory Browsing, file: lista_url_directory.txt, check_value = 'Validation Error: 404 - Page Not Found'
# A7 - Secret Administrative Pages, file: lista_url_php.txt, check_value = '404 Not Found'

def find_secret_pages(url, check_value):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if check_value in soup.get_text():
            return None
        else:
            title = soup.title.text if soup.title else "Null"
            return (url, title)

def pages_enum(popular_url, main_url, check_value, cores=8):
    urls_to_check = []
    with open(popular_url, 'r') as f:
        for line in f:
            url = main_url + line.strip()
            urls_to_check.append(url)

    with ThreadPoolExecutor(max_workers=cores) as executor:
        results = list(tqdm(executor.map(lambda url: find_secret_pages(url, check_value), urls_to_check), total=len(urls_to_check), desc="Przetwarzanie podstron"))

    for result in results:
        if result is not None:
            print(f"-Page Name '{result[0]}': {result[1]}")

if __name__ == "__main__":
    popular_url = "lista_url_directory.txt" 
    check_value = '404 Not Found'
    url = "http://192.168.64.141/mutillidae/"
    pages_enum(popular_url, url, check_value)
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def find_secret_pages(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if 'Validation Error: 404 - Page Not Found' in soup.get_text():
            return None
        else:
            title = soup.title.text if soup.title else "Null"
            return (url, title)

def pages_enum(popular_url, main_url, cores=8):
    urls_to_check = []
    with open(popular_url, 'r') as f:
        for line in f:
            url = main_url + line.strip()
            urls_to_check.append(url)

    with ThreadPoolExecutor(max_workers=cores) as executor:
        results = list(tqdm(executor.map(find_secret_pages, urls_to_check), total=len(urls_to_check), desc="Przetwarzanie podstron"))

    for result in results:
        if result is not None:
            print(f"-Page Name '{result[0]}': {result[1]}")

if __name__ == "__main__":
    popular_url = "lista_url.txt" 
    url = "http://192.168.64.141/mutillidae/index.php?page="
    pages_enum(popular_url, url)
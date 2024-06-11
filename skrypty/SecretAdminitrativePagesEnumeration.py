import requests
import argparse
from bs4 import BeautifulSoup
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# A5 - Directory Browsing, file: lista_url_directory.txt, check_value = 'Validation Error: 404 - Page Not Found'
# A7 - Secret Administrative Pages, file: lista_url_php.txt, check_value = '404 Not Found'


def find_secret_pages(url, check_value):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        if check_value in soup.get_text():
            return None
        else:
            title = soup.title.text if soup.title else "Null"
            return (url, title)


def pages_enum(popular_url, main_url, check_value, cores=8):
    urls_to_check = []
    with open(popular_url, "r") as f:
        for line in f:
            url = main_url + line.strip()
            urls_to_check.append(url)

    # https://docs.python.org/3/library/concurrent.futures.html
    with ThreadPoolExecutor(max_workers=cores) as executor:
        results = list(
            tqdm(
                executor.map(
                    lambda url: find_secret_pages(url, check_value), urls_to_check
                ),
                total=len(urls_to_check),
                desc="Przetwarzanie podstron",
            )
        )

    for result in results:
        if result is not None:
            print(f"-Nazwa strony '{result[0]}': {result[1]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Enumeracja stron/podstron/plików/parametrów na bazie odwrócenia słowa kluczowego, odnajdując wszystkie podstrony nie zawierające tej treści. "
    )
    parser.add_argument("--url", type=str, help="Adres URL strony")
    parser.add_argument(
        "--list",
        type=str,
        help="Nazwa pliku zawierającego liste (musi znajdować się na tym samym poziomie w systemie co plik wykonywalny)",
    )
    parser.add_argument("--klucz", type=str, help="Słowo kluczowe np. '404 Not Found'")
    args = parser.parse_args()

    pages_enum(args.list, args.url, args.klucz)

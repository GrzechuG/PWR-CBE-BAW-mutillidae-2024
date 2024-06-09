from selenium import webdriver
from seleniumwire import webdriver as wire_webdriver

# from os import path


class FirefoxBrowser:
    def __init__(self, headless=False):
        options = webdriver.FirefoxOptions()
        # if path.exists(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'):
        #     options.binary_location = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
        # else:
        #     options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        if headless:
            options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)


class FirefoxBrowserSeleniumWire:
    def __init__(self, headless=False, user_agent=""):
        options = wire_webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        if user_agent != "":
            options.set_preference("general.useragent.override", user_agent)
        self.driver = wire_webdriver.Firefox(options=options)

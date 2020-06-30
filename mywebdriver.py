from selenium import webdriver
from values import strings


class Driver:

    def __init__(self):
        path = "/Users/abichevo/PycharmProjects/Integration/chromedriver"
        self.instance = webdriver.Chrome(executable_path=path)

    def navigate(self, base_url):
        if isinstance(base_url, str):
            self.instance.get(strings.base_url)
            self.instance.maximize_window()
        else:
            raise TypeError("URL must be a string.")

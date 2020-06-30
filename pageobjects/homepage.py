import allure
from pageobjects.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.logo_boat_setter = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//img[@class='u-mr2']")))

    @allure.step("Validate Search container is present")
    def validate_search_container_is_present(self):
        search_container = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "SearchHome-content")))
        assert search_container.is_displayed()





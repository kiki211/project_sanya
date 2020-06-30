import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

        #####################
        #    Upper footer   #
        #####################
    @allure.step("Validate Upper footer links are present")
    def validate_upper_footer_links_are_present(self):
        logo = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//img[@class='u-mr2']")))
        assert logo.is_displayed()
        top_menu = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "js-nav-top")))
        assert top_menu.is_displayed()
        search_bar = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "js-nav-searchbar")))
        assert search_bar.is_displayed()
        list_your_boat_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "u-textWhite u-textNoWrap u-fsSm u-md-hide'")))
        assert list_your_boat_link.is_displayed()
        signup_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Sign up')]")))
        assert signup_link.is_displayed()
        login_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Log in')]")))
        assert login_link.is_displayed()
        how_it_works_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'How it works')]")))
        assert how_it_works_link.is_displayed()
        support_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Support')]")))
        assert support_link.is_displayed()

        #####################
        #    Lower footer   #
        #####################
    @allure.step("Validate Lower footer links are present")
    def validate_lower_footer_links_are_present(self):
        lower_footer = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//footer[@class='global-footer u-pv4 u-bgWhite']")))
        terms_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Terms')]")))
        privacy = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Privacy')]")))
        how_it_works = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'How it Works')]")))
        about = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'About')]")))
        careers = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Careers')]")))
        press = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Press')]")))
        blog = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Blog')]")))
        reviews = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Reviews')]")))
        why_list = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Why List')]")))
        refer_owner = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Refer an Owner')]")))
        captains = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Captains')]")))
        partners = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Partners')]")))
        affilliates = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Affiliates')]")))
        support = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Support')]")))
        safety_tips = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Safety Tips')]")))
        experiences = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Experiences')]")))
        boating_quides = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Boating Guides')]")))
        rules_regulations = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Rules and Regulations')]")))
        san_francisco = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'San Francisco')]")))
        miami = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Miami')]")))
        new_york = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'New York')]")))
        chicago = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Chicago')]")))
        washington_dc = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Washington DC')]")))
        seattle = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[contains(text(),'Seattle')]")))
        see_all_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[@class='u-textPrimary u-fsSm u-textUnderline']")))
        icon_facebook = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//i[@class='Icon Icon-facebook']")))
        icon_twiter = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//i[@class='Icon Icon-twitter']")))
        icon_instagram = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//i[@class='Icon Icon-instagram']")))
        assert lower_footer.is_displayed()
        assert terms_link.is_displayed()
        assert privacy.is_displayed()
        assert how_it_works.is_displayed()
        assert about.is_displayed()
        assert careers.is_displayed()
        assert blog.is_displayed()
        assert reviews.is_displayed()
        assert press.is_displayed()
        assert why_list.is_displayed()
        assert refer_owner.is_displayed()
        assert captains.is_displayed()
        assert partners.is_displayed()
        assert affilliates.is_displayed()
        assert support.is_displayed()
        assert safety_tips.is_displayed()
        assert experiences.is_displayed()
        assert boating_quides.is_displayed()
        assert rules_regulations.is_displayed()
        assert san_francisco.is_displayed()
        assert miami.is_displayed()
        assert chicago.is_displayed()
        assert washington_dc.is_displayed()
        assert new_york.is_displayed()
        assert seattle.is_displayed()
        assert see_all_link.is_displayed()
        assert icon_facebook.is_displayed()
        assert icon_instagram.is_displayed()
        assert icon_twiter.is_displayed()



        # @allure.step("Click About Me menu link")
        # def click_about_me_link(self):
        #     about_me_link = WebDriverWait(self.driver.instance, 10).until(
        #         EC.visibility_of_element_located((
        #             By.LINK_TEXT, "About Me")))
        #     about_me_link.click()

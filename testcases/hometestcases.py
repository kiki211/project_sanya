import unittest
from pageobjects.homepage import HomePage
from values import strings
from mywebdriver import Driver


class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_page = HomePage(self.driver)
        home_page.validate_search_container_is_present()
        home_page.validate_upper_footer_links_are_present()
        home_page.validate_lower_footer_links_are_present()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()

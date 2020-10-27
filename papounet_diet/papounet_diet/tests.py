from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class CustomerTestCase(LiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = WebDriver()
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_home_page(self):
        """
        Test the User story with an optimal scenario
        """
        self.browser.get('%s%s' % (self.live_server_url, ''))
        brand_element = self.browser.find_element_by_class_name('brand')
        self.assertEqual('test', brand_element.text)
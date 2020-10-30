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

    def test_quickly_find_product_from_home_page(self):
        """
        Test the User story where the persona wants to look for a product
        without logging in
        """
        self.browser.get('%s%s' % (self.live_server_url, ''))
        self.assertIsNotNone(self.browser.find_element_by_id(
            "favicon"))
        # First of all, Lily Kala has a look at the page
        # At the top, she can see a navigation bar displaying:
        # The company logo
        self.assertIsNotNone(self.browser.find_element_by_id(
            "company_logo"))
        # The company name
        brand_element = self.browser.find_element_by_class_name('brand')
        self.assertEqual('Pur Beurre', brand_element.text)
        # The possibility to log in
        self.assertIsNotNone(self.browser.find_element_by_id(
            "login"))
        # To retrieve recorded products
        self.assertIsNotNone(self.browser.find_element_by_id(
            "carrot"))
        # To log off
        self.assertIsNotNone(self.browser.find_element_by_id(
            "logout"))
        
        self.fail("Test Incomplet")



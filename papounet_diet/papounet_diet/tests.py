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
        # A field to search for an item
        customer_input = self.browser.find_element_by_css_selector(
            'input#customer_input')
        self.assertEqual(customer_input.get_attribute(
            'placeholder'), 'Recherche')
        # In the upper half of the page, a picture
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'img#background_picture'))
        # Contains the motto and a piece of advice
        self.browser.find_element_by_css_selector('h1#motto')
        self.browser.find_element_by_css_selector('h2#advice')
        # and a search field with a validation button.
        main_customer_input = self.browser.find_element_by_css_selector(
            'input#main_customer_input')
        self.assertEqual(main_customer_input.get_attribute(
            'placeholder'), 'Recherche')
        # Just below Lily Kala can see the story of the company
        self.browser.find_element_by_css_selector('h2#heroes')
        self.browser.find_element_by_css_selector('p#story')
        # With the pictures of Colette and Remy
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'img#Colette'))
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'img#Remy'))
        # Still below LK sees an invite to contact the company
        call_to_action = self.browser.find_element_by_css_selector(
            'h2#call_to_action')
        # Per telephone
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'img#telephone'))
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'p#phone_number'))
        # Or per e-mail
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'img#e_mail'))
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'p#e_mail'))
        # At the bottom of the page, she can find the terms of reference
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'a#terms_of_use'))
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'a#contact'))

        self.fail("Test Incomplet")



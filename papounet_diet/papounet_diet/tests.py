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
        self.browser.find_element_by_id("favicon")
        # First of all, Lily Kala has a look at the page
        # At the top, she can see a navigation bar displaying:
        # The company logo
        self.browser.find_element_by_id("company_logo")
        # The company name
        brand_element = self.browser.find_element_by_class_name('navbar-brand')
        self.assertEqual('Pur Beurre', brand_element.text)
        # The possibility to log in
        self.browser.find_element_by_id("login")
        # To retrieve recorded products
        self.browser.find_element_by_id("carrot")
        # To log off
        self.browser.find_element_by_id("logout")
        # A field to search for an item
        customer_input = self.browser.find_element_by_name(
            'searched_item')
        self.assertEqual(customer_input.get_attribute(
            'placeholder'), 'Votre Recherche')
        # In the upper half of the page, a picture
        self.browser.find_element_by_css_selector('img#background_picture')
        # Contains the motto and a piece of advice
        self.browser.find_element_by_css_selector('h1#motto')
        self.browser.find_element_by_css_selector('h2#advice')
        # and a search field with a validation button (see below)
        # Just below Lily Kala can see the story of the company
        self.browser.find_element_by_css_selector('h2#heroes')
        self.browser.find_element_by_css_selector('p#story')
        # With the pictures of Colette and Remy
        self.browser.find_element_by_css_selector('img#Colette')
        self.browser.find_element_by_css_selector('img#Remy')
        # Still below LK sees an invite to contact the company
        self.browser.find_element_by_css_selector('h2#call_to_action')
        # Per telephone
        self.browser.find_element_by_css_selector('img#telephone')
        self.browser.find_element_by_css_selector('p#phone_number')
        # Or per e-mail
        self.browser.find_element_by_css_selector(
            'img#e_mail')
        self.browser.find_element_by_css_selector('p#e_mail')
        # At the bottom of the page, she can find the terms of reference
        self.browser.find_element_by_css_selector('a#terms_of_use')
        # Then she enters the name of a certain product
        # in a dedicated input box either at the top and validate
        customer_input.send_keys('Nutella')
        self.browser.find_element_by_id('top_button').click()
        # Or in the middle of the page
        # Then she validates
        # A new window opens
        self.browser.switch_to_window('search_results')
        # LK is informed that no product was found
        self.browser.find_element_by_id('error_message')
        # The input field is initialized
        # LK is invited to input another product name
        # And she can validate the search
        # Then a list of max 6 comparable products
        # with an equivalent or better nutrition grade is displayed
        # The name of the product can be seen below the picture
        # LK selects a product to get some details
        # A new window opens, showing the details
        # LK is proposed to record her search for a later use
        # If no, she gets back to the home page
        # If yes, she can start the registering process
        # The register page opens
        # LK processes the registration as a new user (See other User Story)
        # She is informed that she is a registered user
        # And she can record the product.

        self.fail("Test Incomplet")



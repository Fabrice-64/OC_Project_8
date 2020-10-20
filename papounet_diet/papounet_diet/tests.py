from django.test import LiveServerTestCase
from selenium import webdriver


class CustomerTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_customer_selects_better_product(self):
        """
        Test the User story with an optimal scenario
        """
        self.fail('Test Incomplete... still a lot to learn')

        # As a member, Lily Kala authenticates herself upon opening the Website
        # The interface offers the possibility to log in
        # Lily Kala types in her username
        # Then, she types in her password
        # Both are checked in the database
        # if Lily Kala makes a mistake she is proposed to try again
        # In case of validation, a welcome box is displayed
        # On the top right she can see she is logged in.

        # Then she enters the name of a certain product
        # in a dedicated input box

        # Then she validates

        # LK is informed that no product was found
        # The input field is initialized
        # LK is invited to input another product name
        # And she can validate the search

        # Then max 6 products with a better nutrition grade are displayed
        # With the picture, the name and the nturition grade of each product

        # Then she selects a product by clicking on its vignette

        # Then the detailed description of the product pops up,
        # In a box above the active window
        # Including its brand, the shops where it can be purchased
        # And its ingredients

        # Lily Kala is then offered to record the product
        # Lily Kala is informed that the product has been recorded
        # Then Lily Kala can close this box.

    def test_customer_gets_registered(self):
        """
        Test the User story with an optimal scenario
        """
        self.fail('Test Incomplete... still a lot to learn')

        # As a User, Lily Kala gets the opportunity to be registered as such
        # The landing page offers validation while clicking on a button

        # Then Lily Kala types her e-mail
        # If the structure of the e-mail is not correct,
        # she is invited to type it again
        # Then she is invited to type a password
        # If the structure of the password does not match the criteria,
        # she is invited to type it again.
        # Lily Kala is requested to confirm her password by typing it again

        # Then Lily Kala validates the registration

        # Then Lily Kala gets the confirmation she is a registered user

        # Finally Lily Kala is sent back to the landing page
        # and her username is displayed at the top of the page

    def test_customer_finds_recorded_item(self):
        """
        Test the User story with an optimal scenario
        """
        self.fail('Test Incomplete... still a lot to learn')

        # As a registered customer Lily Kala requests authentication
        # A dialog box pops up in the middle of the page
        # Then LK enters her username and her password
        # If the entry is wrong she is invited to do it again
        # If correct, she is informed that she is logged

        # The the interface offers LK to retrieve a former search
        # LK validates this option
        # The recorded products are displayed.
        # The 6 last recorded products are displayed
        # With the picture, the name and the nturition grade of each product

        # She then selects a product by clicking on its vignette

        # Then the detailed description of the product pops up,
        # In a box above the active window
        # Including its picture, brand, the shops where it can be purchased
        # And its ingredients

        # She then can close this dialog box


class SuperUserTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_superuser_functionality(self):
        """
        Test the User story with an optimal scenario
        """
        self.fail('Test Incomplete... still a lot to learn')

        # As a registered superuser FJ requests authentication
        # A dialog box pops up in the middle of the page
        # Then FJ enters his username and his password
        # If the entry is wrong he is invited to do it again
        # If correct, he is informed that she is logged

        # Then he gets access to the list of registered users
        # and to the journal of activities

        # He can choose to download a new category of products
        # And he is informed of the number of products uploaded
        # Or he can update an already existing category.

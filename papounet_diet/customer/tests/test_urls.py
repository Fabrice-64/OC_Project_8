from django.test import Client, TestCase


class SimpleTest(TestCase):
    def test_registration(self):
        client = Client()
        response = client.get('/customer/registration/')
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        client = Client()
        response = client.get('/customer/home/')
        self.assertTemplateUsed(response, 'customer/home.html/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        client = Client()
        response = client.get('/customer/login/')
        self.assertTemplateUsed(response, 'customer/login.html/')
        self.assertEqual(response.status_code, 200)

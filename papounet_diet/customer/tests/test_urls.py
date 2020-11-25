from django.test import Client, TestCase


class SimpleTest(TestCase):
    def test_register(self):
        client = Client()
        response = client.get('/customer/register/')
        self.assertTemplateUsed(response, 'customer/register.html')
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        client = Client()
        response = client.get('/customer/')
        self.assertTemplateUsed(response, 'customer/home.html')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        client = Client()
        response = client.get('/customer/login/')
        self.assertTemplateUsed(response, 'customer/login.html')
        self.assertEqual(response.status_code, 200)

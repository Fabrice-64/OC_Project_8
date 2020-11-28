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
        client.login(username='user', password='pwd')
        response = client.get('/customer/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer/login.html')

    def test_user_logout(self):
        client = Client()
        response = client.get('/customer/logout/')
        self.assertTemplateUsed(response, 'customer/home.html')
        self.assertEqual(response.status_code, 200)


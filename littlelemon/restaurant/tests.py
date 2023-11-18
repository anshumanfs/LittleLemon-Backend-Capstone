from django.test import TestCase
from .models import Menu
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import reverse


class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_item(self):
        item = Menu.objects.get(title="IceCream")
        self.assertEqual(str(item), "IceCream : 80.00")


class MenuViewTestCase(APITestCase):
    def setUp(self):
        # Create a user and a token for testing
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=self.user)
        # Create an item for testing
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_menu_view_with_token(self):
        # Set the authentication credentials with the token
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        # Get the URL of the view
        url = reverse("menu")
        # Send a GET request to the view
        response = self.client.get(url)
        # Check the status code and the content of the response
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from .models import Author

# Create your tests here.
class AuthorApiTest(APITestCase):
    def set_up(self):
        self.autor = Author.objects.create_user("josias", email="josiasn.queiroz@gmail.com", password="1@345678", age=25, bio="Young author")
        self.factory = APIRequestFactory()
    def test_can_get_author(self):
        data = {"id":1, "username":"josias", 'passsword'}
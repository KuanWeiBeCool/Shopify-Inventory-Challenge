from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Product
from django.conf import settings
import os

class TestProduct(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_a = User(username="TestUser", email="test@gmail.com")
        self.user_a.set_password('1234567890')
        self.user_a.save()
        self.client.login(username="TestUser", password="1234567890")
        
        self.product = Product.objects.create(
            user = self.user_a,
            name = "test",
            category = "test_category",
            brand = "test_brand",
        )
        
    def test_info_correct(self):
        self.assertEquals(self.product.user, self.user_a)
        self.assertEquals(self.product.name, "test")
        self.assertEquals(self.product.category, "test_category")
        self.assertEquals(self.product.brand, "test_brand")
        self.assertEquals(self.product.description, None)
        self.assertEquals(self.product.image.url, os.path.join(settings.MEDIA_URL, 'default.png'))
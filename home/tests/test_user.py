from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        user_a = User(username="TestUser", email="test@gmail.com")
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password('1234567890')
        user_a.save()
        
    def test_user_exist(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        
    # def test_login_url(self):
        
    
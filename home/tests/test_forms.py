from django.test import TestCase
from ..forms import CreateForm, RegisterForm
from django.contrib.auth.models import User

class TestCreateForm(TestCase):
    def test_form_valid(self):
        form = CreateForm(data={
            "name" : "test",
            "category" : "test_category",
            "brand" : "test_brand",
            "countInStock" : 10,
            "description" : "test_description",
            "image" : "default.png"
        })
        
        self.assertTrue(form.is_valid())
        
    def test_form_valid_without_description(self):
        form = CreateForm(data={
            "name" : "test",
            "category" : "test_category",
            "brand" : "test_brand",
            "countInStock" : 10,
            "image" : "default.png"
        })
        
        self.assertTrue(form.is_valid())
        
    def test_form_valid_without_image(self):
        form = CreateForm(data={
            "name" : "test",
            "category" : "test_category",
            "brand" : "test_brand",
            "countInStock" : 10,
        })
        
        self.assertTrue(form.is_valid())
                
    def test_form_invalid_without_countInStock(self):
        form = CreateForm(data={
            "name" : "test",
            "category" : "test_category",
            "brand" : "test_brand",
            "image" : "default.png"
        })
        
        self.assertFalse(form.is_valid())
        

        
    def test_form_invalid_without_name(self):
        form = CreateForm(data={
            "category" : "test_category",
            "brand" : "test_brand",
            "countInStock" : 10,
            "image" : "default.png"
        })
        
        self.assertFalse(form.is_valid())
        
    def test_form_invalid_without_category(self):
        form = CreateForm(data={
            "name" : "test",
            "brand" : "test_brand",
            "countInStock" : 10,
            "image" : "default.png"
        })
        
        self.assertFalse(form.is_valid())
        
    def test_form_invalid_without_brand(self):
        form = CreateForm(data={
            "name" : "test",
            "category" : "test_category",
            "countInStock" : 10,
            "image" : "default.png"
        })
        
        self.assertFalse(form.is_valid())
        
    def test_form_invalid_with_negative_inventory(self):
        form = CreateForm(data={
            "name" : "test",
            "category" : "test_category",
            "brand" : "test_brand",
            "countInStock": -1,
            "image" : "default.png"
        })
        
        self.assertFalse(form.is_valid())   
    
class TestRegisterForm(TestCase):
    
    def setUp(self):
        self.user_a = User(username="TestUser", email="test@gmail.com")
        self.user_a.set_password('hello12345')
        self.user_a.save()
    
    def test_form_valid(self):
        form = RegisterForm(data={
            "username" : "testUser2",
            "password1" : "avacado12345",
            "email": "test@126.com",
            "password2" : "avacado12345"
        })
        
        self.assertTrue(form.is_valid())
        
    def test_form_invalid_with_simple_password(self):
        form = RegisterForm(data={
            "username" : "TestUser",
            "password1" : "1234567890",
            "email": "test@126.com",
            "password2" : "1234567890"
        })
        
        self.assertFalse(form.is_valid())
        
    def test_form_invalid_with_same_username(self):
        form = RegisterForm(data={
            "username" : "TestUser",
            "password1" : "avacado12345",
            "email": "test@126.com",
            "password2" : "avacado12345"
        })
        
        self.assertFalse(form.is_valid())
        
    def test_form_invalid_with_different_password(self):
        form = RegisterForm(data={
            "username" : "testUser",
            "password1" : "avacado12345",
            "email": "test@126.com",
            "password2" : "avacado1234"
        })
        
        self.assertFalse(form.is_valid())
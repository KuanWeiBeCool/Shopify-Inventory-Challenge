from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Product

class TestViewsWithoutLogin(TestCase):
    def setUp(self):
        client = Client()
        user_a = User(username="TestUser", email="test@gmail.com")
        user_a.set_password('1234567890')
        user_a.save()
        
        
        Product.objects.create(
            user = user_a,
            name = "test",
            category = "test_category",
            brand = "test_brand",
        )
        
    def test_login_GET(self):
        response = self.client.get(reverse('login'))
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/login.html')
        
        
    def test_confirmation_GET(self):
        response = self.client.get(reverse('confirmation'))
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/confirmation.html')    
 
    def test_logout_GET(self):
        response = self.client.get(reverse('logout'))
        
        self.assertEquals(response.status_code, 302)       
        
    def test_home_GET(self):
        response = self.client.get(reverse('home'))
        
        self.assertEquals(response.status_code, 302)
        
    def test_search_results_GET(self):
        response = self.client.get(reverse('search-results'))
        
        self.assertEquals(response.status_code, 302)    
    
    def test_create_GET(self):
        response = self.client.get(reverse('create'))
        
        self.assertEquals(response.status_code, 302)

    def test_update_GET(self):
        response = self.client.get(reverse('update', args=[1]))
        
        self.assertEquals(response.status_code, 302)         
    
    def test_delete_GET(self):
        response = self.client.get(reverse('delete', args=[1]))
        
        self.assertEquals(response.status_code, 302)        
    
    
class TestViewsWithLogin(TestCase):
    def setUp(self):
        self.client = Client()
        user_a = User(username="TestUser", email="test@gmail.com")
        user_a.set_password('1234567890')
        user_a.save()
        self.client.login(username="TestUser", password="1234567890")
        
        Product.objects.create(
            user = user_a,
            name = "test",
            category = "test_category",
            brand = "test_brand",
        )
        
 
    def test_home_GET(self):     
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')           
        
    def test_search_results_GET(self):     
        response = self.client.get(reverse('search-results'))
        self.assertEquals(response.status_code, 200)    
        self.assertTemplateUsed(response, 'home/home.html')       
        
    def test_create_GET(self):     
        response = self.client.get(reverse('create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/product_post.html')  
    
    def test_update_GET(self):     
        response = self.client.get(reverse('update', args=[1]))
        self.assertEquals(response.status_code, 200)         
        self.assertTemplateUsed(response, 'home/product_post.html')     
  
    def test_delete_GET(self):     
        response = self.client.get(reverse('delete', args=[1]))
        self.assertEquals(response.status_code, 302)      
        
    def test_logout_GET(self):     
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)  

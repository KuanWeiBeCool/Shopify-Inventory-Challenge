from django.contrib import admin
from django.test import TestCase
from django.urls import reverse, resolve
from ..loginViews import register_login, logout_user, confirmation
from ..CRUDViews import InventoryView, ProductCreateView, ProductUpdateView, ProductDeleteView

class TestUrlsViewsConnection(TestCase):
    
    # Check if urls are correctly resoved to the corresponding view functions
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, register_login)
        
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_user)
        
    def test_confirmation_url_is_resolved(self):
        url = reverse('confirmation')
        self.assertEqual(resolve(url).func, confirmation)
        
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, InventoryView)
    
    def test_home_url_is_resolved(self):
        url = reverse('search-results')
        self.assertEqual(resolve(url).func, InventoryView)
        
    def test_create_url_is_resolved(self):
        # class based view compare names
        url = reverse('create')
        self.assertEqual(resolve(url).func.__name__, ProductCreateView.as_view().__name__)
        
    def test_update_url_is_resolved(self):
        # class based view compare names
        url = reverse('update', args=[1])
        self.assertEqual(resolve(url).func.__name__, ProductUpdateView.as_view().__name__)   
    
    def test_delete_url_is_resolved(self):
        url = reverse('delete', args=[1])
        self.assertEqual(resolve(url).func, ProductDeleteView)   
   
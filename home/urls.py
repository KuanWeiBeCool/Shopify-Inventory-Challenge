from .loginViews import register_login, logout_user, confirmation
from .CRUDViews import InventoryView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.urls import path

urlpatterns = [
    path('', register_login, name="login"),
    path('logout/', logout_user, name="logout"),
    path('register_complete/', confirmation, name="confirmation"),  
    path('inventory/', InventoryView, name="home"),
    path('inventory/search/', InventoryView, name="search-results"),
    path('inventory/new/', ProductCreateView.as_view() , name="create"),   
    path('inventory/update/<int:pk>', ProductUpdateView.as_view() , name="update"),   
    path('inventory/delete/<int:pk>', ProductDeleteView , name="delete"),   
]

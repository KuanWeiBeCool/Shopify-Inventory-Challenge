from . import views
from django.urls import path

urlpatterns = [
    path('', views.register_login, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register_complete/', views.confirmation, name="confirmation"),  
    path('inventory/', views.InventoryView, name="home"),
    path('inventory/search/', views.InventoryView, name="search-results"),
    path('inventory/new/', views.ProductCreateView.as_view() , name="create"),   
    path('inventory/update/<int:pk>', views.ProductUpdateView.as_view() , name="update"),   
    path('inventory/delete/<int:pk>', views.ProductDeleteView , name="delete"),   
]

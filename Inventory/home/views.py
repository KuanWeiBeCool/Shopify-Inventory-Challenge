from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from .filters import ProductFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Product
from .forms import CreateForm, RegisterForm, FilterForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
# Create your views here.

@login_required
def InventoryView(request):
    '''
    Main view for showing list of inventories.
    '''
    products = request.user.product_set.all().order_by('date_posted')
    
    product_filter = ProductFilter(request.GET, queryset=products)
    products = product_filter.qs
    context = {'products': products, 'product_filter':product_filter}
    return render(request, 'home/home.html', context)






# class InventoryView(LoginRequiredMixin, ListView):
#     '''
#     Main view for showing list of inventories.
#     '''
#     model = Product
#     template_name = 'home/home.html'
#     context_object_name = 'products'
#     # paginate_by = 1 # show 1 posts per page
    
#     # Override get_queryset for the user
#     def get_queryset(self):
#         return self.request.user.product_set.all().order_by('date_posted')
    
# class SearchResultsView(ListView):
#     '''
#     This view is for the search results
#     '''
#     model = Product
#     template_name = 'home/search_results.html'
#     context_object_name = 'products'
#     paginate_by = 1 # show 1 posts per page
    
#     def get_queryset(self):
#         query = self.request.GET.get('search')
#         filter_field = self.request.GET.get('filter_field')
#         inventory_min = self.request.GET.get('inventory_min')
#         inventory_max = self.request.GET.get('inventory_min')
        
#         if filter_field == "all":
#             if inventory_min:
#                 result =  Product.objects.filter(
#                         Q(name__icontains=query) |
#                         Q(type__icontains=query) |
#                         Q(brand__icontains=query)
#                     )
#         elif filter_field == "name":
#             result = Product.objects.filter(Q(name__icontains=query))
#         elif filter_field == "type":
#             result = Product.objects.filter(Q(type__icontains=query))    
  
#         elif filter_field == "brand":
#             result = Product.objects.filter(Q(brand__icontains=query))  
            
#         if result:
#             if inventory_min:
                
#             return result.order_by('-date_posted')
#         else:
#             return result

    
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['form'] = FilterForm(initial={
#             'search': self.request.GET.get('search', ''),
#             'filter_field': self.request.GET.get('filter_field', ''),
#         })

#         return context
    
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    '''
    View for create a new product
    '''
    model = Product
    form_class = CreateForm
    success_url = reverse_lazy('home')
    template_name = "home/product_post.html"
     
    # Set the user of the product to be the user currently login
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    This view is for updating the product information
    '''
    model = Product
    form_class = CreateForm
    success_url = reverse_lazy('home')
    template_name = "home/product_post.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # Get the form pre-filled by the original brand
        original_product = self.get_form_kwargs().get('instance')
        context['form'] = CreateForm(initial={
            'name': self.request.GET.get('name', original_product.name),
            'description': self.request.GET.get('description', original_product.description),
            'category': self.request.GET.get('category', original_product.category),         
            'brand': self.request.GET.get('brand', original_product.brand),   
            'countInStock': self.request.GET.get('countInStock', original_product.countInStock),   
            'image': self.request.GET.get('image', original_product.image),     
        })
        
        return context
    
    # Set the user of the product to be the user currently login
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)   
    
    # Test to see if the user that attempts to update the product is actually the user loggin
    def test_func(self):
        product = self.get_object()
        if self.request.user == product.user:
            return True
        return False
    

def ProductDeleteView(request, pk):
    entry = Product.objects.get(id=pk)
    entry.delete()
    return redirect('home')

def register_login(request):
    '''
    View for both sign in and sign up page.
    '''
    form = RegisterForm()
    if request.method == "POST":
        if 'signUp' in request.POST:
            # Register
            form = RegisterForm(request.POST)
            
            if form.is_valid():
                form.save()
                username = request.POST['username']
                password = request.POST['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('confirmation')
            # leave sign_up checked so that the page will remain on the sign up page
            return render(request, 'home/login.html', {'form':form, 'sign_up':"checked", 'sign_in':""})
        else:
            # Login
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('home')
            else:
                messages.error(request, "Whoops, your username and password didn't match. Please try again.")
                return render(request, 'home/login.html', {'form':form, 'sign_up':"", 'sign_in':"checked"})
            # leave sign_up checked so that the page will remain on the sign up page

    # When just entered the page, by default will be sign in page
    return render(request, 'home/login.html', {'form':form, 'sign_up':"", 'sign_in':"checked"})


def confirmation(request):
    '''
    View for successfully signed up.
    '''
    return render(request, "home/confirmation.html")

def logout_user(request):
    '''
    View for the logout. 
    '''
    logout(request)
    return redirect('login')

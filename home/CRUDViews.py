from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView, UpdateView)
from .filters import ProductFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product
from .forms import CreateForm
from django.urls import reverse_lazy

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



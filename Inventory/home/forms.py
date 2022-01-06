from django.contrib.auth.models import User
from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput

class CreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'brand', 'countInStock', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'}),
            'brand': forms.TextInput(attrs={'class':'form-control'}),
            'countInStock': forms.NumberInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
        

class RegisterForm(UserCreationForm):
    username = forms.RegexField(
        label=("Username"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text=("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': ("Username may contain only letters, numbers and "
                        "@/./+/-/_ characters.")},
        widget=TextInput(attrs={'class': 'input',
                                'required': 'true',
                                # 'placeholder': 'Username'
        })
    )

    email = forms.EmailField(label=("Email"), widget=forms.EmailInput(attrs={'class': 'input', # form-control
                                  'type': 'email',
                                #   'placeholder': 'Email address',
                                  'required': 'true'
    }))

    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'input', # form-control (for register.html)
                                        'type': 'password',
                                        'required': 'true',
                                        # 'placeholder': 'Password',
                                        

        })
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'input', # form-control (for register.html)
                                        'type': 'password',
                                        'required': 'true',
                                        # 'placeholder': "Confirm Password"
        }),
        help_text=("Enter the same password as above, for verification.")
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")
        if password != confirm_password:
            raise forms.ValidationError("Your passwords didn't match!")
        

class FilterForm(forms.Form):
    '''
    A filter form for searching bar
    '''
    FILTER_CHOICES = (
        ('all', 'All'),
        ('name', 'Name'),
        ('type', 'Type'),
        ('brand', 'Brand'),
    )
    

    search = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control mr-sm-2', 
                                        'type': 'search',
                                        'placeholder': "What Post Do You Want To See",
        }))
    filter_field = forms.ChoiceField(choices=FILTER_CHOICES, widget=forms.Select(attrs={'class':'form-control mr-sm-2'}))
    inventory_min = forms.IntegerField(required=False, min_value=0, widget=forms.NumberInput(attrs={'class':'form-control mr-sm-2'}))
    inventory_max = forms.IntegerField(required=False, min_value=0, widget=forms.NumberInput(attrs={'class':'form-control mr-sm-2'}))
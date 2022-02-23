from django import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm

from .models import Customer, Address


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["full_name", "phone", "address_line", "address_line2", "town_city", "postcode"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {"class":"form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["phone"].widget.attrs.update(
            {"class":"form-control mb-2 account-form", "placeholder": "Phone Number"}
        )
        self.fields["address_line"].widget.attrs.update(
            {"class":"form-control mb-2 account-form", "placeholder": "Address Line 1"}
        )
        self.fields["address_line2"].widget.attrs.update(
            {"class":"form-control mb-2 account-form", "placeholder": "Address Line 2"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class":"form-control mb-2 account-form", "placeholder": "Town/City"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class":"form-control mb-2 account-form", "placeholder": "Postcode"}
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label="Enter Username",min_length=4,max_length=50,help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required':"Sorry, you will need an email"})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        model = Customer
        fields = ('user_name', 'email')

    
    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = Customer.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("username already exists")
        return user_name
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Posswords do not match')
        return cd['password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another email, that is already taken')
        return email

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['user_name'].widget.attrs.update({'class':'form-control mb-3', 'placeholder':'Username'})
        self.fields['email'].widget.attrs.update({'class':'form-control mb-3', 'placeholder':'E-mail'})
        self.fields['password'].widget.attrs.update({'class':'form-control mb-3', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control mb-3', 'placeholder':'Repeat Password'})


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(
        label='Account email(can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Firstname', min_length=4, max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))

    class Meta:
        model = Customer
        fields = ('email','first_name')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].required = True
        self.fields['email'].required = True 



class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        u = Customer.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunatley we can not fint that email addres'
            )
        return email 

class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))
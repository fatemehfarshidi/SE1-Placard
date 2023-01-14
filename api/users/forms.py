from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer

class RegistrationForm(forms.ModelForm):

    username = forms.CharField(min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = Customer.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': '  Sonbol_32'})
        self.fields['email'].widget.attrs.update({'placeholder': '  Sonbol@aut.com'})
        self.fields['password'].widget.attrs.update({'placeholder': '  ********'})
        self.fields['password2'].widget.attrs.update({'placeholder': '  ********'})

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  نام کاربری'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '  رمز عبور'}))
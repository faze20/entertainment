from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

# classes here............................................................
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('telephone', 'address')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

# django sign up from render

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(widget=forms.PasswordInput())

    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

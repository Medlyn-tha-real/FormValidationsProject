from django import forms # type: ignore

from validationsdemoapp.models import UserRegistration  # type: ignore
from django.forms import PasswordInput, RadioSelect, Select, DateInput, EmailInput, URLInput # type: ignore

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = UserRegistration
        fields = '__all__'

        genders = [{"male", "Male"}, {"female", "Female"}]

        countries = [("select", "Please Choose Country"),
                     ("USA", "USA"),
                     ("Finland", "Finland"),
                     ("Canada", "Canada"),
                     ("Australia", "Australia"),
                     ]
        
        widgets = {
            "password": PasswordInput(),
            "confirm_password": PasswordInput(),
            "gender": RadioSelect(choices=genders),
            "country": Select(choices=countries),
            "date_of_birth": DateInput(attrs={"type": "date"}),
            "email": EmailInput(),
            "website_url": URLInput()
        }





























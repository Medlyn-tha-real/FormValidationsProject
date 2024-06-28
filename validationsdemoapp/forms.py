from django import forms # type: ignore

from validationsdemoapp.models import UserRegistration  # type: ignore
from django.forms import PasswordInput, RadioSelect, Select, DateInput, EmailInput, URLInput # type: ignore
import re
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
    # Field Level Validations
    def clean_phone_number(self):
        iphonenumber = self.cleaned_data.get("phone_number")
        if iphonenumber:
            pattern = re.compile(r"(0|81)?[0-9][0-9]{7}")
            if not re.fullmatch(pattern, iphonenumber):
                raise forms.ValidationError("Invalid Phone Number! Example : 8123456789.")
            return iphonenumber
    # Form Level Validation
    def clean(self):
        cleaned_data = super().clean()
        ipassword = cleaned_data.get("password")
        iconfirm_password = cleaned_data.get("confirm_password")
        if ipassword and iconfirm_password:
            if ipassword != iconfirm_password:
                raise forms.ValidationError("Passwords do not match!")
        
        iusername = cleaned_data.get("username")
        ipassword = cleaned_data.get("password")

        if ipassword and iusername:
            if ipassword == iusername:
                raise forms.ValidationError("Username and password should not be same!!")
            
        country = cleaned_data.get("country")
        if country == "select":
            raise forms.ValidationError("Please choose a country.")
        
        terms_conditions = cleaned_data.get("terms_confirm")
        if not terms_conditions:
            raise forms.ValidationError("Please agree to terms and conditions!!")
        
        return cleaned_data
        

    
    
































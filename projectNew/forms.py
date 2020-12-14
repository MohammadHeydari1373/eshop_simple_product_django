from django import forms
from django.contrib.auth import get_user_model

#object of usermodel
User = get_user_model()

class Contact(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Enter your fullname'
                                                             }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Enter your Email'}))
    textarea = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'Enter your message'}))
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not '@gmail.com' in email:
            raise  forms.ValidationError("hdldgd")
        return email

class LoginForm(forms.Form) :
    username = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control",
                                                             "placeholder" : "username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control",
                                                             "placeholder" : "password"}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control",
                                                             "placeholder" : "username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class" : "form-control",
                                                             "placeholder" : "username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class" : "form-control",
                                                             "placeholder" : "password"}))
    password2 = forms.CharField(label= 'comfirm password' , widget=forms.PasswordInput(attrs={"class" : "form-control",
                                                                   "placeholder" : "password",
                                                                     }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username dose exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email dose exists")
        return email

    def clean(self):
        data = self.cleaned_data
        password =  self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2 :
            raise forms.ValidationError('has not mach password')
        return data

#get_user for register
#validation for unique data





from django.shortcuts import render , redirect
from projectNew.forms import Contact ,LoginForm , RegisterForm
from django.contrib.auth import  authenticate , login , get_user_model

#object getusermoel
User = get_user_model()
# Create your views here.
def home_page(request) :
    context = {
        "title" : "صفحه اصلی",
        "text":"به صفحه اصلی خوش آمدید ",

    }
    if request.user.is_authenticated :
        context['newText'] = "به لاگین خوش امدید"

    return render(request, "index.html", context)
def about_us(request) :
    context = {
        "title": "در باره ی ما",
        "text" :"نشانی ما را در این قسمت بینید",

    }
    return render(request, "about_us.html", context)
def contact_page(request) :
    form = Contact(request.POST or None)
    context = {
        "title": "تماس با ما",
        "text" :"this is the  contact_page",
        'form' : form

    }

    if form.is_valid() :
        print(form.cleaned_data)


    return render(request, "contact/contact_us.html", context)
def login_page(requset) :
    #print(requset.user.is_authenticated)
    form = LoginForm(requset.POST or None)
    context = {
        "title": "login",
        "text" :"the form login :",
        'form' : form

    }
    if form.is_valid() :
        print(form.cleaned_data)
        print(f"username is : {form.cleaned_data.get('username')}")
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(requset, username =username ,password = password)
        print(user)
        if user is not None :
            login(requset , user)

            context['form'] = LoginForm()
            print('ok')
            return redirect('/')
        else :
            print('Error')




    return render(requset, 'auth/login.html', context)

def register_page(request) :
    form = RegisterForm(request.POST or None)
    context = {
        "title": "Register",
        "text": "the Reister form :",
        'form' : form
    }


    if form.is_valid() :
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        new_user = User.objects.create_user(username = username , password = password , email=email)
        print(new_user)
    return render(request, 'auth/register.html', context)
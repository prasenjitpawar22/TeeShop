from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from .forms import LoginForm, RegisterForm

User = get_user_model()

def registerPage(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1 # 1 == True
    return render(request, "register.html", {"form": form})


def loginPage(request):
    if request.user.is_authenticated:
        # alert message user already logged in!
        return redirect('/')
    else:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user != None:
                # user is valid and active -> is_active
                # request.user == user
                login(request, user)
                return redirect("/")
            else:
                # attempt = request.session.get("attempt") or 0
                # request.session['attempt'] = attempt + 1
                # return redirect("/invalid-password")
                request.session['invalid_user'] = 1 # 1 == True
        return render(request, "login.html", {"form": form})

def logoutPage(request):
    logout(request)
    # request.user == Anon User
    return redirect("login")
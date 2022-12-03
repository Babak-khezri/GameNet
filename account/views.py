from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserForm
from .models import User

# Create your views here.


def login_view(request):

    if request.user.is_authenticated:  # user is already authenticated
        return redirect('/')

    form = AuthenticationForm(data=request.POST or None)

    error = None

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            error = "کاربر پیدا نشد !!!"

    return render(request, 'account/login_page.html', {'form': form, 'error': error})


def logout_view(request):
    logout(request)
    return redirect('account:login')


def employee_list_view(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            salary = form.cleaned_data['salary']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name,email=email, last_name=last_name,
                        salary=salary, username=username, password=password)
            user.save()

    users = User.objects.all()
    context = {'users': users,
               'form': form, }
    return render(request, 'account/employee_list.html', context)

def forget_password_view(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
        except :
            pass
    return render(request, 'account/forget_password.html')
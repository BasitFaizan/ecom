from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from productpage.models import products
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cPassword = request.POST.get('cPassword')
        if password != cPassword:
            messages.warning(request,'Password not match')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,"Email is already in use")
        else:
            user =User.objects.create_user(email,email,password)
            user.save()
            messages.success(request,'You have successfully created your account')
            return redirect('/login')
    return render(request, 'signin.html')

def log_in(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials please try again.')
    return render(request, 'login.html')


def contact(request):
    return render(request, 'contact.html')

def log_out(request):
    logout(request)
    return redirect('/')


def menu(request):
    allProd = []
    # allCateg = products.objects.all()
    allCateg = products.objects.values('category','id')
    prod = {item['category'] for item in allCateg}
    for prod in prod:
        categ = products.objects.filter(category=prod)
        print(categ)
        allProd.append(categ)
        # print(prod)
    return render(request,'menu.html',{'allProd':allProd})

def product(request,id):
    print(id)
    product = products.objects.filter(id=id)
    print(product)
    return render(request,'productPage.html',{'product':product})
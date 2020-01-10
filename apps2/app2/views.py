from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from app2.models import salon, salon1, Contact, sal


def home(request):
    dic = salon.objects.all()
    return render(request, "home.html", {'dic': dic})


def about(request):
    return render(request, "about.html")


def products(request):
    dic = sal.objects.all()
    return render(request, "products.html", {'dic': dic})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", '')
        email = request.POST.get("email", '')
        phone = request.POST.get("phone", '')
        address = request.POST.get("address", '')
        contactt = Contact(name=name, email=email, phone=phone, address=address)
        contactt.save()
        return HttpResponse("contact saved in database")
        return redirect("/contact")
    return render(request, "contact.html")


def serve(request):
    dic = salon.objects.all()
    return render(request, "serve.html", {'dic': dic})


def price(request):
    return render(request, "price.html")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken....")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken....')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('/login')
        else:
            messages.info(request, 'password not matching....')
            return redirect('/register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')
        return render(request,'home.html')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def prac(request):
    dic = salon1.objects.all()
    return render(request, "prac.html", {'dic': dic})


def pp(request):
    return render(request, "pp.html")

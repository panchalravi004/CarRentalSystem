from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.EmailBackEnd import EmailBackEnd
from app.decorators import *
from app.models import *

def getCurrentURL(request):
    return request.META.get('HTTP_REFERER', '/default-url/')

@unathenticated_user
def REGISTER(request):
    return render(request,"registration/register.html")

@unathenticated_user
def LOGIN(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('pass')
        user = EmailBackEnd.authenticate(request,username=email,password=pwd)

        if user != None:

            isCustomerExists = Customer.objects.filter(user=user.id)
            isEmployeeExists = Employee.objects.filter(user=user.id)

            print(f'Customer : {isCustomerExists.exists()}')
            print(f'Employee : {isEmployeeExists.exists()}')

            if isCustomerExists.exists():
                login(request,user)
                return redirect('chome')
            elif isEmployeeExists.exists():
                login(request,user)
                return redirect('ehome')
            
            messages.warning(request,'User does\'t have access !')
            return redirect(getCurrentURL(request))
        else:
            messages.warning(request,'Email or Password Are Invalid !')
            return redirect('login')

    messages.warning(request,'Invalid request method !')
    return redirect(getCurrentURL(request))

@unathenticated_user
def CREATEACCOUNT(request):

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pwd = request.POST.get('pass')

        isUserExists = User.objects.filter(email=email)

        if isUserExists.exists():
            messages.warning(request,'User with email already exists !')
            return redirect(getCurrentURL(request))

        # Create Customer Record After Creating User
        # user = User(
        #     username=name,
        #     email=email,
        # )
        # user.set_password(pwd)
        # user.save()

        customer = Customer(
            # user=user,
            name=name,
            email=email,
            phone=phone,
            address=address,
            password=pwd
        )

        customer.save()

        return redirect('login')
    
    messages.warning(request,'Invalid request method !')
    return redirect(getCurrentURL(request))

@login_required
def LOGOUT(request):
    logout(request)
    return redirect('login')
from django.shortcuts import redirect
from app.models import *

def getCurrentURL(request):
    return request.META.get('HTTP_REFERER', '/default-url/')

def unathenticated_user(view_func):
    def wrapper_fuc(request, *args, **kwargs):
        if request.user.is_authenticated:
            isCustomerExists = Customer.objects.filter(user=request.user.id)
            isEmployeeExists = Employee.objects.filter(user=request.user.id)
            if isCustomerExists.exists():
                return redirect('chome')
            if isEmployeeExists.exists():
                return redirect('ehome')
            
            return redirect('register')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_fuc

def restricted_user(type):
    def decorator(view_func):
        def wrapper_fuc(request, *args, **kwargs):
            isCustomerExists = Customer.objects.filter(user=request.user.id)
            isEmployeeExists = Employee.objects.filter(user=request.user.id)
            if type == 'CUSTOMER' and isCustomerExists.exists():
                return redirect('chome')
            if type == 'EMPLOYEE' and isEmployeeExists.exists():
                return redirect('ehome')
            return view_func(request, *args, **kwargs)
        return wrapper_fuc
    return decorator


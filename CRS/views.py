from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from app.decorators import *
from app.models import *

def getCurrentURL(request):
    return request.META.get('HTTP_REFERER', '/default-url/')

def BASE(request):
          
    return render(request,"base.html")

@login_required
@restricted_user('EMPLOYEE')
def CUSTOMER_HOME(request):

    customer = Customer.objects.get(user=request.user)

    carList = Car.objects.filter(status='Available').order_by('-created_date')
    rentalList = Rental.objects.filter(status='Accepted', customer=customer).order_by('-created_date')
    requestList = Rental.objects.filter(Q(status='Pending') | Q(status='Not Available'), customer=customer).order_by('-created_date')

    data = {
        'carList': carList,
        'rentalList': rentalList,
        'requestList': requestList,
    }
          
    return render(request, "customer-home.html", data)

@login_required
@restricted_user('CUSTOMER')
def EMPLOYEE_HOME(request):

    employee = Employee.objects.get(user=request.user)

    carList = Car.objects.all().order_by('-created_date')
    rentalList = Rental.objects.filter(status='Accepted', employee=employee).order_by('-created_date')
    requestList = Rental.objects.filter(Q(status='Pending') | Q(status='Not Available')).order_by('-status', 'start_date', 'car__name')

    data = {
        'carList': carList,
        'rentalList': rentalList,
        'requestList': requestList,
    }
          
    return render(request, "employee-home.html", data)

@login_required
@restricted_user('CUSTOMER')
def ADD_NEW_CAR(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        type = request.POST.get('type')
        year = request.POST.get('year')

        car = Car(
            name=name,
            model=model,
            type=type,
            year=int(year),
            status='Available'
        )

        car.save()
        messages.success(request,'New car added successfully!')
        return redirect('ehome')

    messages.warning(request,'Invalid request method!')
    return redirect(getCurrentURL(request))

@login_required
@restricted_user('CUSTOMER')
def UPDATE_STATUS(request, id, status):
    car = Car.objects.get(id=int(id))
    if car != None:
        if status == 'Available':
            car.status = 'Not Available'
        if status == 'Not Available':
            car.status = 'Available'
        car.save()
        messages.success(request,'Status updated successfully!')

    return redirect(getCurrentURL(request))

@login_required
@restricted_user('CUSTOMER')
def CAR_REQUEST_UPDATE(request, id, status):
    employee = Employee.objects.get(user=request.user)
    rental = Rental.objects.get(id=int(id))
    if rental != None:
        if rental.status != 'Accepted':

            if status == 'Accepted':
                existing_request = Rental.objects.filter(~Q(id=rental.id), car=rental.car, status='Pending').filter((Q(start_date__lte = rental.start_date) & Q(end_date__gte = rental.start_date)) | (Q(start_date__lte = rental.end_date) & Q(end_date__gte = rental.end_date)))
                
                if existing_request.exists():
                    existing_request.update(status='Not Available')
        
            rental.status = status
            rental.employee = employee
            rental.save()
            messages.success(request,'Status updated successfully!')
        else:
            messages.info(request,'Request already accepted by other agent!')

    return redirect(getCurrentURL(request))

@login_required
@restricted_user('CUSTOMER')
def UPDATE_CAR(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        model = request.POST.get('model')
        type = request.POST.get('type')
        year = request.POST.get('year')

        car = Car.objects.get(id=int(id))
        car.name = name
        car.model = model
        car.type = type
        car.year = int(year)
        car.save()

        messages.success(request,'Car details updated successfully!')
        return redirect('ehome')
    
    messages.warning(request,'Invalid request method!')
    return redirect(getCurrentURL(request))
    
@login_required
@restricted_user('EMPLOYEE')
def CAR_RENTAL_REQUEST(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')

        customer = Customer.objects.get(user=request.user)
        car = Car.objects.get(id=int(id))

        # Check any existing record available of request with accepted status
        # and selected similar start date and end date

        existing_request = Rental.objects.filter(car=car, status='Accepted').filter((Q(start_date__lte = startdate) & Q(end_date__gte = startdate)) | (Q(start_date__lte = enddate) & Q(end_date__gte = enddate)))

        is_already_request = Rental.objects.filter(car=car, status='Pending', start_date=startdate, end_date=enddate, customer=customer)

        if existing_request.exists():
            messages.warning(request,f'{car.name} is not available for selected dates!')
            return redirect('chome')
        elif is_already_request.exists():
            messages.warning(request,f'You Already requested {car.name} for selected dates!')
            return redirect('chome')
        else:
            rental = Rental(
                start_date = startdate,
                end_date = enddate,
                customer = customer,
                car = car,
                status = 'Pending'
            )

            rental.save()

            messages.success(request,'Rental request send successfully!')
            return redirect('chome')
    
    messages.warning(request,'Invalid request method!')
    return redirect(getCurrentURL(request))
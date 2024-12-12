from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    position = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
        
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=15)
    created_date = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.name
    
class Car(models.Model):
    TYPE = [ 
        ('Hatchback', 'Hatchback'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('MUV', 'MUV'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Pickup Truck', 'Pickup Truck')
    ]

    STATUS = [ 
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    ]

    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    type = models.CharField(max_length=100, choices=TYPE)
    status = models.CharField(max_length=100, choices=STATUS)
    created_date = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.name
    
class Rental(models.Model):

    STATUS = [ 
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Not Available', 'Not Available')
    ]

    start_date = models.DateField()
    end_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS)
    created_date = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.car.name+' | '+str(self.start_date)+' | '+self.status


# Model Signals Callback Method
@receiver(post_save, sender=Employee)
def employee_post_save(sender, instance, created, **kwargs):
        if created:
            user = User(
                first_name=instance.name,
                username=instance.email,
                email=instance.email,
            )
            user.set_password(instance.password)
            user.save()

            instance.user = user
            instance.save()
        if not created:
            user = instance.user
            user.first_name=instance.name
            user.username = instance.email
            user.email = instance.email
            user.set_password(instance.password)
            user.save()

@receiver(post_delete, sender=Employee)
def employee_post_delete(sender, instance, *args, **kwargs):
    try:
        instance.user.delete()
    except Exception as e:
        print('Employee Cascade Delete: User not found!')

@receiver(post_save, sender=Customer)
def customer_post_save(sender, instance, created, **kwargs):
        if created:
            user = User(
                first_name=instance.name,
                username=instance.email,
                email=instance.email,
            )
            user.set_password(instance.password)
            user.save()

            instance.user = user
            instance.save()
        if not created:
            user = instance.user
            user.first_name=instance.name
            user.username = instance.email
            user.email = instance.email
            user.set_password(instance.password)
            user.save()

@receiver(post_delete, sender=Customer)
def customer_post_delete(sender, instance, *args, **kwargs):
    try:
        instance.user.delete()
    except Exception as e:
        print('Customer Cascade Delete: User not found!')

# post_save.connect(create_user, sender=Employee)
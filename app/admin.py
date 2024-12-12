from django.contrib import admin
from app.models import *

class CustomerAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "phone")
  exclude = ('user',)

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ("name", "email", "position")
  exclude = ('user',)

class CarAdmin(admin.ModelAdmin):
  list_display = ("name", "model", "year", "type", "status")

class RentalAdmin(admin.ModelAdmin):
  list_display = ("car", "start_date", "end_date", "status", "customer", "employee")

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Rental, RentalAdmin)
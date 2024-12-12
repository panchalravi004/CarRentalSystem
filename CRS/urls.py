"""
URL configuration for CRS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views, user_login

admin.site.site_header = "Car Rental System"
admin.site.site_title = "Car Rental System"
admin.site.index_title = "Welcome to Car Rental System"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name="base"),
    path('', views.CUSTOMER_HOME,name="chome"),
    path('chome', views.CUSTOMER_HOME,name="chome"),
    path('ehome', views.EMPLOYEE_HOME,name="ehome"),
    path('car/new', views.ADD_NEW_CAR,name="add_new_car"),
    path('car/update', views.UPDATE_CAR,name="update_car"),
    path('car/request', views.CAR_RENTAL_REQUEST,name="rental_request_car"),
    path('car-update-status/<int:id>/<str:status>', views.UPDATE_STATUS,name="update_status"),
    path('car-request-update/<int:id>/<str:status>', views.CAR_REQUEST_UPDATE,name="car_request_update"),

    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register', user_login.REGISTER,name="register"),
    path('accounts/create-account', user_login.CREATEACCOUNT,name="create-account"),
    path('dologin/', user_login.LOGIN,name="dologin"),
    path('logout/',user_login.LOGOUT,name='logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

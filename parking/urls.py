"""parking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from django.contrib import admin
from parkingapp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('drivers/driver/', DriverList.as_view()),
    path('drivers/driver/<int:pk>/', DriverDetail.as_view()),
    path('vehicles/vehicle/', VehicleList.as_view()),
    path('vehicles/vehicle/<int:pk>/', VehicleDetail.as_view()),
    path('vehicles/set_driver/<int:pk>/', DriverInOutDetail.as_view()),
]


from .serializers import DriverSerializer, VehicleSerializer, DriverInOutSerializer
from datetime import datetime as dt
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Driver, Vehicle


# output of the list of drivers
# creating a new driver
# output a list of drivers who created after 10-11-2021/output of the list of drivers who created before 16-11-2021

class DriverList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        date_gte = self.request.query_params.get('created_at__gte')
        date_lte = self.request.query_params.get('created_at__lte')
        if date_gte is not None:
            date_gte = dt.strptime(date_gte, '%d-%m-%Y')
            queryset = queryset.filter(created_at__gte=date_gte)
        elif date_lte is not None:
            date_lte = dt.strptime(date_lte, '%d-%m-%Y')
            queryset = queryset.filter(created_at__lte=date_lte)
        return queryset


# obtaining information on a specific driver
# driver editing
# remove the driver
class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny)
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


# put the driver in the car / drop off driver from the car
class DriverInOutDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny)
    queryset = Vehicle.objects.all()
    serializer_class = DriverInOutSerializer


# output car list
class VehicleList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = VehicleSerializer

    # output of the list of cars with drivers
    # output of the list of cars without drivers
    def handler(self):
        queryset = Vehicle.objects.all()
        with_drivers = self.request.query_params.get('with_drivers')
        if with_drivers == 'yes':
            queryset = queryset.filter(driver_id__isnull=False)
        elif with_drivers == 'no':
            queryset = queryset.filter(driver_id__isnull=True)
        return queryset


# getting information on a specific car
# editing car
# remove the car
class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime 
from .models import DriverInfo, CarInfo, Tracker


class CheckUser(APIView):
    def get(self, request, licence, car_no):
        try:
            driver_obj = DriverInfo.objects.get(licence_no=licence)
            car_obj = CarInfo.objects.get(car_no=car_no)

            Tracker.objects.create(driver=driver_obj, car=car_obj)

            if datetime.date.today() >= driver_obj.exp_date:
                return Response({'status': 'No'})
            return Response({'status': 'ok'})

        except Exception as e:
            print(e)
            return Response({'status': 'No'})
        return Response({'status': 'ok'})


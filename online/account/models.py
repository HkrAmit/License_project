from django.db import models


class DriverInfo(models.Model):
    name = models.CharField(max_length=100)
    licence_no = models.CharField(max_length=100)
    exp_date = models.DateField()

    def __str__(self):
        return self.licence_no


class CarInfo(models.Model):
    car_no = models.CharField(max_length=100)
    issu_date = models.DateField()
    exp_date = models.DateField()

    def __str__(self):
        return self.car_no


class Tracker(models.Model):
    driver = models.ForeignKey(DriverInfo, on_delete=models.CASCADE)
    car = models.ForeignKey(CarInfo, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
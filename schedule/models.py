from django.db import models

class Stop(models.Model):
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.location

class Route(models.Model):
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.number

class Schedule(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    stops = models.ManyToManyField(Stop)
    

    def __str__(self):
        return f"{self.route} ({self.departure_time} - {self.arrival_time})"
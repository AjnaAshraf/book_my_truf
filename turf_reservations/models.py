from django.db import models
from turf.models import Turf

class Bookings(models.Model):

    team = models.CharField(max_length=200)

    phone_number = models.CharField(max_length=200)

    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)

    date = models.DateField()

    email = models.EmailField()

    match_time = models.TimeField(
        editable=False,
        null=True
    )

    match_duration = models.DurationField()

    # created_at = models.DateTimeField(auto_now_add=True)
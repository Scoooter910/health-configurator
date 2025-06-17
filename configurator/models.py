from django.db import models

class HealthConfig(models.Model):
    client_name = models.CharField(max_length=100)
    enable_vaccine_tracking = models.BooleanField(default=False)
    enable_covid_screening = models.BooleanField(default=False)
    notification_email = models.EmailField()

    def __str__(self):
        return self.client_name

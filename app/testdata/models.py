from django.db import models


class UserData(models.Model):
    environment = models.CharField(max_length=10)
    number = models.CharField(max_length=15)
    mail = models.EmailField(max_length=254, default='email@email.email')
    otp = models.CharField(default=None, max_length=6)
    used = models.BooleanField(default=False)
    eligible_e2e = models.BooleanField(default=False)
    eligible_emi = models.BooleanField(default=False)

    def __str__(self):
        return self.number

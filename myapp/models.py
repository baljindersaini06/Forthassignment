from django.db import models
from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=48, unique=True, null=False)
    address_street_name = models.CharField(max_length=50, unique=True, null=False)
    suburb = models.CharField(max_length=40, null=False, unique=True)
    postcode = models.CharField(max_length=6, validators=[RegexValidator(r'^\d{1,10}$')])
    state = models.CharField(max_length=20, null=False, blank=False)
    contact_name = models.CharField(max_length=48, null=False)
    email_address= models.EmailField(max_length=62, null=False)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return self.client_name
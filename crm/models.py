from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    #tc kimlik kismi nasil yapilmali arastirilacak.
    tc_no = models.IntegerField(editable=True, validators=[
        RegexValidator(
            r'^[1-9]{1}[0-9]{9}[02468]{1}$', 
            message="Invalid Tc No ", 
            code="invalid_number"
            )
        ], unique=True)
    first_name = models.CharField(max_length=50, editable=True)
    last_name =  models.CharField(max_length=50, editable=True)
    phone = models.CharField(max_length=15, editable=True)
    city =  models.CharField(max_length=50, editable=True)
    district =  models.CharField(max_length=50, editable=True)

    def __str__(self):  
        return(f"{self.first_name} {self.last_name}")
    
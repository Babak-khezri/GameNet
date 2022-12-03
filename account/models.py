from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    date_of_employ = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=0,blank=True,null=True)

    def full_name(self):
        return self.first_name + ' ' + self.last_name
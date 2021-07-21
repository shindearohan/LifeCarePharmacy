from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False



class Photo(models.Model):
    Medical_Name = models.CharField(max_length=50, default="")
    Medicine_Name = models.CharField(max_length=50)
    No_of_strips = models.CharField(max_length=12)
    NO_of_medicine = models.CharField(max_length=12)
    photo = models.ImageField(upload_to="photoimage")
    

    #def __str__(self):
        #return self.name
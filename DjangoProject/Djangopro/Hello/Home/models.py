from django.db import models
import datetime

#makemigrations - create changes and store in a file
#migrate - apply the pending changes created by makemigrations

# Create your models here.

class About_us(models.Model):
    name = models.CharField(max_length=250)
    contact_number = models.IntegerField(blank=True,unique=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=250)
    # contact_number = models.IntegerField(blank=True,unique=True)
    feedback = models.CharField(max_length=250)
    suggestions = models.TextField()
    added_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    name = models.CharField(max_length=250)
    email_id = models.CharField(max_length=250)
    address = models.TextField()
    order_list = models.CharField(max_length=250)
    paid_payment = models.IntegerField(max_length=250)
    remaining_payment = models.CharField(max_length=250)
    total_payment = models.CharField(max_length=250)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Salesrecord(models.Model):
    medical_name = models.CharField(max_length=250)
    medicine_name = models.CharField(max_length=250)
    amount_of_medicine = models.IntegerField(max_length=250)
    price_of_medicine = models.IntegerField(max_length=250)
    manufacture_date = models.DateField(max_length=250)
    expiry_date = models.DateField(max_length=250)
    added_on = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
        #return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=40)

    def __str__(self):
        return self.name
        
class Reg(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=122)
    contactno = models.CharField(max_length=12, default="")
    password = models.CharField(max_length=12)
    re_password = models.TextField(max_length=40)

    def __str__(self):
        return self.name
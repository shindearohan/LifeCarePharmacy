from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Login(models.Model):
    emailid = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class Forgotpass(models.Model):
    emailid = models.EmailField(max_length=50)
    newpassword= models.CharField(max_length=50)
    confpassword= models.CharField(max_length=50)

class Contact(models.Model):

    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    message= models.CharField(max_length=200)

class Stock(models.Model):
    
    medname = models.CharField(max_length=50)
    companyname = models.CharField(max_length=50)
    batchno = models.CharField(max_length=20)
    no_of_strips = models.CharField(max_length=50,default="")
    no_of_med = models.CharField(max_length=50)
    mfd = models.DateField()
    exd = models.DateField()
    price = models.FloatField(max_length=10)
    added_on =models.DateTimeField(auto_now_add=True)
    #class Meta:
       #db_table="Stock"

class Newfeedback(models.Model):
    nm = models.CharField(max_length=20)
    feedback = models.CharField(max_length=50)
    #star = models.CharField(max_length=5)
    suggestion = models.CharField(max_length=500)
    added_on =models.DateTimeField(auto_now_add=True)



#renuka files
class Photo(models.Model):
    name= models.CharField(max_length=20, default="")
    email= models.EmailField()
    Medical_Name = models.CharField(max_length=50, default="")
    Medicine_Name = models.CharField(max_length=50)
    No_of_strips = models.CharField(max_length=12)
    NO_of_medicine = models.CharField(max_length=12)
    photo = models.ImageField(upload_to="photoimage")

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    address = models.CharField(max_length=30, default="", editable=False)

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


#class Update(models.Model):
    #id = models.IntegerField(primary_key=True)
    #medname = models.CharField(max_length=50)
    #companyname = models.CharField(max_length=50)
    #batchno = models.CharField(max_length=20)
    #mfd = models.DateField()
    #exd = models.DateField()
    #price = models.FloatField(max_length=10)

#class Delete(models.Model):
    
    #medname = models.CharField(max_length=50)
    #companyname = models.CharField(max_length=50)
    #batchno = models.CharField(max_length=20)
    #mfd = models.DateField()
    #exd = models.DateField()
    #price = models.FloatField(max_length=10)

#rohan files
class Reg(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=122)
    contactno = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    re_password = models.CharField(max_length=40)
    mname = models.CharField(max_length=50, null=True)
    medicalno = models.CharField(max_length=50, null=True)
    maddress = models.CharField(max_length=500, null=True)

    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."  

class Accbill(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    Medicine_Name = models.CharField(max_length=50)
    No_of_strips = models.CharField(max_length=12)
    NO_of_medicine = models.CharField(max_length=12)
    mednameprice = models.CharField(max_length=50)
    stripsprice = models.CharField(max_length=12)
    nomedprice = models.CharField(max_length=12)
    total = models.CharField(max_length=12)

class Bill(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    Medicine_Name = models.CharField(max_length=50)
    No_of_strips = models.CharField(max_length=12)
    NO_of_medicine = models.CharField(max_length=12)
    mednameprice = models.CharField(max_length=50)
    stripsprice = models.CharField(max_length=12)
    nomedprice = models.CharField(max_length=12)
    total = models.CharField(max_length=12)
    

    def __str__(self):
        return self.name         
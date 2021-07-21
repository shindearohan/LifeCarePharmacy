from django.http import HttpResponse
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from home.models import Customer
from django.views import  View
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.contrib import messages
#from django.contrib.auth.models import User

#from home.forms import CustomerOrder
#from home.models import User
from home.form import PhotoForm
from home.models import Photo



# Create your views here.
def index(request):
    return render(request,'index.html')
   
#def main(request):
    #print(request.user)
    #if request.user.is_anonymous:
     #if request.method=="POST":
      #fm = CustomerOrder(request.POST)
      #if fm.is_valid():
      #name = fm.cleaned_data['Medical_Name']  
      #nm = fm.cleaned_data['Medicine_Name']
      #strip = fm.cleaned_data['No_of_strips']
      #no = fm.cleaned_data['NO_of_medicine']
      #image = fm.cleaned_data['image']
      #reg = User(Medical_Name=name, Medicine_Name=nm, No_of_strips=strip, NO_of_medicine=no, image=image)   
      #reg.save()
      #fm = CustomerOrder()   
    #else:
      #fm = CustomerOrder()
    #stud = User.objects.all()   
    #return render(request,'addandshow.html', {'form':fm ,
    #'stu':stud})            
        #return render(request,'addandshow.html')                    
    #return render(request,'main.html')

def addandshow(request):
    return render(request,'addandshow.html')    

def delete_data(request, id):
 if request.method == 'POST':
  pi = Photo.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/main')
 

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('index')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message
    
class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('main')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})


#def logout(request):
    #request.session.clear()
    #stud = Photo.objects.clear()
    #return render(request, "index.html", {'stu':stud})
    #return redirect('index')

#def main(request):
    #if request.method == "POST":
    #form = PhotoForm()    
    #return render (request, "addandshow.html", {'form':form}    

def main(request):
    if request.method == "POST":
        
  
     form = PhotoForm()
    img = Photo.objects.all()   
    return render(request, "addandshow.html", {'img':img, 'form':form})

def main(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
    
    
        if form.is_valid():
            form.save()
            
  
    form = PhotoForm()
    img = Photo.objects.all() 
    stud = Photo.objects.all()  
    return render(request, "addandshow.html", {'img':img,'stu':stud, 'form':form})


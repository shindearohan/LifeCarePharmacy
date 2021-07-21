from django.shortcuts import redirect, render, HttpResponseRedirect
from django.http import HttpResponse
from home.models import Login
from home.models import Forgotpass
from home.models import Contact
from home.models import Stock
from home.form import Stockform
#from home. import FReport
from home.models import Newfeedback
from django.contrib import messages
from django.db.models import Q
#from home.models import Fbackforms
#from home.form import Feedbackform
from django.utils.datastructures import MultiValueDictKeyError
#Rohan files
from home.models import Reg, Bill, Accbill
from home.models import Orders, OrderUpdate
from home.Paytm import Checksum
from django.views.decorators.csrf import csrf_exempt
MERCHANT_KEY = 'uWfCBp23aXYyBt2e'
#renukafile
from home.form import PhotoForm
from home.models import Photo
from django.contrib.auth.hashers import  check_password
from home.models import Customer
from django.views import  View
from django.contrib.auth.hashers import make_password

from django.template.loader import get_template   
from xhtml2pdf import pisa 

#from home.models import search
#from home.models import Update
#from home.models import Delete
#from home.form import Update


# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is homepage")
def feedback(request):
    return render(request,'feedback.html')

def base(request):
    return render(request, 'base.html')

def registration(request):
    return HttpResponse("this is registrationpage")

def login(request):
    if request.method=='POST':
        emailid = request.POST['emailid']
        password = request.POST['password']
        print(emailid, password)
        login = Login(emailid=emailid, password=password)
        login.save()
    return render(request, 'login.html')

def contact(request):
    if request.method== 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact= Contact(name=name, email=email, message=message)
        contact.save()
    return render(render,'/#contact')

def login_1(request):
    return render(request, 'login_1.html')   


    
def forgotpass(request):
    if request.method=='POST':
        emailid = request.POST['emailid']
        newpassword = request.POST['newpassword']
        confpassword = request.POST['confpassword']
        print(emailid, newpassword, confpassword)
        forgotpass = Forgotpass(emailid=emailid, newpassword=newpassword, confpassword=confpassword)
        forgotpass.save()
    return render(request, 'forgotpass.html')

def stock(request):
    if request.method=='POST':
        #id = request.POST['id']
        medname = request.POST['medname']
        companyname = request.POST['companyname']
        batchno = request.POST['batchno']
        no_of_strips = request.POST['no_of_strips']
        no_of_med = request.POST['no_of_med']
        mfd = request.POST['mfd']
        exd = request.POST['exd']
        price = request.POST['price']
        print(medname, companyname, batchno, mfd, exd, price)
        stock = Stock( medname=medname, companyname=companyname, batchno=batchno, no_of_strips=no_of_strips, no_of_med=no_of_med, mfd=mfd, exd=exd, price=price)
        stock.save()
        messages.success(request,"Stock Added succesfully...!")
    return render(request, 'stock.html')  

def newfeedback(request):
    all_data = Newfeedback.objects.all()
    if request.method == 'POST':
        nm = request.POST['nm']
        feedback = request.POST['feedback']
        #star = request.POST['star']
        suggestion=request.POST['suggestion']
        newfeedback = Newfeedback(nm=nm, feedback=feedback, suggestion=suggestion)
        newfeedback.save()
        res = "Dear {} Thanks for your feedback".format(nm)
        return render(request,"newfeedback.html",{"status":res,"messages":all_data})
    return render(request, 'newfeedback.html',{"messages":all_data})

#def feedback(request):
    #if request.method =='POST':
        #try:
            #name = request.POST['name']
            #Star = request.POST['Star']
            #suggestion = request.POST['suggetion']
        #except MultiValueDictKeyError:
             #name=  request.POST['name']
             #Star= False
             #suggestion= False       
        #feedback= Feedback(name=name, Star=Star, suggestion=suggestion)
        #feedback.save()
    #return render(request, 'feedback.html')

#def feedback(request):
    #if request.method == 'POST':
        #name = request.POST['name']
        #feedback= request.POST['feedback']
        #suggestion = request.POST['suggetion']
       # name = request.POST['name']
        #suggestion = request.POST['suggetion']
       # feedback= Fbackforms(name=name, feedback=feedback ,suggestion=suggestion)
       # feedback.save()
    #return render(request, 'feedback.html')
        

       



def stockbase(request):
    return render(request, 'stockbase.html')  

def view(request):
    display = Stock.objects.all()
    #print(stock)
    return render(request, 'view.html', {'Stock': display})

def checkorders(request):
    order = Photo.objects.all()
    return render(request, 'checkorders.html', {'Photo': order})

def checkorders1(request):
    order = Photo.objects.all()
    return render(request, 'checkorders1.html', {'Photo': order})

def checkorders2(request):
    order = Photo.objects.all()
    return render(request, 'checkorders2.html', {'Photo': order})


def search(request):
    allpost = Stock.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        allpost=Stock.objects.filter(Q(medname__icontains=q)|Q(companyname__icontains=q)|Q(batchno__icontains=q))
    return render(request,"view.html",{'Stock':allpost})
     
        #return render(request, 'search.html', {'allsearch': allsearch})
        #params = {'allsearch' : allsearch}
    #return render(request, 'search.html', {'allsearch': allsearch})

def delete(request, id = id):
    stock = Stock.objects.get(id=id)
    stock.delete()
    #messages.success(request,"Stock Deleted succesfully...!")
    return redirect("/view")

def update(request, id):
    updateemp = Stock.objects.get(id=id)
    form = Stockform(request.POST,instance=updateemp)
    if form.is_valid() :
        form.save()
        messages.success(request,"Record updated succesfully...!")
        return render(request,"view.html")
    else:
        return render(request,"stockupdate.html",{'Stock':updateemp})    

#def stockupdate(request, id):
    #if request.method == "POST":
 #   displayrecored = Stock.objects.get( id = id )
 #   return render(request, 'stockupdate.html', {'Stock': displayrecored})

#def updatestock(request, id ):
 #   updaterecods = Stock.objects.get( id = id )
 #   form = Stockform(request.POST, instance=updaterecods)
 #   if form.is_valid():
 #       form.save()
 #       messages.success(request, "recorde Updated Successfully...")
 #       return HttpResponse(request, "stockupdate.html", {'Stock': updaterecods})
        #return render(request, "stockupdate.html")
    #else:  
        #return render(request, "stockupdate.html")  
        #return render(request, "stockupdate.html", {'Stock': updaterecods})

    #form = Stockform(request.POST, instance=Stock)
    #if request.method == "POST":
        #if form.is_valid():
            #form.save()
            #return redirect("view.html")
    #else:
       # form = Update
        
def search1(request):
    allpost = Photo.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        allpost=Photo.objects.filter(Q(Medical_Name__icontains=q)|Q(Medicine_Name__icontains=q))
    return render(request,"checkorders.html",{'Photo':allpost})

def pharma(request):
    return render(request, 'pharma.html')        

def checkorderbase(request):
    return render(request, 'checkorderbase.html')



#def feedback(request):
    #return render(request, 'feedback.html')


       
        #form = Feedbackform(request.POST)
        #if form.is_valid():
            #form.save()
            #name=form.cleaned_data.get['name']
            #star=form.cleaned_data.get['star']
            #suggestion=form.cleaned_data.get['suggestion']
            #return redirect('feedback.html')
    #else:
        #form = Feedbackform()
    #return render(request, 'feedback.html', {'form': form})

def customerorder(request):
    if request.method=='POST':
        Medicinename = request.POST['medname']
    return render(request,'customerorder.html')

#renuka files
def customerindex(request):
    return render(request,'customerindex.html')

def addandshow(request):
    return render(request,'addandshow.html')    

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
        address = postData.get('address')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'address' : address,
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            address=address)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password, address)
            customer.password = make_password(customer.password)
            customer.register()
            messages.success(request,"Registration succesfull...!")

            return redirect('customerlogin')
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
        elif not customer.address:
            error_message = 'address Required'
        elif len(customer.address) < 4:
            error_message = 'Address must be 4 char long or more'
        # saving
        
        return error_message

class customerlogin(View):
    return_url = None
    def get(self , request):
        customerlogin.return_url = request.GET.get('return_url')
        return render(request , 'customerlogin.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if customerlogin.return_url:
                    return HttpResponseRedirect(customerlogin.return_url)
                else:
                    customerlogin.return_url = None
                    return redirect('custdashboard')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'customerlogin.html', {'error': error_message})


def pdf_report(request):
    home = Stock.objects.all()

    home = Stock.objects.filter().order_by("id")
    template_path = 'pdf_report.html'
    context = {'Stock':home,"messages":home}
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'attachment; filename="Pdf_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some error <pre>' + html + '</pre>')
    return response

def cst_order_pdf(request):
    home = Photo.objects.all()

    home = Photo.objects.filter().order_by("id")
    template_path = 'cst_order_pdf.html'
    context = {'Photo':home,"messages":home}
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'attachment; filename="Customer_Order_Pdf_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some error <pre>' + html + '</pre>')
    return response

#roshnifile
def FReport(request):
    fback = Newfeedback.objects.all()

    return render(request,"FReport.html", {'Newfeedback':fback})

def FReport1(request):
    fback = Newfeedback.objects.all()
    return render(request,"FReport1.html", {'Newfeedback':fback})

def FReport2(request):
    fback = Newfeedback.objects.all()
    return render(request,"FReport2.html", {'Newfeedback':fback})


def SReport(request):
    display = Photo.objects.all()
    return render(request,"SReport.html",{'Photo':display} )

def SReport1(request):
    display = Photo.objects.all()
    return render(request,"SReport1.html",{'Photo':display} )



def feedpdf_report(request):
    home = Newfeedback.objects.all()

    home = Newfeedback.objects.filter().order_by("id")
    template_path = 'feedpdf_report.html'
    context = {'Newfeedback':home,"messages":home}
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'attachment; filename="feedback_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some error <pre>' + html + '</pre>')
    return response

def Spdf_report(request):
    home = Photo.objects.all()
    home = Photo.objects.filter().order_by("id")
    template_path = 'Spdf_report.html'
    context = {'Photo':home,"messages":home}
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'attachment; filename="salesrecord_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some error <pre>' + html + '</pre>')
    return response

    #rohan file
def reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        contactno = request.POST['contactno']
        password = request.POST['password']
        re_password = request.POST['re_password']
        mname = request.POST['mname']
        medicalno = request.POST['medicalno']
        maddress = request.POST['maddress']
        reg = Reg(name=name, email=email, contactno=contactno, password=password, re_password=re_password, 
        mname=mname, medicalno=medicalno, maddress=maddress)
        reg.save()
    return render(request,'reg.html')

def pharmalogin(request):
    if request.method == "POST":
        try:
            Userdetails=Reg.objects.get(email=request.POST['email'], password=request.POST['password'])
            
            request.session['email']=Userdetails.email
            return render(request,"admindashboard.html")
        except Reg.DoesNotExist as e:
            messages.success(request,'Username / password Invalid')
    return render(request,"pharmalogin.html")

def pharmadashboard(request):
    return render(request,'pharmadashboard.html')    

def pharmacydashboard(request):
    return render(request,'pharmacydashboard.html')    

def admindashboard(request):
    return render(request,'admindashboard.html')  
      
def customerdashboard(request):
    return render(request,'customerdashboard.html') 
       
def custdashboard(request):
    return render(request,'custdashboard.html')
    
def paymentdashboard(request):
    return render(request,'paymentdashboard.html')    


def customerdetails(request):

    all_data = Customer.objects.all()
    return render(request,"customerdetails.html", {'Customer':all_data})

def pharmadetails(request):

    all_data = Reg.objects.all()
    return render(request,"pharmadetails.html", {'Reg':all_data})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

                'MID': 'RnnpsU89707581682095',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, "paymentstatus.html", {'response': response_dict})

def paymentstatus(request):
    return render(request, "paymentstatus.html")

def PReport(request):
    display = Orders.objects.all()
    return render(request,"PReport.html",{'Orders':display} )

def PReport1(request):
    display = Orders.objects.all()
    return render(request,"PReport1.html",{'Orders':display} )


def innerpage(request):
    return render(request, 'inner-page.html')

def Paypdf(request):
    home = Orders.objects.all()
    home = Orders.objects.filter()
    template_path = 'Paypdf.html'
    context = {'Orders':home,"messages":home}
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'attachment; filename="paymentrecord_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some error <pre>' + html + '</pre>')
    return response

def search2(request):
    allpost = Customer.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        allpost=Customer.objects.filter(Q(first_name__icontains=q)|Q(last_name__icontains=q))
    return render(request,"customerdetails.html",{'Customer':allpost})

def search3(request):
    allpost = Reg.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        allpost=Reg.objects.filter(Q(name__icontains=q)|Q(mname__icontains=q))
    return render(request,"pharmadetails.html",{'Reg':allpost})

def search4(request):
    allpost = Photo.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        allpost=Photo.objects.filter(Q(id__icontains=q)|Q(Medicine_Name__icontains=q)|Q(Medical_Name__icontains=q))
    return render(request,"SReport.html",{'Photo':allpost})

def search5(request):
    allpost = Orders.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        allpost=Orders.objects.filter(Q(name__icontains=q)|Q(email__icontains=q))
    return render(request,"PReport.html",{'Orders':allpost})


def accmakebill(request,id):
    stud = Photo.objects.filter(id=id)
    
    return render(request,"makebill.html", {'stu': stud,"messages":stud})

def billgenerate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Medicine_Name = request.POST.get('Medicine_Name')
        No_of_strips = request.POST.get('No_of_strips')
        NO_of_medicine = request.POST.get('NO_of_medicine')
        mednameprice = request.POST.get('mednameprice')
        stripsprice = request.POST.get('stripsprice')
        nomedprice = request.POST.get('nomedprice')
        total = request.POST.get('total')
       # total = request.POST.get('bill')
        accmakebill= Bill(name=name, email=email, Medicine_Name=Medicine_Name, No_of_strips=No_of_strips, NO_of_medicine=NO_of_medicine, mednameprice=mednameprice, stripsprice=stripsprice,nomedprice=nomedprice,total=total)
        accmakebill.save()
        messages.success(request, 'Bill Generated...')
        

    return render(request,"makebill.html")

def bill_pdf(request):
    home = Bill.objects.all()

    home = Bill.objects.filter().order_by("id")
    template_path = 'bill_pdf.html'
    context = {'Bill':home,"messages":home}
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'attachment; filename="Bill.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some error <pre>' + html + '</pre>')
    return response

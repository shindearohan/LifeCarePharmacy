from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse 
from datetime import datetime
from Home.models import Contact
from Home.models import About_us
from Home.models import Feedback
from Home.models import Payment
from Home.models import Salesrecord
from Home.models import Reg
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError
from xhtml2pdf import pisa 
from django.template.loader import get_template 



# Create your views here.
def index(request):
    try:
        request.session['email']
    except:
        return render(request,"index.html")

    #return render(request,"main.html")
    context = {"variable1" : "This is sent",
               "variable2" :  "It is great"
    }

    #messages.success(request, 'This is test messages..')
    return render(request,'index.html', context)
   #return HttpResponse("This is home page")

def about(request):
    #cats = Category.objects.all().order_by("cat_name")
    all_data = About_us.objects.all()
    if request.method=="POST":
        nm = request.POST["name"]
        con = request.POST["contact"]
        sub = request.POST["subject"]
        msz = request.POST["message"]

        data = About_us(name=nm,contact_number=con,subject=sub,message=msz)
        data.save()
        res = "Dear {} Thanks for your feedback".format(nm)
        return render(request,"about.html",{"status":res,"messages":all_data})
        # return HttpResponse("<h1 style='color:green;'>Dear {} Data Saved Successfully!</h1>".format(nm))
    return render(request,"about.html",{"messages":all_data})
        # return HttpResponse("This is about page")  


def feedback(request):
    
    #cats = Category.objects.all().order_by("cat_name")
    all_data = Feedback.objects.all()
    if request.method=="POST":
        nm = request.POST["name"]
        # cont = request.POST["contact"]
        feed = request.POST["feedback"]
        sugg = request.POST["suggestions"]
        
        # is_private = request.POST.get('is_private', False)

        feedback = Feedback(name=nm, feedback=feed, suggestions=sugg)
        feedback.save()
        res = "Dear {} Thanks for your feedback".format(nm)
        return render(request,"feedback.html",{"status":res,"messages":all_data})
        # return HttpResponse("<h1 style='color:green;'>Dear {} Data Saved Successfully!</h1>".format(nm))
    return render(request,"feedback.html",{"messages":all_data})
   # return HttpResponse("This is feedback page")  

def payment(request):
    
    #cats = Category.objects.all().order_by("cat_name")
    all_data = Payment.objects.all()
    if request.method=="POST":
        nm = request.POST["name"]
        email = request.POST["email_id"]
        addr = request.POST["address"]
        olist = request.POST["order_list"]
        ppay = request.POST["paid_payment"]
        rpay = request.POST["remaining_payment"]
        tpay = request.POST["total_payment"]
        
        # is_private = request.POST.get('is_private', False)

        data = Payment(name=nm, email_id=email, address=addr, order_list=olist, paid_payment=ppay, remaining_payment=rpay, total_payment=tpay)
        data.save()
        res = "Dear {} Thanks for your payment".format(nm)
        return render(request,"payment.html",{"status":res,"messages":all_data})
        # return HttpResponse("<h1 style='color:green;'>Dear {} Data Saved Successfully!</h1>".format(nm))
    return render(request,"payment.html",{"messages":all_data})
    # return HttpResponse("This is payment page")  


def salesrecord(request):
    
    #cats = Category.objects.all().order_by("cat_name")
    all_data = Salesrecord.objects.all()
    if request.method=="POST":
        mname = request.POST["medical_name"]
        medicinename = request.POST["medicine_name"]
        amountmedicine = request.POST["amount_of_medicine"]
        pricemedicine = request.POST["price_of_medicine"]
        manudate = request.POST["manufacture_date"]
        exprdate = request.POST["expiry_date"]
       
        # is_private = request.POST.get('is_private', False)

        data = Salesrecord(medical_name=mname, medicine_name=medicinename, amount_of_medicine=amountmedicine, price_of_medicine=pricemedicine, manufacture_date=manudate, expiry_date=exprdate)
        data.save()
        res = "Dear customer Thanks for ordering from {} ".format(mname)
        return render(request,"salesrecord.html",{"status":res,"messages":all_data})
        # return HttpResponse("<h1 style='color:green;'>Dear {} Data Saved Successfully!</h1>".format(mname))
    return render(request,"salesrecord.html",{"messages":all_data})
   # return HttpResponse("This is salesrecord page")  

def services(request):
    return render(request,'services.html')
   # return HttpResponse("This is services page")  

def contact(request):
    all_data = Contact.objects.all()
    #print(contact)
    if request.method == "POST":
        nm = request.POST.get('name')
        eml = request.POST.get('email')
        phn = request.POST.get('phone')
        des = request.POST.get('desc')
        contact = Contact(name=nm, email=eml, phone=phn, desc=des)
        contact.save()
        res = "Dear {} Thanks for Feedback".format(nm)
        return render(request,'contact.html',{"status":res,"messages ": contact})
        messages.success(request, 'Your message has been send')
    return render(request,'contact.html',{"messages ": all_data})
   # return HttpResponse("This is contact page")        

def reg(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        reg = Reg(name=name, email=email, contactno=contactno, password=password, re_password=re_password)
        reg.save()
        messages.success(request, 'Your message has been send')
    return render(request,'reg.html')

def login(request):
    if request.method == "POST":
        try:
            Userdetails=Reg.objects.get(email=request.POST['email'], password=request.POST['password'])
            
            request.session['email']=Userdetails.email
            return render(request,"contact.html")
        except Reg.DoesNotExist as e:
            messages.success(request,'Username / password Invalid')
    return render(request,"login.html")

def logoutuser(request):
    try:
        del request.session['email']
    except:
        return render(request,"index.html")

    return redirect('/index')

@csrf_exempt
def handlerequest(request):
    #paytm will send you post request here
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
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})

#def search(request):
 #   if request.method == "POST":
 #           Userdetails=Reg.objects.get(customername=request.POST['customername'])
 #           request.session['customername']=Userdetails.name
 #   return render(request,"search.html")

def search(request):
    allpost = Salesrecord.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        allpost=Salesrecord.objects.filter(Q(medical_name__icontains=q)|Q(medicine_name__icontains=q)|Q(amount_of_medicine__icontains=q))
    return render(request,"SReport.html",{'msg':allpost,"messages":allpost})

def FReport(request):
    home = Feedback.objects.all()

    return render(request,"FReport.html", {'messages': home,"messages":home})

def PReport(request):
    home = Payment.objects.all()

    return render(request,"PReport.html", {'messages': home,"messages":home})

def SReport(request):
    home = Salesrecord.objects.all()

    return render(request,"SReport.html", {'messages': home,"messages":home})


def pdf_report(request):
    home = Salesrecord.objects.all()

    home = Salesrecord.objects.filter().order_by("id")
    template_path = 'pdf_report.html'
    context = {'msg':home,"messages":home}
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

def feedpdf_report(request):
    home = Feedback.objects.all()

    home = Feedback.objects.filter().order_by("id")
    template_path = 'feedpdf_report.html'
    context = {'msg':home,"messages":home}
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

def paypdf_report(request):
    home = Payment.objects.all()

    home = Payment.objects.filter().order_by("id")
    template_path = 'paypdf_report.html'
    context = {'msg':home,"messages":home}
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'attachment; filename="payment_report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    #create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('we had some error <pre>' + html + '</pre>')
    return response


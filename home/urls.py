from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
#renukafile
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
   path("", views.index, name='home'),
   path("inner-page", views.innerpage, name='inner-page'),
   path("base", views.base, name='base'),
   path("registration", views.registration, name='registration'),
   path("login", views.login, name='login'),
   path("pharmalogin", views.pharmalogin, name='pharmalogin'),
   path("reg", views.reg, name='reg'),
   #path("feedback", views.feedback, name='feedback'),
   path("forgotpass", views.forgotpass, name='forgotpass'),
   path("stock", views.stock, name='stock'),
   path("newfeedback", views.newfeedback, name='newfeedback'),
   path("FReport", views.FReport, name='FReport'),
   path("FReport1", views.FReport1, name='FReport1'),
   path("FReport2", views.FReport2, name='FReport2'),

   path("feedpdf_report", views.feedpdf_report, name='feedpdf_report'),
   path("SReport", views.SReport, name='SReport'),
   path("SReport1", views.SReport1, name='SReport1'),

   path("Spdf_report", views.Spdf_report, name='Spdf_report'),
   path("Paypdf", views.Paypdf, name='Paypdf'),

   path("PReport", views.PReport, name='PReport'),
   path("PReport1", views.PReport1, name='PReport1'),

   path('password-reset', auth_views.PasswordResetView.as_view(
      template_name='password_reset.html'), name='password_reset'),
   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
      template_name='password_reset_done.html'), name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
      template_name='password_reset_confirm.html'), name='password_reset_confirm'),

   path("custdashboard", views.custdashboard, name='custdashboard'),
   path("paymentdashboard", views.paymentdashboard, name='paymentdashboard'),
 
   path("pharmacydashboard", views.pharmacydashboard, name='pharmacydashboard'),
   path("pharmadashboard", views.pharmadashboard, name='pharmadashboard'),
   path("admindashboard", views.admindashboard, name='admindashboard'),
   path("customerdetails", views.customerdetails, name='customerdetails'),
   path("pharmadetails", views.pharmadetails, name='pharmadetails'),
   path("checkout", views.checkout, name="Checkout"),
   path("handlerequest", views.handlerequest, name="HandleRequest"),
   path("paymentstatus",views.paymentstatus ,name='paymentstatus'),
   path("customerdashboard", views.customerdashboard, name="customerdashboard"),

   path("pdf_report", views.pdf_report, name='pdf_report'),
   path("cst_order_pdf", views.cst_order_pdf, name='cst_order_pdf'),
   
   path('search', views.search, name='search'),  
   path('search1', views.search1, name='search1'),  
   path('search2', views.search2, name='search2'),  
   path('search3', views.search3, name='search3'),  
   path('search4', views.search4, name='search4'),  
   path('search5', views.search5, name='search5'),  

   #path("stockupdate/<int:id>", views.stockupdate, name='stockupdate'),
   path("update/<int:id>", views.update, name='update'),
   path("stockbase", views.stockbase, name='stockbase'),
   path("view", views.view, name='view'),
   path('delete/<int:id>', views.delete),  
   path("pharma", views.pharma, name='pharma'),
   path("checkorderbase", views.checkorderbase, name='checkorderbase'),
   path("checkorders", views.checkorders, name='checkorders'),
   path("checkorders1", views.checkorders1, name='checkorders1'),
   path("checkorders2", views.checkorders2, name='checkorders2'),

   path("customerorder", views.customerorder, name='customerorder'),
   #renuka files
   path('main', views.main, name='main'),
   path('addandshow', views.addandshow, name='addandshow.html'),
   path("delete/<int:id>/", views.delete_data, name='deletedata'),
   path('customerlogin', views.customerlogin.as_view(), name='customerlogin'),
   path("customerindex", views.customerindex, name="customerindex.html"),
   path('signup', views.Signup.as_view(), name='signup'),
   path('bill_pdf', views.bill_pdf, name='bill_pdf'),

   path("makebill/<int:id>", views.accmakebill, name='makebill'),
   path('billgenerate', views.billgenerate, name='billgenerate'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

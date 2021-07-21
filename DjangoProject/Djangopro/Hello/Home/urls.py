from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('index', views.index, name='Home'),
    path('about',views.about, name='about'),
    path('feedback',views.feedback, name='feedback'),
    path('payment', views.payment, name='payment'),
    path('salesrecord', views.salesrecord, name='salesrecord'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
    path('reg',views.reg, name='reg'),
    path('login',views.login, name='login'),
    path('logout',views.logoutuser, name='logoutuser'),
    path('handlerequest',views.handlerequest, name='handlerequest'),
    path('FReport',views.FReport, name='FReport'),
    path('PReport',views.PReport, name='PReport'),
    path('SReport',views.SReport, name='SReport'),
    path('search', views.search, name='search'),  
    path("pdf_report", views.pdf_report, name='pdf_report'),
    path("feedpdf_report", views.feedpdf_report, name='feedpdf_report'),
    path("paypdf_report", views.paypdf_report, name='paypdf_report'),

]

admin.site.site_header = 'Lifecare Pharmacy Admin'
admin.site.index_title = 'Welcome to Lifecare Pharmacy System'
admin.site.site_title = 'Lifecare Pharmacy System'
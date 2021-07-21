from django.urls import path
from django.contrib import admin
from home import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index.html"),
    path('signup', views.Signup.as_view(), name='signup'),
    path('login', views.Login.as_view(), name='login'),
    #path('logout', views.logout , name='logout'),
    path('main', views.main, name='main'),
    path('addandshow', views.addandshow, name='addandshow.html'),
    path("delete/<int:id>/", views.delete_data, name='deletedata'),
    

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

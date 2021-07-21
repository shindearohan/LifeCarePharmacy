from django.contrib import admin
from home.models import Customer
#from home.models import User
from home.models import Photo

# Register your models here.
admin.site.register(Customer)
#@admin.register(User)
#class UserAdmin(admin.ModelAdmin):
 #list_display = ('id', 'Medical_Name','Medicine_Name', 'No_of_strips', 'NO_of_medicine')
admin.site.register(Photo)

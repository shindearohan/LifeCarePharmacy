from django.contrib import admin
from django.db import OperationalError
from Home.models import Contact
from Home.models import Reg
from Home.models import Feedback
from Home.models import Payment
from Home.models import Salesrecord

# Register your models here.
admin.site.register(Contact)
admin.site.register(Reg)
admin.site.register(Feedback)
admin.site.register(Payment)
admin.site.register(Salesrecord)
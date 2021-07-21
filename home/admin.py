from django.contrib import admin
from home.models import Login
#from home.models import Forgotpass
from home.models import Stock
from home.models import Newfeedback
from home.models import Contact
#from home.models import Fbackforms
#from home.models import Update
#from home.models import Delete
#renukafile
from home.models import Photo
from home.models import Customer
#rohan files
from home.models import Reg
from home.models import Accbill
from home.models import Bill

# Register your models here.
admin.site.register(Login)
#admin.site.register(Forgotpass)
admin.site.register(Stock)
admin.site.register(Newfeedback)
admin.site.register(Contact)
#admin.site.register(Fbackforms)
#admin.site.register(Update)
#admin.site.register(Delete)
#renukafile
admin.site.register(Photo)
admin.site.register(Customer)
#rohan files
admin.site.register(Accbill)
admin.site.register(Bill)

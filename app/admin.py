from django.contrib import admin
from .models import Employee , Person,Profile, Address,CarModel,FuelType
# Register your models here.

# in admin block we need to add every model karan site vr bgnysathi
#theses models we can see at site
admin.site.register([Employee,Person,Profile,Address,CarModel,FuelType])


print("in admin :- added by Athrav")
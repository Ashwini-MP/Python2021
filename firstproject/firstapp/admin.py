from django.contrib import admin
from .models import Name, Contact, Address

# Register your models here.

admin.site.register(Name)
admin.site.register(Contact)
admin.site.register(Address)

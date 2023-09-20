from django.contrib import admin

from bank.models import Account,Employee,Operateur

# Register your models here.
admin.site.register(Operateur)
admin.site.register(Account)
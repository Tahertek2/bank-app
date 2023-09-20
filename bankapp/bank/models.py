from django.db import models
from django.contrib.auth.models import User

class Operateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)


class Account(models.Model):
    customer = models.ForeignKey(Operateur, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.CharField(max_length=20)



class Card(models.Model):
    card_number = models.CharField(max_length=16, unique=True)
    card_holder_name = models.CharField(max_length=100)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=4)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    
    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

class CardType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

 

    class Meta:
        verbose_name = 'Card Type'
        verbose_name_plural = 'Card Types'

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    is_successful = models.BooleanField(default=True)



    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

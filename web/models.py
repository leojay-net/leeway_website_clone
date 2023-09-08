from wsgiref.simple_server import demo_app
from django.db import models
from django.utils import timezone
import random

# Create your models here.
class Myuser(models.Model):
    username = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    phone = models.IntegerField(blank=True)
    date =models.DateTimeField(default=timezone.datetime.now())
    account_balance = models.FloatField(default=5.00)
    total_profit = models.FloatField(default=0.00)
    total_bonus = models.FloatField(default=0.00)
    total_referral_bonus = models.FloatField(default=0.00)
    total_investment_plans = models.FloatField(default=0.00)
    total_active_investment_plans = models.FloatField(default=0.00)
    total_deposit = models.FloatField(default=0.00)
    total_withdrawals = models.FloatField(default=0.00)
    address = models.CharField(max_length=1000, blank=True)
    referral_id = models.CharField(max_length=100, blank=True)
    dob = models.DateField(default=timezone.now())
    bank_name = models.CharField(max_length=100, blank=True)
    account_number =models.CharField(max_length=100, blank=True, default='')
    account_name = models.CharField(max_length=100, blank=True)
    swift_code = models.CharField(max_length=100, blank=True, default='')
    btc = models.CharField(max_length=1000, blank=True)
    eth = models.CharField(max_length=1000, blank=True)
    ltc = models.CharField(max_length=1000, blank=True)
    otp = models.CharField(max_length=4, blank=True)
    mail_profit = models.CharField(max_length=4, blank=True)
    mail_expires = models.CharField(max_length=4, blank=True)
    

    def __str__(self):
        return self.username
    
class Record(models.Model):
    username = models.CharField(max_length=100, default='')
    plan = models.CharField(max_length=100)
    amount = models.IntegerField()
    type = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.username

class Deposit(models.Model):
    username = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='Pending')
    amount = models.IntegerField()
    payment_mode = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.username

class Withdrawal(models.Model):
    username = models.CharField(max_length=100, default='')
    recieving_mode = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.username

class Withdrawal_Page(models.Model):
    username = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='Pending')
    amount_requested = models.IntegerField()
    amount_charges = models.CharField(max_length=100)
    recieving_mode = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.username

class Others(models.Model):
    username = models.CharField(max_length=100, default='')
    plan = models.CharField(max_length=100)
    amount = models.IntegerField()
    type = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.username

class Support(models.Model):
    username = models.CharField(max_length=100, default='')
    message = models.CharField(max_length=1000)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username
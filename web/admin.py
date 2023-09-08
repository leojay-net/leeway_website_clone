from tkinter import W
from django.contrib import admin
from .models import Myuser, Record, Deposit,Withdrawal,Others, Withdrawal_Page, Support
# Register your models here.
admin.site.register(Myuser)
admin.site.register(Record)
admin.site.register(Deposit)
admin.site.register(Withdrawal)
admin.site.register(Withdrawal_Page)
admin.site.register(Others)
admin.site.register(Support)
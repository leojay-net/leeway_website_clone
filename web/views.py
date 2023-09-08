from requests import Session
from django.core.mail import send_mail,  BadHeaderError
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import Myuser, Record, Deposit,Withdrawal_Page, Withdrawal, Others, Support
from django.contrib.auth.decorators import login_required
import random



def crypto():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'333',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '3db43e48-c593-4b21-9544-ef9ac7f5d51c',
    }

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        data = dict()
    return data

def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Faq(request):
    return render(request, 'faq.html')

def Contact(request):
    return render(request, 'contact.html')

@login_required(login_url="login")
def account(request):
    pk = request.user.username
    user = Myuser.objects.get(username=pk)
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        dob = request.POST['dob']
        address = request.POST['address']
        if user.name != name:
            user.name = name
        if user.phone != phone:
            user.phone = phone
        if user.dob != dob:
            user.dob = dob
        if user.address != address:
            user.address = address
        user.save()
    context = {
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'account.html', context)

@login_required(login_url="login")
def account_bank(request):
    pk = request.user.username
    user = Myuser.objects.get(username=pk)
    if request.method == 'POST':
        bank_name = request.POST['bank_name']
        acc_name = request.POST['account_name']
        acc_no = request.POST['account_no']
        swift = request.POST['swiftcode']
        if user.bank_name != bank_name:
            user.bank_name = bank_name
        if user.account_name != acc_name:
            user.account_name = acc_name
        if user.account_number != acc_no:
            user.account_number = acc_no
        if user.swift_code != swift:
            user.swift_code = swift
        btc = request.POST['btc_address']
        eth = request.POST['eth_address']
        ltc = request.POST['ltc_address']
        if user.btc != btc:
            user.btc = btc
        if user.eth != eth:
            user.eth = eth
        if user.ltc != ltc:
            user.ltc = ltc
        user.save()
    context = {
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'account.html', context)
            
# @login_required(login_url="login")      
# def account_crypto(request):
#     pk = request.user.username
#     user = Myuser.objects.get(username=pk)
#     if request.method == 'POST':
#         btc = request.POST['btc_address']
#         eth = request.POST['eth_address']
#         ltc = request.POST['ltc_address']
#         if user.btc != btc:
#             user.btc = btc
#         if user.eth != eth:
#             user.eth = eth
#         if user.ltc != ltc:
#             user.ltc = ltc
#     context = {
#         'myuser' : Myuser.objects.get(username = pk)
#     }

#     return render(request, 'account.html', context)

@login_required(login_url="login")      
def account_password(request):
    pk = request.user.username
    user = Myuser.objects.get(username=pk)
    if request.method == "POST":
        old_pass = request.POST['current_password']
        new_pass = request.POST['password']
        confirm_new_pass = request.POST['password_confirmation']
        if request.user.password != old_pass:
            if new_pass == confirm_new_pass:
                User.objects.get(username=pk).password = new_pass
                User.save()
        else:
            messages.info(request, 'password is wrong')
            return redirect('account')
    context = {
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'account.html', context)

@login_required(login_url="login")      
def account_otp(request):
    pk = request.user.username
    user = Myuser.objects.get(username=pk)
    if request.method == 'POST':
        otp = request.POST['otpsend']
        mail_profit = request.POST['roiemail']
        mail_expires = request.POST['invplanemail']
        user.otp = otp
        user.mail_profit = mail_profit
        user.mail_expires = mail_expires

    context = {
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'account.html', context)

@login_required(login_url="login")
def account_history(request):
    pk = request.user.username
    deposits = Deposit.objects.all()
    withdraws = Withdrawal_Page.objects.all()
    context = {
        'deposits' : deposits,
        'withdraws' : withdraws,
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'account_history.html', context)

@login_required(login_url="login")
def dashboard(request):
    pk = request.user.username
    context = {
        'myuser' : Myuser.objects.get(username = pk)
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url="login")    
def deposit(request):
    pk = request.user.username
    if request.method == 'POST':
        amount = request.POST['amount']
        payment = request.POST['payment']

        pay = Deposit.objects.create(username=request.user.username, amount=amount, payment_mode=payment)
        pay.save()
        return redirect('payment_page')
    context = {
        'myuser' : Myuser.objects.get(username = pk)
    }
    return render(request, 'deposit.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'credentials not correct')
            return redirect('login')
    return render(request, 'login.html')

@login_required(login_url="login")
def record(request):
    pk = request.user.username
    records = Record.objects.all()
    j = ['plan', 'amount', 'type', 'date']
    context = {
     'myusers' :  records,
     'myuser' : Myuser.objects.get(username = pk)
     }
    return render(request, 'record.html', context)

@login_required(login_url="login")
def refer(request, ref):
    pk = request.user.username
    if Myuser.objects.get(username=pk) is None:
        Myuser.objects.get(username=pk).referral_id = f'{pk}{str(random.randint(100,1000))}'
        Myuser.save()
    context = {
        'payments' : payments,
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'refer.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password_confirmation']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                if Myuser.objects.filter(username=username).exists():
                    print('username exists')
                else:
                    user1 = Myuser.objects.create(name=fname +' '+lname, username=username, email=email,phone=phone)
                    user1.save()
                
                return redirect('login')
        else:
            messages.info(request, "passwords don't match")
            return redirect('register')
    else:            
        return render(request, 'signup.html')

@login_required(login_url="login")
def subscribe(request):
    pk = request.user.username
    payments = Deposit.objects.all()
    if request.method == 'POST':
        amount = request.POST['amount']
        type = request.POST['type']
        sub = Record.objects.create(username=request.user.username, plan=f'{type}(${amount})', type=type, amount=amount)
        sub.save()
        context = {
            'payments' : payments,
            'myuser' : Myuser.objects.get(username = pk)
        }
        return render(request, 'subscribe.html', context)
    else:
        context = {
            'payments' : payments,
            'myuser' : Myuser.objects.get(username = pk)
        }
        return render(request, 'subscribe.html', context)

@login_required(login_url="login")
def support(request):
    pk = request.user.username
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if name and email and message:
            support = Support.objects.create(username=pk, message=message, email=email)
            support.save()
            messages.info(request, 'message sent')
            return redirect('support')

    context = {
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'support.html', context)

@login_required(login_url="login")
def withdraw(request):
    pk = request.user.username
    if request.method == 'POST':
        method = request.POST['method']
        withdraw = Withdrawal.objects.create(username=pk, recieving_mode=method)
        withdraw.save()
        return redirect('withdraw_page')
    context = {
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'withdraw.html', context)
          
@login_required(login_url="login")
def xchange(request):
    pk = request.user.username
    data = crypto()
    if request.method == 'POST':
        source = request.POST['source']
        dest = request.POST['destination']
        amount = request.POST['amount']
        if source == 'btc':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'ltc':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'eth':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'link':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'bnb':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'ada':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'aave':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'xlm':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'xrp':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'bch':
            j = round(data['data']['1']['quote']['USD']['price'])
        elif source == 'usdt':
            j = round(data['data']['1']['quote']['USD']['price'])
    context = {
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'xchange.html', context)
              
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url="login")
def payment_page(request):
    pk = request.user.username
    payments = Deposit.objects.all().last()
    context = {
        'payment' : payments,
        'myuser' : Myuser.objects.get(username = pk)
    }

    return render(request, 'payment_page.html', context)
    
@login_required(login_url="login")
def withdraw_page(request):
    pk = request.user.username
    withdraws = Withdrawal.objects.all().last()
    context = {
        'withdraw' : withdraws,
        'myuser' : Myuser.objects.get(username = pk)
    }
    
    if request.method == 'POST':
        amount = request.POST['amount']
        address = request.POST['details']

        if withdraws.username == pk:
            method = withdraws.recieving_mode

            if withdraws.recieving_mode == 'Doge':
                j = float(amount)*(0.02)
                submit = Withdrawal_Page.objects.create(username=pk, amount_requested=amount, amount_charges=float(amount)+j, recieving_mode=method, address = address)
                submit.save()
            else:
                j = 0
                submit = Withdrawal_Page.objects.create(username=pk, amount_requested=amount, amount_charges=float(amount)+j, recieving_mode=method, address = address)
                submit.save()

    return render(request, 'withdraw_page.html', context)

    
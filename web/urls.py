from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name='home'),
    path("about", views.About, name='about'),
    path("contact", views.Contact, name='contact'),
    path("faqs", views.Faq, name='faq'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("deposit", views.deposit, name='deposit'),
    path("record", views.record, name='record'),
    path("refer/<str:ref>", views.refer, name='refer'),
    path("subscribe", views.subscribe, name='subscribe'),
    path("xchange", views.xchange, name='xchange'),
    path("withdraw", views.withdraw, name='withdraw'),
    path("account_history", views.account_history, name='account_history'),
    path("account", views.account, name='account'),
    path("support", views.support, name='support'),
    path("login", views.login, name='login'),
    path("signup", views.signup, name='signup'),
    path("logout", views.logout, name='logout'),
    path("payment_page", views.payment_page, name='payment_page'),
    path("withdraw_page", views.withdraw_page, name='withdraw_page'),
    path("account_bank", views.account_bank, name='account_bank'),
    #path("account_crypto", views.account_crypto, name='account_crypto'),
    path("account_password", views.account_password, name='account_password'),
    path("account_otp", views.account_otp, name='account_otp')
]
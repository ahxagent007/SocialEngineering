from django.urls import path
from .views import *

urlpatterns = [
    path('', GmailLogin, name='GmailLogin'),
]
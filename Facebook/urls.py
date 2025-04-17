from django.urls import path
from .views import *

urlpatterns = [
    path('', FBLogin, name='FBLogin'),
]
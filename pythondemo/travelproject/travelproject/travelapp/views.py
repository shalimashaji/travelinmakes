from django.contrib import messages, auth
# from django.contrib.auth.models import _user
from django.shortcuts import render, redirect

from travelapp.models import place
from travelapp.models import writer


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def demo(request):
    obj = place.objects.all()
    obc = writer.objects.all()
    return render(request, "index.html", {'result': obj, 'resul': obc})

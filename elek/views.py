from django.shortcuts import render
from .models import Elektro, Acsessuar, Nout



def site(request):
    return render(request, 'site.html')

def about(request):
    tel = Elektro.objects.all()
    data = {
        'tel': tel
    }

    return render(request, 'about.html', data)

def nout(request):
    nout = Nout.objects.all()
    da = {
        'nout': nout
    }
    return render(request, 'nout.html', da)

def chasy(request):
    chasy = Acsessuar.objects.all()
    dat = {
        'chasy': chasy
    }
    return render(request, 'chasy.html', dat)


from django.shortcuts import render, redirect
from .models import Elektro, Acsessuar, Nout
from .forms import ElektroForm



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

def create(request):
    error = ''
    if request.method == 'POST':
        form = ElektroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error = 'Форма была неверной'


    form = ElektroForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'create.html', data)
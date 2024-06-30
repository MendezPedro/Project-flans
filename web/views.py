from django.shortcuts import render, redirect
from .models import Flan

# Create your views here.
def inicio(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', context = {'flanes': flanes_publicos})

def about(request):
    return render(request, 'about.html')

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', context = {'flanes': flanes_privados})


def login(request):
    return redirect('account/login')

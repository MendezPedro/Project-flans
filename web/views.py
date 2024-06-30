from django.shortcuts import render, redirect
from .models import Flan, ContactForm
from django.http import HttpResponseRedirect
from .forms import ContactFormForm

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

def contacto(request):

    if request.method == 'POST':
        form = ContactFormForm(request.POST)

        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
        
    else:
        form = ContactFormForm()

    return render(request, 'contacto.html', context = {'form': form})

def exito(request):
    return render(request, 'exito.html')
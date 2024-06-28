from django.shortcuts import render, redirect

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def welcome(request):
    return render(request, 'welcome.html')


def login(request):
    return redirect('account/login')

from django.shortcuts import render

# Create your views here.

# Make sure this is spelled 'home' exactly as written below!
def home(request):
    return render(request, 'main/index.html')

def volunteer(request):
    return render(request, 'main/volunteer.html')

def about(request):
    return render(request, 'main/about.html')

def causes(request):
    return render(request, 'main/causes.html')

def contact(request):
    return render(request, 'main/contact.html')

def donate(request):
    return render(request, 'main/donate.html')

def exit(request):
    return render(request, 'main/exit.html')
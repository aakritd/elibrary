from django.shortcuts import render
from .models import book

# Create your views here.

def main(request):
    return render(request, "main.html")

def books(request):
    b = book.objects.all()
    return render(request,'books.html', {"bks" : b})

def about(request):
    return render(request, 'about.html')
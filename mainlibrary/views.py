from django.shortcuts import render
from .models import book
from .forms import SearchForm
# Create your views here.

def main(request):
    results = []

    if request.method == 'POST':#if i press the send button. request.method will be POST
        form = SearchForm(request.POST)#then form variable will have the content of the form
        if form.is_valid():
            query = form.cleaned_data['query']
            results = list(book.objects.filter(book_name__icontains=query))

    else:
        form =  SearchForm()
        results = None

    return render(request, 'main.html', {'form': form, 'results': results})



def books(request):
    b = book.objects.all()
    return render(request,'books.html', {"bks" : b})

def about(request):
    return render(request, 'about.html')


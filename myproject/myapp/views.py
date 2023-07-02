from django.shortcuts import render
from django.http import HttpResponse

def name(request):
    r='<h1>welcome to my world</h1>'
    return HttpResponse(r)

def form(request):
    return render(request,'myapp/myhtml.html')

# Create your views here.

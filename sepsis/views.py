from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"index.html")
def p(request):
    return render(request,"prevention.html")    
from django.shortcuts import render
from django.http import HttpResponse

def vista1(request):
    return HttpResponse("<h1>Vista 1 App1</h1>"
    "<p style='color:red'> Todo lo que necesites</p>")

from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request, 'index.html')
    return render(request, 'result.html')




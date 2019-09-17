from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'helloworld ！'
    context['test'] = 'test'
    return render(request,'hello.html',context)

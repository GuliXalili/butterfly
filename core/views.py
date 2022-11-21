from django.shortcuts import render

def chocolata(request):
    return render(request, 'index.html')

def cupcake(request):
    return render(request, 'index1.html')

def mandms(request):
    return render(request, 'index2.html')

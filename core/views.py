from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'core/core.html')

def szerviz(request):
    return render(request,'core/szerviz.html')

def mitsu(request):
    return render(request,'core/mitsubishi.html')

def kapcsolat(request):
    return render(request,'core/kapcsolat.html')

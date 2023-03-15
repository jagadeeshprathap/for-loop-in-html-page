from django.shortcuts import render

# Create your views here.
def asif(request):
    d={'name':'prathap','age':55}
    return render(request,'asif.html',d)
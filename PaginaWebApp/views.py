from django.shortcuts import render, HttpResponse

# Create your views here.

def Home (request):
    return render(request,"PaginaWebApp/Home.html")

def Servicios (request):
    return render(request,"PaginaWebApp/Servicios.html")


def Tienda (request):
    return render(request,"PaginaWebApp/Tienda.html")


def Blog (request):
    return render(request,"PaginaWebApp/Blog.html")


def Contacto (request):
    return render(request,"PaginaWebApp/Contactos.html")


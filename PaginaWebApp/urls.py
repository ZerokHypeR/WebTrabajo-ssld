from django.urls import path


from PaginaWebApp import views

urlpatterns = [
    path('Home', views.Home, name= "Home"),
    path("Servicios", views.Servicios, name= "Servicios"),
    path("Tienda", views.Tienda, name= "Tienda"),
    path("Blog", views.Blog, name= "Blog"),
    path("Contacto", views.Contacto, name= "Contactos"),
]

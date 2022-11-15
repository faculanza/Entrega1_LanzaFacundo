from django.urls import path
from AppEntrega import views

urlpatterns =[
    path('',views.inicio, name='Inicio'),
    path('fabricas/',views.fabricas, name='Fabricas'),  
    path('categorias/',views.categorias, name='Categorias'),  
    path('productos/',views.productos, name='Productos'),  
    path('AgregarFabrica/',views.AgregarFabrica, name='AgregarFabrica'),
    path('AgregarCategoria/',views.AgregarCategoria, name='AgregarCategoria'),
    path('AgregarProducto/',views.AgregarProducto, name='AgregarProducto'),
    path('buscarproducto/',views.buscarproducto, name='buscarproducto'),
    path('resultado_producto/',views.resultado_producto, name='resultado_producto'),

    


]
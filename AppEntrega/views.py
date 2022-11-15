#from django.http.request import QueryDict
#from AppEntrega.forms import AgreCat

from AppEntrega.models import Categorias, Fabricas, Productos
from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "index.html")

def fabricas(request):
    fabs = Fabricas.objects.all()
    return render(request, "fabricas.html", {"fabricas": fabs})


def categorias(request):
    fabs = Categorias.objects.all()
    return render(request, "categorias.html", {"categorias": fabs})


def productos(request):
    fabs = Productos.objects.all()
    #no pude hacer andar la consulta de acá abajo... :(
    #fabs = ListadoProductos.objects.all()
    return render(request, "productos.html", {"productos": fabs})

def buscarproducto(request):
    return render(request, "BuscarProducto.html")

def resultado_producto(request):
    nombre_producto = request.POST["producto"]

    producto = Productos.objects.filter(producto__icontains=nombre_producto)
    return render(request, "productos.html", {"productos": producto})

def AgregarFabrica(request):
    if request.method=="POST":
        #el 6 es un id que lo puse fijo para que funcione, no me anda el incremental, me da error si no cargo el ID
        agfabrica=Fabricas(6,request.POST['fabrica'])
        agfabrica.save()
        return render(request,"fabricas.html")
    return render(request, "AgregarFabrica.html")

def AgregarCategoria(request):
    if request.method=="POST":
        agcat=Categorias(4,request.POST['categoria'])
        agcat.save()
        return render(request,"categorias.html")
    return render(request, "AgregarCategoria.html")

#--------------------------------------------
# def AgregarCategoria(request):
#       if request.method == 'POST':
#             miFormulario = AgreCat(request.POST) #aquí mellega toda la información del html
#             print(miFormulario)
#             if miFormulario.is_valid:   #Si pasó la validación de Django
#                 informacion = miFormulario.cleaned_data
#                 agcat=Categorias(request.POST['categoria'])
#                 agcat.save()
#                 return render(request, "categorias.html") #Vuelvo al inicio o a donde quieran
#       else: 
#             miFormulario= AgreCat() #Formulario vacio para construir el html
#       return render(request, "AgregarCategoria.html", {"miFormulario":miFormulario})
#--------------------------------------------



def AgregarProducto(request):
    if request.method=="POST":
        agcat=Productos(4,request.POST['producto'],request.POST['precio'],request.POST['idfabrica'],request.POST['idcategoria'])
        agcat.save()
        return render(request,"productos.html")
    
    cats = Categorias.objects.all()
    categ = {"categorias": cats}

    fabs = Fabricas.objects.all()
    fabri = {"fabricas": fabs}

    categ.update(fabri)
    return render(request, "AgregarProducto.html", categ)
    
    #,{"fabricas:" fabs}
    


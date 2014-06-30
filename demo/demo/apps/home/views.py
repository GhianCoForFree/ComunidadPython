from django.shortcuts import render_to_response,RequestContext
from demo.apps.ventas.models import Producto
from demo.apps.home.forms import Contacto

def index(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about(request):
	sms = "Este es un mensaje desde la vista about"
	ctx = {'var':sms}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def productos(request):
	prod = Producto.objects.filter(estado=True)
	ctx = {'productos':prod}
	return render_to_response('home/productos.html',ctx,RequestContext(request))

def contacto(request):
	formu = Contacto()
	ctx = {'formul':formu}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))
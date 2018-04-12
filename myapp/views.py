from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Articulo
def like(request,id,accion):
	#Paso 1: crear el objeto
	art = Articulo.objects.get(pk=id)

	# paso 2: editar el objeto

	if accion == 'like':
		art.likes +=1
	else:
		art.dislikes +=1
		pass

	#paso 3: Guardar los cambios 

	art.save()

	return HttpResponseRedirect(reverse('articulo', args=[art.slug]))



def articulo(request,slug):
	art = Articulo.objects.get(slug=slug)
	return render(request,'articulo.html',{'articulo':art})


def index(request):
	

	#SELECT * FROM  Articulos ORDER BY id DESC: queryset
	articulos =  Articulo.objects.all().order_by('-id')

	return render(request,'index.html',{'articulos':articulos})
from django.shortcuts import render

# Create your views here.

def index (request):
	template_name = 'index.html'
	return render (request, template_name)

def cursos (request):
	template_name = 'cursos.html'
	return render (request, template_name)

def contato (request):
	template_name = 'contato.html'
	return render (request, template_name)
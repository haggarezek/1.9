from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request):
	context = {

	"title": "Detail"
	}
	return render(request, "index.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
	"object_list": queryset,
	"title": "List"
	}
	return render(request, "index.html", context)

		
	#return HttpResponse("<h1>list</h1>")

def post_update(request):
	return HttpResponse("<h1>update</h1>")

def post_delete(request):
	return HttpResponse("<h1>delete</h1>")
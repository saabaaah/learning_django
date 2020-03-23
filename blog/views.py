from django.shortcuts import render
from django.http import HttpResponse
# La liste des articles à afficher  est récupérée à partir de la BD#
from .models import Post

def home(request):
    # context #
    context = {
        'posts':Post.objects.all(),
        'title':'First django website',
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
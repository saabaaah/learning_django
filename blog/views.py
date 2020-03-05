from django.shortcuts import render
from django.http import HttpResponse

# La liste des articles à afficher #
posts = [
    {
        'author': 'Sabah HM',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Yassine K',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
def home(request):
    # context #
    context = {
        'posts':posts,
        'title':'First django website',
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/page_acceuil.html', {})

def jouer(request):
    return render(request, 'blog/liens.html', {})

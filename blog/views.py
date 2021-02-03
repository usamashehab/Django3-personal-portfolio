from django.shortcuts import render, get_object_or_404
from.models import blog

# Create your views here.


def BlogHome(request):
    blogs = blog.objects.order_by('-date')
    return render(request, 'blog/home.html', {'blogs': blogs})


def article(request, blog_id):
    article = get_object_or_404(blog, pk=blog_id)
    return render(request, 'blog/article.html', {'article': article})

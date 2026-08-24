from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from blog.models import Category, Post


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def categories(request):
    categories = Category.objects.all()
    return render(request,
                  'blog/categories.html',
                  {'categories': categories})


def posts(request):
    posts = Post.objects.all()
    users = User.objects.all()
    categories = Category.objects.all()
    return render(request,
                  'blog/posts.html',
                  {
                      'posts': posts,
                      'users': users,
                      'categories': categories
                  })


def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, "blog/category_detail.html",
                  {'category': category})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "blog/post_detail.html",
                  {'post': post})


def category_create(request):
    category_name = request.POST['name']
    category = Category.objects.create(name=category_name)
    return redirect('categories')


def category_update(request, category_id):
    category = Category.objects.get(id=category_id)
    category.name = request.POST['name']
    category.save()
    return redirect('categories')


def category_delete(request):
    category_id = request.POST['category_id']
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('categories')


def post_create(request):
    title = request.POST['title']
    header_image = request.FILES['header_image']
    title_tag = request.POST['title_tag']
    author = User.objects.get(id=request.POST['author'])
    body = request.POST['body']
    snippet = request.POST['snippet']
    category = Category.objects.get(id=request.POST['category'])

    post = Post.objects.create(title=title,
                               header_image=header_image,
                               title_tag=title_tag,
                               author=author,
                               body=body,
                               snippet=snippet,
                               category=category)
    return redirect('posts')
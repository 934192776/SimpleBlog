from django.contrib.auth.models import User
#从Django内置的“用户认证系统”中导入“用户模型”
# 这个user模型是django自带的，存了用户名，密码，邮箱

from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# 导入"渲染"和“重定向”功能
# render = 把html页面渲染出来显示给用户
# redirect = 处理完请求后跳转到另一个页面


from blog.models import Category, Post


# 从blog应用的models.py中导入category和post模型
# category = 分类（比如：内科，外科）
# post = 文章/帖子


# 首页视图， 定义一个叫“home”的视图函数
def home(request):  # request = 用户发来的请求（包含所有信息）
    return render(request, 'blog/home.html')


# render = 渲染页面功能
#参数1： request 请求对象
# 参数2： ‘blog/home.html'(要显示的html模板文件）
# 返回一个完整的HTML页面给用户


# 分类列表视图
def categories(request):  #从数据库查出所有分类
    categories = Category.objects.all()  #把所有分类存到变量categories里 # Category.bojects.all() = SELECT * FROM category
    return render(request,  # 把查到的categories数据传给模板
                  'blog/categories.html',  # 渲染categories.html页面
                  {'categories': categories})  # 模板里可以用{{categories}} 来显示数据


# 文章列表页视图
def posts(request):
    posts = Post.objects.all()  # 从数据库查出所有文章 # post.objects.all() = SELECT * FROM post
    users = User.objects.all()  # 从数据库查出所有用户 # User.objects.all() = SELECT * FROM user
    categories = Category.objects.all()  # 从数据库查出所有分类 # Category.objects.all() = SELECT * FROM category
    return render(request,
                  'blog/posts.html',  # 渲染posts.html页面
                  {
                      'posts': posts,
                      'users': users,
                      'categories': categories
                  })


#单个分类详情页视图
def category_detail(request, category_id):  # category_id = 从URL中提取的分类
    category = Category.objects.get(
        id=category_id)  # Category.objects.get(id=category_id) = SELECT *FROM category WHERE id=1
    # 根据id从数据库查出某个分类 # 用户访问/category/1/时，category_id = 1
    return render(request, "blog/category_detail.html",  # 渲染category_detail.html页面
                  {'category': category})  # 把查到的category数据传给模板


# 单篇文章详情页视图
def post_detail(request, post_id):  # post_id = 从URL中提取的分类
    post = Post.objects.get(id=post_id)  # Post.objects.get(id=post_id) = SELECT * FROM post WHERE id=1
    # 根据id从数据库查出某篇文章  # 用户访问/post时，post_id = 1
    return render(request, "blog/post_detail.html",  # 渲染post_detail.html页面
                  {'post': post})  # 把查到的post数据传给模板


# 创建分类的视图（处理表单提交）
def category_create(request):
    # 从用户提交的POST数据中获取分类名称
    category_name = request.POST['name']
    # request.POST = 用户提交的表单数据
    category = Category.objects.create(name=category_name)
    # 在数据库里创建一条新分类记录
    # Category.objects.create(name=category_name = INSERT INTO category(name) VALUE('新分类 '）
    return redirect('categories')
    # 处理完后重定向到“分类列表 ”页面
    # redirect('categories') = 跳转到名字叫‘categories' 的页面
    # 这个名字对应url.py里的name='categories'


# 更新分类的视图
def category_update(request, category_id):
    # 根据ID查出要修改的分类
    category = Category.objects.get(id=category_id)
    category.name = request.POST['name']
    # 把分类名称改成用户提交的新名称
    # request.POST['name'] = 表单里输入的新名称
    category.save()  # 保存到数据库  # .save()= UPDATE category SET name= '新名称 ’ WHERE id=category_id
    return redirect('categories')
    # 重定向到分类列表页


# 删除分类视图
def category_delete(request):
    # 从表单中获取要删除的分类ID， 用的是POST数据， 不是URL参数
    category_id = request.POST['category_id']
    category = Category.objects.get(id=category_id)
    # 根据ID查出要删除的分类
    category.delete()
    # 从数据库删除
    return redirect('categories')
    # 重定向到分类列表页


# 创建文章的视图
def post_create(request):
    title = request.POST['title']
    # 从表单获取标题
    # request.POST['title'] = 表单里name="title"的输入框
    header_image = request.FILES['header_image']
    # 从表单获取图片文件
    # request.FILES = 用户上传的文件
    title_tag = request.POST['title_tag']
    # 从表单获取标题标签
    author = User.objects.get(id=request.POST['author'])
    # 从表单获取作者ID，然后从数据库查出对应的用户对象
    # request.POST['author']= 下拉选择框选中的作者ID

    body = request.POST['body']  # 从表单获取正文
    snippet = request.POST['snippet']  # 从表单获取摘要
    category = Category.objects.get(id=request.POST['category'])
    # 从表单获取分类ID，然后查出对应的分类对象

    post = Post.objects.create(  # 在数据库里创建新文章， 把所有字段传进去
        title=title,
        header_image=header_image,
        title_tag=title_tag,
        author=author,  # 传入用户对象（外键）
        body=body,
        snippet=snippet,
        category=category)  # 传入分类对象（外键）
    return redirect('posts')
    # 创建成功后重定向到文章列表页


# 更新文章的视图

def post_update(request, post_id):
    """
    更新文章
    """
    # 1. 根据ID查出要修改的文章
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        # 2. 从表单获取新的数据
        post.title = request.POST.get('title')
        post.title_tag = request.POST.get('title_tag')
        post.body = request.POST.get('body')
        post.snippet = request.POST.get('snippet')

        # 3. 如果有上传新图片，更新图片
        if 'header_image' in request.FILES:
            post.header_image = request.FILES['header_image']

        # 4. 如果修改了作者或分类
        if 'author' in request.POST:
            post.author = User.objects.get(id=request.POST['author'])
        if 'category' in request.POST:
            post.category = Category.objects.get(id=request.POST['category'])

        # 5. 保存到数据库
        post.save()

        # 6. 重定向到文章列表页
        return redirect('posts')

    # GET请求：显示编辑表单
    users = User.objects.all()
    categories = Category.objects.all()

    context = {
        'post': post,
        'users': users,
        'categories': categories,
    }
    return render(request, 'blog/post_update.html', context)


# 删除文章的视图（新增）

def post_delete(request):
    """
    删除文章
    """
    if request.method == 'POST':
        # 1. 从表单中获取要删除的文章ID
        post_id = request.POST.get('post_id')

        # 2. 根据ID查出要删除的文章
        post = Post.objects.get(id=post_id)

        # 3. 从数据库删除
        post.delete()

        # 4. 重定向到文章列表页
        return redirect('posts')

    # 如果不是POST请求，重定向到文章列表
    return redirect('posts')


# 还需要修改 post_create 视图，因为模板里用到了 users 和 categories

class TemplateView:
    pass


def post_create(request):
    """
    创建文章（修改版 - 支持GET和POST）
    """
    # 如果是GET请求，显示创建表单
    if request.method == 'GET':
        users = User.objects.all()
        categories = Category.objects.all()
        context = {
            'users': users,
            'categories': categories,
        }
        return render(request, 'blog/post_create.html', context)

    # 如果是POST请求，处理表单提交
    if request.method == 'POST':
        title = request.POST.get('title')
        header_image = request.FILES.get('header_image')
        title_tag = request.POST.get('title_tag')
        author = User.objects.get(id=request.POST.get('author'))
        body = request.POST.get('body')
        snippet = request.POST.get('snippet')
        category = Category.objects.get(id=request.POST.get('category'))

        post = Post.objects.create(
            title=title,
            header_image=header_image,
            title_tag=title_tag,
            author=author,
            body=body,
            snippet=snippet,
            category=category
        )
        return redirect('posts')


class PostListTemplate(TemplateView):
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['categories'] = Category.objects.all()
        context['users'] = User.objects.all()
        print(context)
        print(type(context))
        return context


class PostList_Generic(ListView):
    model = Post
    template_name = "blog/posts_list_view.html"

class PostDetail_Generic(DetailView):
    model = Post
    template_name = "blog/posts_detail_view.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_create_view.html"
    success_url = "/post_list_view"
    # form_class =
    fields = ['title', 'header_image', 'title_tag',
              'author', 'body', 'snippet', 'category'
]

class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_update_view.html"
    success_url = "/post_list_view"
    form_class = PostCreateView

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete_view.html"
    success_url = "/post_list_view"



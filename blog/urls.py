from django.urls import path
# 从Django的URL工具中导入 path 函数
# path = 用来定义URL路径和视图的对应关系

from blog.views import home, categories, posts, category_detail, post_detail, category_create, category_update, \
    category_delete, post_create, post_update, post_delete, PostList_Generic, PostDetail_Generic, \
    PostUpdateView, PostCreateView, PostDeleteView, PostListTemplate

# 从blog/views.py导入所有视图函数
# 这样下面才能使用这些函数名

urlpatterns = [# urlpatterns = 路由列表（所有URL规则的集合）
               # 就像"导航地图"，告诉Django用户访问什么网址该去哪里
    path("", home, name="home"),
# 首页
    # path('', ...) = 空路径，就是根地址
    # 比如：http://127.0.0.1:8000/
    # 访问时执行 home 视图
    # name='home' = 给这个URL起个名字，方便其他地方引用

    path("categories/", categories, name="categories"),
# 分类列表页
    # path('categories/', ...) = 访问 /categories/ 时
    # 比如：http://127.0.0.1:8000/categories/
    # 执行 categories 视图

    path("posts/", posts, name="posts"),
    # 文章列表页
    # 访问 /posts/ 时执行 posts 视图


    path("category/<int:category_id>/", category_detail, name="category_detail"),
# 单个分类详情页
    # path('category/<int:category_id>/', ...)
    # <int:category_id> = 从URL中提取一个整数作为分类ID
    # 比如访问 /category/1/ 时，category_id = 1
    # 执行 category_detail 视图，并把1传给它


    path("post/<int:post_id>/", post_detail, name="post_detail"),
# 单篇文章详情页
    # 访问 /post/1/ 时，post_id = 1
    # 执行 post_detail 视图


    path("category/create/", category_create, name="category_create"),
# 创建分类（处理表单提交）
    # 访问 /category/create/ 时执行 category_create

    path("category/update/<int:category_id>/", category_update,
         name="category_update"),
    # 更新分类（处理表单提交）
    # 访问 /category/update/1/ 时，category_id = 1
    # 执行 category_update

    path("category/delete/", category_delete,
         name="category_delete"),
# 删除分类（处理表单提交）
    # 访问 /category/delete/ 时执行 category_delete

    path("post/create/", post_create, name="post_create"),
   # 创建文章（处理表单提交），访问 /post/create/ 时执行 post_create

    path("post/update/<int:post_id>/", post_update, name="post_update"),
    # 更新分类（处理表单提交）
    # 访问 /post/update/1/ 时，post_id = 1
    # 执行 post_update

    path("post/delete/", post_delete, name="post_delete"),
# 删除分类（处理表单提交）
    # 访问 /post/delete/ 时执行 post_delete

    path("post_template_view", PostListTemplate.as_view(),
         name="post_template_view"),

    path("post_list_view", PostList_Generic.as_view(),
         name="post_list_view"),

    path("post_detail_view/<int:pk>/",
         PostDetail_Generic.as_view(),
         name="post_detail_view"),

    path("post_create_view", PostCreateView.as_view(),
         name="post_create_view"),

    path("post_update_view/<int:pk>/",PostUpdateView.as_view(),
         name="post_update_view"),

path("post_delete_view/<int:pk>/",PostDeleteView.as_view(),
         name="post_delete_view"),
    ]
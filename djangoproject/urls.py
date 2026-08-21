# 目录/导航
# 告诉请求该去哪里

from django.urls import path

from blog.views import home, categories

urlpatterns = [
    path("", home, name="home"),
    path("categories/", categories, name="categories"),
]
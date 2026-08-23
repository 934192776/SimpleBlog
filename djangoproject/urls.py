# 目录/导航
# 告诉请求该去哪里

from django.contrib import admin

from django.urls import path

from blog.views import home, categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("categories/", categories, name="categories"),
]
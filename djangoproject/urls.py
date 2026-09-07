# 目录/导航
# 告诉请求该去哪里
from django.conf.urls.static import static
from django.contrib import admin


from django.urls import path, include

from djangoproject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('blog.urls')),
    path("accounts/", include("django.contrib.auth.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
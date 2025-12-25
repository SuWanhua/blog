from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogs.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] 

# 注意这里的写法：urlpatterns 后面必须有一个 += 或者放在列表里用 + 拼接
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
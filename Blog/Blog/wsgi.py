import os

from django.core.wsgi import get_wsgi_application

# 确保这里的 'Blog.settings' 与你的项目文件夹名称一致
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')

application = get_wsgi_application()
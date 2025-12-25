from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    # 确保这里叫 content，不是 text 或其他名字
    content = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)
    # 确保这里叫 image
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image'] # 与模型字段严格对应
        labels = {
            'title': '标题',
            'content': '正文内容',
            'image': '图片附件',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
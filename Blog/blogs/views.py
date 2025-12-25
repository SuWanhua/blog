from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied # 导入权限异常
from .models import BlogPost
from .forms import BlogPostForm

# 首页列表
def index(request):
    posts = BlogPost.objects.order_by('-date_added')
    return render(request, 'blogs/index.html', {'posts': posts})

# 删除博文逻辑
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    
    # 权限检查：必须是作者本人或者是超级管理员
    if post.owner == request.user or request.user.is_superuser:
        post.delete()
        return redirect('blogs:index')
    else:
        # 如果不是作者且不是超级用户，禁止操作
        raise PermissionDenied

# 注册逻辑
def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:index')
    return render(request, 'registration/register.html', {'form': form})

# 新建博文
@login_required
def new_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
    return render(request, 'blogs/new_post.html', {'form': form})

# 编辑博文
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    # 编辑权限：仅作者或超级管理员
    if post.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
        
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    return render(request, 'blogs/edit_post.html', {'form': form, 'post': post})

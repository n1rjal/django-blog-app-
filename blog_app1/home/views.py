from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Blog, Comment
from django.views.generic import ListView
from datetime import datetime
from .forms import Comments
from django.contrib.auth import (logout, authenticate)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count

def index(requests):
    if requests.user.is_anonymous:
        return redirect("members/login")
    else:
        User = requests.user
        username = User.id
        if requests.method == 'POST':
            title = requests.POST.get('title')
            content = requests.POST.get('content')
            if (title and content) == '':
                return redirect('/')
            else:

                blog = Blog(aurthor=User, title=title, content=content)
                blog.save()
                return redirect('blogs')

    return render(requests, 'index.html', {'user': User})


class Show_bLogs(LoginRequiredMixin, ListView):
    login_url = 'members/login/'
    model = Blog
    template_name = 'blogs.html'
    ordering = ['-time']

    # def get_context_data(self, **kwargs):
    #     context = super(Show_bLogs, self).get_context_data(**kwargs)
    #     context['comments'] = Comment.objects.all()
    #     context['form'] = Comments()
    #     return context

    # def post(self, request, *args, **kwargs):
    #     form = Comments(request.POST)
    #     print(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.post_id = request.POST.get("post")
    #         comment.save()
    #         return redirect('/blogs')
    #     else:
    #         return HttpResponse("Db issue here.")


def view_blog(request, pk_second):
    if request.user.is_anonymous:
        return redirect("login")
    else:
        blog = Blog.objects.get(pk=pk_second)
        author = request.user
        commenty = blog.comments.annotate(count=Count('like')).order_by('-count')
        form = Comments(initial={'post': blog})
        if request.method == 'POST':

            form = Comments(request.POST, initial={'post': blog})
            if form.is_valid():
                comment = form.save()
                if not request.user.is_anonymous:

                    comment.name = request.user
                    comment.save()

        context = {'blog': blog, 'commenty': commenty,
                   'form': form, 'aurthor': author}

        return render(request, 'view_blog.html', context)


def user_profile(request, pk):
    author = User.objects.get(pk=pk)

    if request.user.is_anonymous:
        return redirect("login")
    else:
        posts = author.blog_set.all().order_by('-time')
        user_main = request.user
    context = {'posts': posts, 'user': user_main, 'show_user': author}
    return render(request, 'user_profile.html', context)


# def user_profile_id(request , pk):
#     profile= User.objects.get(pk=pk)

#     posts = profile.blog_set.all().order_by('-time')

#     context={'posts':posts,}
#     return render(request, 'user_profile.html', context)

def like_comment(request, blog_id, comment_id):
    comment = Comment.objects.filter(post__id=blog_id).filter(pk=comment_id).first()
    comment.like.add(request.user)
    comment.save()
    return redirect('view_blog', pk_second=blog_id)

from django.contrib import admin
from django.urls import path, include
from home import views
from .views import Show_bLogs
from members import urls
urlpatterns = [
    path('', views.index, name='home'),
    path('blogs', Show_bLogs.as_view(), name='blogs'),
    path('view_blog/<int:pk_second>', views.view_blog, name='view_blog'),
    path('view_blog/<int:blog_id>/like/<int:comment_id>',
         views.like_comment, name='like_comment'),
    path('profile/<int:pk>', views.user_profile, name='user_profile'),
    path('serach', views.serach, name='serach'),
    # path('profile/<int:pk>', views.user_profile_id, name='user_profile_id')
]

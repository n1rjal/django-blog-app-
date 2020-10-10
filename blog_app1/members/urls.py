from django.contrib import admin
from django.urls import path , include
from members import views

urlpatterns = [
    path('register/' , views.register , name = 'register'),
    path('login/' , views.loginUser , name = 'login'),
    path('logout_user/' , views.logoutUser , name = 'logut'),
    path('oauth/', include('social_django.urls', namespace='social')),
]

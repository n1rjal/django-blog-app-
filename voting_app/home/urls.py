from django.urls import path , include
from home import urls , views
from home.views import view_qestion , vote_here
app_name = 'home'
urlpatterns = [
    path('',  view_qestion.as_view(), name = 'home'),
    path('vote_here/<int:pk_second>', views.vote_here , name = 'vote_here'),
    path('new' , views.new_vote , name = 'new')
]

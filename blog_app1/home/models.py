from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    aurthor = models.ForeignKey(User , null=True , on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.title)


class Comment(models.Model):
    post = models.ForeignKey(Blog , null=True ,blank=True, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(User , related_name='likes')

    def __str__(self):
        return str(self.name) + '  ' + str(self.post)

class Profile(models.Model):
    user = models.OneToOneField(User , null=True , blank=True , on_delete=models.CASCADE)
    profile_pic = models.ImageField(null= True , blank= True , upload_to = 'static/mages/profile')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | {self.user}"

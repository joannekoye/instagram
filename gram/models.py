from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Profile(models.Model):
    main_user = models.ForeignKey(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 300, blank = True, default='')
    pic = models.ImageField(upload_to = 'images/', null =True, blank = True, default='')
    followers = models.CharField(max_length = 30, blank = True, default = 0)
    following = models.CharField(max_length = 30, blank = True, default = 0)

    def __str__(self):
        return self.main_user.username

    @classmethod
    def search_users(cls,name):
        users=cls.objects.filter(main_user__username__icontains=name)
        return users

    @classmethod
    def get_profile(cls,user):
        profile=cls.objects.get(main_user=user)
        return profile

class Comment(models.Model):
    comment = models.TextField(max_length = 30)
    main_user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Like(models.Model):
    picture = models.CharField(max_length = 30, default = '')
    main_user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.main_user.username

class Image(models.Model):
    image_path = models.ImageField(upload_to = 'images/')
    main_user = models.ForeignKey(User, on_delete = models.CASCADE)
    caption = models.TextField(blank = True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.CharField(max_length = 30, blank = True, default = 0)
    comments = models.CharField(max_length = 30, blank = True, default = 0)

    def __str__(self):
        return self.name
        return self.caption

class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to )



from django.contrib import admin
from .models import Image, Comment, Profile, Like, Contact

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Contact)
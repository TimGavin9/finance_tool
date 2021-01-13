from django.contrib import admin

# Register your models here.
from .models import Post, Stock

admin.site.register(Post)
admin.site.register(Stock)
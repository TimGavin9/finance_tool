from django.contrib import admin
from django.urls import path, include

from posts.views import home_view, post_list_view, quotes_home_view, about_view, post_create_view, add_stock_view, delete_stock_view, delete_view, crypto_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    #path('posts/<int:post_id>', post_detail_view),
    path('posts/', post_list_view),
    path('create-post', post_create_view),
    path('quotes', quotes_home_view, name='home'),
    path('about', about_view, name='about'),
    path('add_stock', add_stock_view, name='add_stock'),
    path('delete/<stock_id>', delete_view, name='delete'),
	path('delete_stock', delete_stock_view, name='delete_stock'),
    path('crypto_view', crypto_view, name='crypto_view'),
]

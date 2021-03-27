from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog')
    # path('', views.all_posts, name='blog'),
    path('<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
]
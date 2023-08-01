from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import BlogView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [

    path('', BlogView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<str:slug>/', cache_page(60)(BlogDetailView.as_view()), name='blog_article', ),
    path('update/<str:slug>/', BlogUpdateView.as_view(), name='blog_update', ),
    path('delete/<str:slug>/', BlogDeleteView.as_view(), name='blog_delete', ),

]
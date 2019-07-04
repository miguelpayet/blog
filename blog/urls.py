from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog.blog_index, name="blog"),
    path('<slug:slug>', views.blog.blog_page, name="page"),
]

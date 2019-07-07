from django.urls import path

from app import views

urlpatterns = [
    path('', views.blog.blog_index, name="blog"),
    path('buscar', views.buscar, name="buscar"),
    path('<slug:slug>', views.blog.blog_page, name="page"),
]

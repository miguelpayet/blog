from django.urls import path

from app import views

urlpatterns = [
    path('', views.blog.blog_index, name="blog"),
    path('<slug:slug>/', views.blog.blog_page, name="page"),
    path('buscar', views.buscar, name="buscar"),
    path('galeria/<str:nombre>/', views.galeria, name="page"),
]

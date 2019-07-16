from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app import views

urlpatterns = [
                  path('', views.BlogIndexView.as_view(), name="blog"),
                  path('<slug:slug>/', views.BlogPageView.as_view(), name="page"),
                  path('buscar', views.BuscarView.as_view(), name="buscar"),
                  path('galeria/<str:nombre>/', views.GaleriaView.as_view(), name="page"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

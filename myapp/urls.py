from django.urls import path
from . import views  # como esta en la misma carpeta lo puedo importar con '.'


urlpatterns = [
    path("", views.hello2),
    path("about/", views.about),
]

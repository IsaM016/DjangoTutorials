from django.urls import path
from .views import homePageView  # Importa la vista basada en función

urlpatterns = [
    path("", homePageView, name="home"),  # Usa la vista basada en función
]
from django.urls import path
from .views import homePageView, AboutPageView, ContactPageView  # Importa ContactPageView

urlpatterns = [
    path("", homePageView, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),  # Nueva ruta para la página de contacto
]
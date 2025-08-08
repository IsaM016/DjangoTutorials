from django.shortcuts import render
from django.views.generic import TemplateView

# Function-based view
def homePageView(request):
    return render(request, "pages/home.html")  # Renderiza la plantilla

# Class-based view (opcional)
class HomePageView(TemplateView):
    template_name = "pages/home.html"
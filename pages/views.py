from django.shortcuts import render
from django.views.generic import TemplateView

# Function-based view
def homePageView(request):
    return render(request, "pages/home.html")  # Renderiza la plantilla

# Class-based view (opcional)
class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact Us - Online Store",
            "subtitle": "Contact Us",
            "email": "contact@onlinestore.com",
            "address": "123 Fake Street, Faketown, FK 12345",
            "phone": "+1 (555) 123-4567",
        })
        return context
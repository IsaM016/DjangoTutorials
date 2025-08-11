from django import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect  # Import necessary classes


# Function-based view
def homePageView(request):
    return render(request, "pages/home.html")  # Render the home page template


# Class-based view (optional)
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


# Product-related views
class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 10.0000},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 999.99},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 999.99},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 999.99}
    ]


class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)


class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        # Check if the product exists in the static list
        product = next((p for p in Product.products if p["id"] == id), None)
        if product is None:
            # Redirect to the home page if the product is not found
            return HttpResponseRedirect('/')

        # Render the product details if found
        return render(request, self.template_name, {"product": product})


# Form for creating a product
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("The price must be greater than zero.")
        return price


class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {
            "title": "Create Product",
            "form": form,
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            # Redirect to the success page
            return render(request, 'products/success.html', {"title": "Success"})
        else:
            viewData = {
                "title": "Create product",
                "form": form,
            }
            return render(request, self.template_name, viewData)
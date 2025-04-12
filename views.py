from django.views.generic import DetailView, TemplateView
from .models import Product

class HomeView(TemplateView):
    template_name = 'vantry/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Welcome to Vantry!"
        return context
    

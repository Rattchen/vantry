from django.views.generic import DetailView, TemplateView
from openfoodfacts import API, APIVersion, Country, Environment, Flavor
from .models import Product

class HomeView(TemplateView):
    template_name = 'vantry/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Welcome to Vantry!"
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'vantry/product_details.html'
    context_object_name = 'product'

    ## If obj.off_id -> return OFF item
    ## Else -> return DB item + info how to add an item

class OFFView(TemplateView):
    template_name = 'vantry/off.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api = API(user_agent="Vantry",
            username=None,
            password=None,
            country=Country.pl,
            flavor=Flavor.off,
            version=APIVersion.v2,
            environment=Environment.net
            )
        code = "5900500047459"
        item = api.product.get(code, fields=['product_name', 'nutriments', 'generic_name', 'brands', 'brands_hierarchy'])
        context["item"] = item
        print(item)
        return context
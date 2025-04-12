from django.views.generic import DetailView, TemplateView
from openfoodfacts import API, APIVersion, Country, Environment, Flavor
from .models import Product
from .dto import ProductDTO

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
        code = str(self.kwargs["barcode"])
        fields=['code', 'product_name', 'nutriments', 'brands']
        json = api.product.get(code, fields)

        product = ProductDTO.from_json(json)
        context["product"] = product
        return context
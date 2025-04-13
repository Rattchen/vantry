from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('stashes', views.StorageListView.as_view(), name='storage_list'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_details'),
    path('product/off/<int:barcode>', views.OFFView.as_view(), name='product_off'),
]

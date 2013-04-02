from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from product.views import ProductCategoryView, ProductListView, ProductInfoView

urlpatterns = patterns("",
    url(r"^(?P<category>\d+)$",
    	ProductCategoryView.as_view(), 
    	name="product_category"),
    url(r"^(?P<category>\d+)/(?P<type>\d+)$",
    	ProductListView.as_view(),
        name="product_list"),
    url(r'^info/(?P<pk>\d+)$',
        ProductInfoView.as_view(),
        name="product_detail"),
)

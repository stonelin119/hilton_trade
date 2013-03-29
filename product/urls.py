from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from product.views import ProductCategoryView, ProductListView, ProductInfoView

urlpatterns = patterns("",
    url(r"^(?P<category>\d+)$",
    	ProductCategoryView.as_view(), 
    	name="product"),
    url(r"^category/(?P<type>\d+)$",
    	ProductListView.as_view(),
    	name="products"),
    url(r'^info/(?P<pk>\d+)$',
        ProductInfoView.as_view(),
        name="product_detail"),
    url(r'^imp&exp$',
        TemplateView.as_view(template_name="product/imp&exp.html"),
        name="imp&exp"),
)

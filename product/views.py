from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView

from product.models import ProductCategory, ProductInfo, ProductInfoDetail, ProductType 

class ProductInfoView(DetailView):
    model = ProductInfo
    template_name = 'product/product.html'

class ProductCategoryView(ListView):
    model = ProductCategory 
    template_name = 'product/base.html'
    context_object_name = "product_categories"
    queryset = ProductCategory.objects.all()
    paginate_by = 10

    def get_context_data(self, **kwargs):
       context = super(ProductCategoryView, self).get_context_data(**kwargs)
       current_category = self.kwargs['category']
       current_type = ProductType.objects.filter(category_id=current_category)[0]
       context['current_type'] = current_type.id 
       return context

class ProductListView(ListView):
    model = ProductInfo
    template_name = 'product/products.html'
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        product_type = self.kwargs['type'] 
        queryset = ProductInfo.objects.filter(product_type__id=product_type)
        return queryset

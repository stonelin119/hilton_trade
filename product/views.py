from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView

from product.models import ProductCategory, ProductInfo, ProductInfoDetail, ProductType 

class ProductInfoView(DetailView):
    model = ProductInfo
    template_name = 'product/product.html'
    context_object_name = "product_info"

class ProductCategoryView(ListView):
    model = ProductCategory 
    template_name = 'product/base.html'
    context_object_name = "product_categories"
    queryset = ProductCategory.objects.all()
    paginate_by = 2 

    def get_context_data(self, **kwargs):
       context = super(ProductCategoryView, self).get_context_data(**kwargs)
       current_category = int(self.kwargs['category'])
       current_type = -1
       if current_category != 3:
           current_type = ProductType.objects.filter(category_id=current_category)[0].id

       context['current_type'] = current_type
       return context

class ProductListView(ListView):
    model = ProductInfo
    template_name = 'product/products.html'
    context_object_name = "products"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        product_type = int(self.kwargs['type'])
        current_type = ProductType.objects.get(id=product_type)
        context['path'] = [current_type.category.category_name, current_type.type_name]
        context['product_type'] = product_type
        return context

    def get_queryset(self):
        product_type = self.kwargs['type'] 
        queryset = ProductInfo.objects.filter(product_type__id=product_type)
        return queryset

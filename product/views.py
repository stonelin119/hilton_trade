from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView

from product.models import ProductCategory, ProductInfo, ProductInfoDetail, ProductType 

class ProductInfoView(DetailView):
    model = ProductInfo
    template_name = 'product/product.html'
    context_object_name = "product_info"

class ProductCategoryView(ListView):
    model = ProductCategory 
    template_name = 'product/category.html'
    context_object_name = "product_categories"
    queryset = ProductCategory.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        current_category = ProductCategory.objects.get(id=int(self.kwargs['category']))

        context['current_category'] = current_category 
        context['path'] = [current_category.category_name]
        return context

class ProductListView(ListView):
    model = ProductInfo
    template_name = 'product/pagination_base.html'
    context_object_name = "products"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        current_type = ProductType.objects.get(id=int(self.kwargs['type']))
        current_category = ProductCategory.objects.get(id=int(self.kwargs['category']))
        context['product_categories'] = ProductCategory.objects.all()
        context['current_category'] = current_category 
        context['current_type'] =current_type 
        context['path'] = [current_category.category_name, current_type.type_name]
        return context

    def get_queryset(self):
        product_type = self.kwargs['type'] 
        queryset = ProductInfo.objects.filter(product_type__id=product_type)
        return queryset

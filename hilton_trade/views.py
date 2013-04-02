from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView

from product.models import ProductCategory

class HomepageView(ListView):
    model = ProductCategory 
    template_name = 'homepage.html'
    context_object_name = "product_categories"
    queryset = ProductCategory.objects.all()

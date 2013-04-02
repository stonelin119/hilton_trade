from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from hilton_trade.views import HomepageView 

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', HomepageView.as_view(), name="home"),
    url(r'^about$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^contact$', TemplateView.as_view(template_name="contact.html"), name="contact"),
    url(r'^product/', include('product.urls')),
    # url(r'^account/', include('account.urls')),
)
